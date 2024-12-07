import asyncio
from urllib.parse import urlparse

from playwright.async_api import async_playwright

async def execute(api: str, get_json: bool = True):
    async with async_playwright() as ap:
        browser = await ap.chromium.launch(headless=True)
        context = await browser.new_context()
        await context.clear_cookies()
        page = await context.new_page()

        api_response = None

        # Gestore per le risposte intercettate
        async def handle_response(response):
            nonlocal api_response
            if response.url == api and response.status == 200:
                if get_json:
                    api_response = await response.json()
                else:
                    api_response = await response.text()

        # Ascolta l'evento 'response'
        page.on("response", handle_response)

        # Analizza l'URL di base
        parsed_url = urlparse(api)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

        # Vai al dominio base
        await page.goto(base_url)

        # Esegui la chiamata API con fetch
        await page.evaluate(f"""
            fetch("{api}", {{
                method: "GET",
                headers: {{
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
                    "Accept": "application/json",
                    "Referer": "{base_url}"
                }}
            }}).then(response => response).then(console.log);
        """)

        # Attendi che la risposta venga intercettata
        for _ in range(50):  # Max 5 secondi
            if api_response:
                break
            await asyncio.sleep(0.1)

        # Chiudi il browser
        await browser.close()

        # Restituisci la risposta
    return api_response
