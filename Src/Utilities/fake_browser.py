import glob
import json
import os
import stat
import subprocess
from urllib.parse import urlparse

from pyppeteer import launch

#chromium_path = os.path.join(os.getcwd(), "browser", "chrome")
chromium_path = "/usr/bin/chromium"

'''
def unzip():
    extract_path = os.path.join(os.getcwd(), "browser")
    if not os.path.exists(os.path.join(extract_path, "chrome")):
        print("Unzip browser")

        zip_prefix = os.path.join(extract_path, "chromium.zip.")
        parts = glob.glob(zip_prefix + '*')
        n = len(parts)

        temp_zip_name = os.path.join(extract_path, "chromium.zip")
        with open(temp_zip_name, "wb") as outfile:
            for i in range(1, n + 1):
                filename = zip_prefix + str(i).zfill(3)
                with open(filename, "rb") as infile:
                    outfile.write(infile.read())

        with zipfile.ZipFile(temp_zip_name, "r") as zip_ref:
            zip_ref.extractall(extract_path)

        os.remove(temp_zip_name)

    print("Browser ready")
'''


def unzip():
    extract_path = os.path.join(os.getcwd(), "browser")
    if not os.path.exists(os.path.join(extract_path, "chrome")):
        print("Unzip browser")

        zip_prefix = os.path.join(extract_path, "chromium.zip.")
        parts = glob.glob(zip_prefix + '*')
        n = len(parts)

        temp_zip_name = os.path.join(extract_path, "chromium.zip")
        with open(temp_zip_name, "wb") as outfile:
            for i in range(1, n + 1):
                filename = zip_prefix + str(i).zfill(3)
                with open(filename, "rb") as infile:
                    outfile.write(infile.read())

        subprocess.run(
            ["unzip", "-o", temp_zip_name, "-d", extract_path],
            check=True,
            text=True,
            capture_output=True
        )

        os.remove(temp_zip_name)

        make_executable(chromium_path)

    print("Browser ready")


def make_executable(path):
    st = os.stat(path)
    os.chmod(path, st.st_mode | stat.S_IEXEC)


async def execute(api: str, more_headers: dict = None, get_json: bool = True):
    api_response = None

    parsed_url = urlparse(api)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

    browser = await launch(headless=True, executablePath=chromium_path,
                           args=["--no-sandbox", '--disable-gpu'],
                           dumpio=True)
    page = await browser.newPage()

    await page.goto(base_url)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "Accept": "application/json" if get_json else "text/html",
        "Referer": f"{base_url}",
        "Origin": f"{base_url}"
    }
    print(f"HEADERSSSSS ================== {headers}")
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
