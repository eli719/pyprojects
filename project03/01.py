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
    await asyncio.sleep(1)
    await page.type('#checkContent_index', '苏州力信通')
    await asyncio.sleep(1)
    await page.click('#checkBtn')
    await page.waitFor(10 * 1000)
    v = await page.querySelector(
        'body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_no_logo.geetest_panelshowslide > div.geetest_panel_next > div > div.geetest_wrap > div.geetest_widget > div > a > div.geetest_canvas_img.geetest_absolute > div > canvas.geetest_canvas_bg.geetest_absolute')
    await page.evaluate(pageFunction="document.getElementsByTagName('canvas')[0].setAttribute('style','display:none')")
    # verify_image = await page.waitForXPath('/html/body/div[3]/div[2]/div[6]/div/div[1]/div[1]/div/a/div[1]')
    verify_image = await page.waitForSelector('body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_no_logo.geetest_panelshowslide > div.geetest_panel_next > div > div.geetest_wrap > div.geetest_widget > div')  # 通过css selector定位验证码元素
    await verify_image.screenshot({'path': 'verify_image.jpg'})
    await page.evaluate(pageFunction="document.getElementsByTagName('canvas')[0].removeAttribute('style','display:none')")
    await page.evaluate(pageFunction="document.getElementsByTagName('canvas')[1].setAttribute('style','display:none')")
    verify_image = await page.waitForSelector(
        'body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_no_logo.geetest_panelshowslide > div.geetest_panel_next > div > div.geetest_wrap > div.geetest_widget > div')  # 通过css selector定位验证码元素
    await verify_image.screenshot({'path': 'verify_image1.jpg'})

    await page.evaluate(pageFunction="document.getElementsByTagName('canvas')[2].setAttribute('style','display:block')")
    verify_image = await page.waitForSelector(
        'body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_no_logo.geetest_panelshowslide > div.geetest_panel_next > div > div.geetest_wrap > div.geetest_widget > div')  # 通过css selector定位验证码元素
    await verify_image.screenshot({'path': 'verify_image2.jpg'})
    slide = await page.querySelector('.geetest_slider_button')
    size = await slide.boundingBox()
    await page.mouse.move(size.get('x'),size.get('y'))
    await page.mouse.down()
    await page.mouse.move(size.get('x')+50,size.get('y'),{'steps':30})
    await page.waitFor(300)

    await asyncio.sleep(2)
asyncio.get_event_loop().run_until_complete(main())