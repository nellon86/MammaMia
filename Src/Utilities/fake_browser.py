import json
from urllib.parse import urlparse

from pyppeteer import launch

chromium_path = "/usr/bin/chromium"


async def execute(api: str, more_headers: dict = None, get_json: bool = True):
    api_response = None

    parsed_url = urlparse(api)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

    browser = await launch(headless=True,
                           executablePath=chromium_path,
                           args=["--no-sandbox", '--disable-gpu', '--disable-dev-shm-usage'])
    page = await browser.newPage()

    await page.goto(base_url, waitUntil='domcontentloaded', timeout=0)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "Accept": "application/json" if get_json else "text/html",
        "Referer": f"{base_url}",
        "Origin": f"{base_url}"
    }
    if more_headers is not None:
        headers.update(more_headers)

    fetch_script = f"""
        () => {{
            return fetch("{api}", {{
                method: "GET",
                headers: {json.dumps(headers)}
            }})
            .then(response => {"response.json()" if get_json else "response.text()"})
        }}
    """

    try:
        api_response = await page.evaluate(fetch_script)
    except Exception as e:
        print(f"Fetch Error: {e}")
    finally:
        await browser.close()

    return api_response
