from urllib.parse import urlparse

from playwright.async_api import async_playwright

chromium_path = "/usr/bin/chromium"

playwright = None
browser = None


async def setup_browser():
    global playwright, browser
    if not playwright:
        playwright = await async_playwright().start()
    if not browser:
        browser = await playwright.chromium.launch(headless=True,
                                                   executable_path=chromium_path,
                                                   args=["--no-sandbox", '--disable-gpu', '--disable-dev-shm-usage'])


async def close():
    global browser, playwright
    if browser:
        await browser.close()
        browser = None
    if playwright:
        await playwright.stop()
        playwright = None

async def execute(api: str, more_headers: dict = None, get_json: bool = True):
    global browser
    await setup_browser()

    context = await browser.new_context()
    await context.new_page()

    parsed_url = urlparse(api)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "Accept": "application/json" if get_json else "text/html",
        "Referer": f"{base_url}",
        "Origin": f"{base_url}"
    }
    if more_headers is not None:
        headers.update(more_headers)

    api_response = await context.request.get(api, headers=headers)
    if api_response.ok:
        return await api_response.json() if get_json else await api_response.text()

    return None
