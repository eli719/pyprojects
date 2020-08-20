import asyncio
from pyppeteer import launch


async def main():
    width = 1366
    height = 768
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.setViewport(viewport={"width": width, "height": height})
    await page.goto('http://hep.heliteq.com/irj/portal', timeout=10000)
    await page.setJavaScriptEnabled(enabled=True)
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 6.1; WOW64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/68.0.3440.106 Safari/537.36')
    await asyncio.sleep(3)
    await page.waitForSelector('#logonuidfield')
    await page.type('#logonuidfield', 'G_janssen_01')
    await page.type('#logonpassfield', '19881101')
    await page.click('.urBtnStd')
    await asyncio.sleep(5)
    frame = page.frames[0]
    print(frame)
    print(frame.childFrames)
    f1 = frame.childFrames[0]
    f2 = frame.childFrames[1]
    f3 = frame.childFrames[2]
    print('f1:', f1.childFrames)
    print('f2:', f2.childFrames)
    print('f3:', f3.childFrames)
    f11 = []
    f12 = []
    if len(f1.childFrames)>0:
        f11 = f1.childFrames[0]
        f12 = f1.childFrames[1]
    elif len(f2.childFrames)>0:
        f11 = f2.childFrames[0]
        f12 = f2.childFrames[1]
    elif len(f3.childFrames)>0:
        f11 = f3.childFrames[0]
        f12 = f3.childFrames[1]

    f111 = []
    f222 = []
    f333 = []
    f444 = []
    if len(f11.childFrames) > 0:
        f111 = f11.childFrames[0]
        f222 = f11.childFrames[1]
        f333 = f11.childFrames[2]
        f444 = f11.childFrames[3]
    elif len(f12.childFrames) > 0:
        f111 = f12.childFrames[0]
        f222 = f12.childFrames[1]
        f333 = f12.childFrames[2]
        f444 = f12.childFrames[3]

    print('f111:', f111)
    print('f222:', f222)
    print('f333:', f333)
    print('f444:', f444)
    print('f1111', f111.childFrames)
    print('f2222', f222.childFrames)
    print('f3333', f333.childFrames)
    print('f4444', f444.childFrames)

    f01=[]
    f02=[]
    if len(f111.childFrames)>0:
        f01 = f111.childFrames[0]
        f02 = f111.childFrames[1]
    elif len(f222.childFrames)>0:
        f01 = f222.childFrames[0]
        f02 = f222.childFrames[1]
    elif len(f333.childFrames)>0:
        f01 = f333.childFrames[0]
        f02 = f333.childFrames[1]
    elif len(f444.childFrames)>0:
        f01 = f444.childFrames[0]
        f02 = f444.childFrames[1]

    print('f01:', f01.childFrames)
    print('f02:', f02.childFrames)

    await f02.querySelector('#WD34-menu')
    await f02.click('#WD34-menu')
    await f02.click('#WD34')
    await asyncio.sleep(3)
asyncio.get_event_loop().run_until_complete(main())