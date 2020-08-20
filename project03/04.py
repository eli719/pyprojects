import asyncio
import random
from pyppeteer import launch

def input_time_random():
    return random.randint(100, 151)

width, height = 1366, 768
async def main():
    browser = await launch({'headless':False})
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.evaluateOnNewDocument(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await page.evaluateOnNewDocument('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    await page.evaluateOnNewDocument('''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    await page.evaluateOnNewDocument('''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')

    await page.goto('https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/')
    await page.waitFor(4 * 1000)
    # await page.click('#J_QRCodeLogin > div.login-links > a.forget-pwd.J_Quick2Static')
    await page.waitFor(3 * 1000)
    await page.type('#fm-login-id', '123123', {'delay': input_time_random() - 50})
    await page.type('#fm-login-password', '232322332', {'delay': input_time_random()})
    await page.waitFor(2 * 1000)
    el = await page.querySelector('#nc_1_n1z')
    box = await el.boundingBox()
    await page.hover('#nc_1_n1z')
    await page.mouse.down()
    await page.mouse.move(box['x']+1000,box['y'], {'delay': random.randint(1000, 2000),'steps':3})
    await page.mouse.up()
    await page.waitFor(5 * 1000)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())