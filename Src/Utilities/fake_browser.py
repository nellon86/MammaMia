import asyncio
import json
from urllib.parse import urlparse

from playwright.async_api import async_playwright


async def execute(api: str, more_headers: dict = None, get_json: bool = True):
    async with async_playwright() as ap:
        browser = await ap.chromium.launch(headless=True)
        context = await browser.new_context()
        await context.clear_cookies()
        page = await context.new_page()

        api_response = None

        async def handle_response(response):
            nonlocal api_response
            if response.url == api and response.status == 200:
                if get_json:
                    api_response = await response.json()
                else:
                    api_response = await response.text()

        page.on("response", handle_response)

        parsed_url = urlparse(api)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

        await page.goto(base_url)

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            "Accept": "application/json",
            "Referer": f"{base_url}",
            "Origin": f"{base_url}"
        }
        if more_headers is not None:
            headers.update(more_headers)

        await page.evaluate(f"""
            fetch("{api}", {{
                method: "GET",
                headers: {json.dumps(headers)}
            }}).then(response => response).then(console.log);
        """)

        for _ in range(50):
            if api_response:
                break
            await asyncio.sleep(0.1)

        await browser.close()

    return api_response
