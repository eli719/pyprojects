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
    await page.goto('http://www.nmpa.gov.cn/WS04/CL2042/')

    await page.goto('http://app1.nmpa.gov.cn/datasearchcnda/face3/base.jsp?tableId=34&tableName=TABLE34&title=%E8%8D%AF%E5%93%81%E7%94%9F%E4%BA%A7%E4%BC%81%E4%B8%9A&bcId=152911762991938722993241728138')
    await asyncio.sleep(3)

asyncio.get_event_loop().run_until_complete(main())