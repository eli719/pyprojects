import asyncio
from pyppeteer import launch


async def main( ):
    width = 1366
    height = 768
    browser = await launch(headless=False, args=['--disable-infobars'])
    page = await browser.newPage()
    await page.setViewport(viewport={"width": width, "height": height})
    await page.setJavaScriptEnabled(enabled=True)
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
    await page.goto('https://www.cods.org.cn/')

    await asyncio.sleep(3)

asyncio.get_event_loop().run_until_complete(main())