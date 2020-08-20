import asyncio
from pyppeteer import launch


async def main():
    width = 1366
    height = 768
    browser = await launch(headless=False,args=['--disable-infobars'])
    page = await browser.newPage()
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36')
    await page.setViewport(viewport={"width": width, "height": height})
    await page.setJavaScriptEnabled(enabled=True)
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => undefined } }) }''')
    await page.evaluate('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')
    await page.goto('http://220.163.129.204:7788/#/login', timeout=10000000)


    await asyncio.sleep(3)
    await page.waitForSelector('#logonuidfield')
    await page.type('#app > div:nth-child(2) > form > div:nth-child(2) > div > div > input', '西安杨森')
    await page.type('#app > div:nth-child(2) > form > div:nth-child(3) > div > div > input', '1234')
    await page.click('#app > div:nth-child(2) > form > div:nth-child(5) > div > button')
    await asyncio.sleep(3)

asyncio.get_event_loop().run_until_complete(main())