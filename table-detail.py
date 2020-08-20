import time
import asyncio


async def main(browser,url):
    width = 1366
    height = 768
    page = await browser.newPage()
    await page.setViewport(viewport={"width": width, "height": height})
    await page.setJavaScriptEnabled(enabled=True)
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
    await page.goto(url)
    await asyncio.sleep(3)
    rows = await page.querySelectorAll('.row')
    for row in rows:
        divs = await row.querySelectorAll('div')
        for div in divs:
            text = await (await div.getProperty('textContent')).jsonValue()
            print(text)
    await asyncio.sleep(5)