import time
import asyncio
from pyppeteer import launch
import image6


async def detail(browser, url):
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


async def main():
    width = 1366
    height = 768
    browser = await launch(headless=False, userDataDir='userdata', args=['--disable-infobars'])
    page = await browser.newPage()
    await page.setViewport(viewport={"width": width, "height": height})
    await page.setJavaScriptEnabled(enabled=True)
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
    await page.goto('http://54.223.83.26:8080/cahweb/JSP/Console.jsp')
    table = await page.J('#sampleTableA > thead')
    thead = await table.querySelectorAll('thead > tr:nth-child(1) > td')
    for td in thead:
        # print(await td.getProperty('textContent'))
        text = await (await td.getProperty('textContent')).jsonValue()
        print(text)

    # sampleTableA > tbody > tr:nth-child(1)
    trs = await page.querySelectorAll('#sampleTableA > tbody > tr')
    for td in trs:
        # print(await td.getProperty('textContent'))
        text = await (await td.getProperty('textContent')).jsonValue()
        s = str(text).replace('\n\t\t\t\t\t\t\t', '')
        print(s)

    await detail(browser, '')
    await asyncio.sleep(5)


asyncio.get_event_loop().run_until_complete(main())
