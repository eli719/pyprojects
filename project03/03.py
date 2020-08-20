import asyncio
from pyppeteer import launch


async def main( ):
    width = 1366
    height = 768
    # proxy = '116.71.132.53:8080	'
    # browser = await launch(headless=False, args=['--disable-infobars', '--enable-automation','--proxy-server={}'.format(proxy)])
    browser = await launch(headless=False, args=['--disable-infobars'])
    page = await browser.newPage()
    await page.setViewport(viewport={"width": width, "height": height})
    await page.setJavaScriptEnabled(enabled=True)
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3477.0 Safari/537.36')
    # await page.evaluateOnNewDocument('''() => {
    #             Object.defineProperty(navigator, 'webdriver', {
    #             get: () => undefined
    #             })
    #             }
    #         ''')
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => undefined } }) }''')
    await page.evaluate('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')
    await page.goto('https://www.cods.org.cn/')
    await page.type('#checkContent_index', '苏州力信通')
    await asyncio.sleep(1)
    await page.click('#checkBtn')
    await page.waitForNavigation({'timeout': 1000 * 30})
    slide = await page.querySelector('.geetest_slider_button')
    if slide is None :
        await page.reload()
    slide = await page.querySelector('.geetest_slider_button')
    size = await slide.boundingBox()
    print(size.get('x'),size.get('y'))
    x = size.get('x').__float__()
    y = size.get('y').__float__()
    await page.mouse.move(x, y)
    await page.mouse.down()
    await page.waitFor(200);
    await page.mouse.move(x+5, y, {'steps': 20})
    await page.mouse.up()
    await page.waitFor(300)

    await asyncio.sleep(2)
asyncio.get_event_loop().run_until_complete(main())