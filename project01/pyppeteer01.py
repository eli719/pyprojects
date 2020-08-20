import asyncio
from pyppeteer import launch
import entire_recognize as er
import excel_util_write as ew
import recognize_code as rc
import excel_util_read as eur


async def main(province_name, institution_name):
    width = 1366
    height = 768
    browser = await launch(headless=False, args=['--disable-infobars'])
    page = await browser.newPage()
    await page.setViewport(viewport={"width": width, "height": height})
    await page.setJavaScriptEnabled(enabled=True)
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
    await page.goto('http://zgcx.nhc.gov.cn:9090/unit/index')
    await asyncio.sleep(3)
    options = await page.querySelectorAll('#Prov option')
    select_dic = {}
    for option in options[1:]:
        option_id = await (await option.getProperty('value')).jsonValue()
        province = await (await option.getProperty('textContent')).jsonValue()
        select_dic.update({option_id: province})

    input_key = ''
    for key, value in select_dic.items():
        if province_name == value:
            input_key = key
    await page.select('#Prov', input_key)
    await page.type('#Unit_Name', institution_name)
    result = await recognize_code(page)
    print(result)
    # if result is False or result is None:
    #     await page.close()
    #     await browser.close()
    #     await asyncio.sleep(5)
    #     return
    table = await page.querySelector('.table-bordered')
    if table is None:
        await page.close()
        await browser.close()
        await asyncio.sleep(5)
        return
    rows_data = []
    titles = await table.querySelectorAll('.ext-table-th')
    title_head = []
    for title in titles:
        text = await (await title.getProperty('textContent')).jsonValue()
        title_head.append(text)
    # rows_data.append(title_head)
    rows = await table.querySelectorAll('tbody tr')
    for row in rows:
        tds = await row.querySelectorAll('td')
        row_data = []
        for i in range(len(tds)):
            td = tds[i]
            cell = await (await td.getProperty('textContent')).jsonValue()
            if i == len(tds)-1:
                a = await td.querySelector('a')
                href = await (await a.getProperty('href')).jsonValue()
                row_data.append(href)
                detail_page = await browser.newPage()
                await detail_page.goto(href.__str__())
                detail_table = await detail_page.querySelector('.details_co')
                detail_rows = await detail_table.querySelectorAll('.row')
                dic = {}
                for detail_row in detail_rows:
                    line_divs = await detail_row.querySelectorAll('div')
                    left = await (await line_divs[0].getProperty('textContent')).jsonValue()
                    right = await (await line_divs[1].getProperty('textContent')).jsonValue()
                    right = ''.join(right.__str__().split())
                    dic.update({left.__str__().replace('：', ''): right})
                    # print(dic)
                if len(title_head) <= 5:
                    for (key, value) in dic.items():
                        # print(key in title_head)
                        if key not in title_head:
                            title_head.append(key)
                    rows_data.append(title_head)
                for (key, value) in dic.items():
                    for index in range(5, len(title_head)):
                        if title_head[index].__eq__(key):
                            row_data.insert(index, value)
                await detail_page.close()
            else:
                row_data.append(cell)
        # if title_head not in rows_data:
        #     rows_data.index(title_head, 0, 1)
        rows_data .append(row_data)
        # await page.goBack()

    title_head = {'ID': 'id', 'PROVINCENAME': '省份', 'KEYWORD': '查询关键字', 'ORGNAME': '医疗机构名称', 'ADDRESSLINE': '地址',
                  'APPROVERNAME': '审批机关', 'REGISTRATIONNO': '登记号', 'SPECIALTYPRACTICE': '诊疗科目', 'LEVELNAME': '级别',
                  'LEGALPERSON': '法人', 'CORPORATION': '负责人', 'LICENCEPERIOD': '执业许可证有效期', 'DETAILHREF': '详细',
                  'SEARCHBATCHNO': '查询批次', 'CREATEDATE': '创建日期', 'IMPFLAG': '是否已加入行业库'}
    head = rows_data[0]
    for i in range(len(head)):
        for key, value in title_head.items():
            if head[i].__eq__(value):
                head[i] = key
    ew.WriteExcel('excel01.xlsx', rows_data[1:]).write_data_line()

    await page.close()
    await browser.close()


async def recognize_code(page):
    verify_image = await page.waitForSelector('#imgCaptcha')  # 通过css selector定位验证码元素
    await verify_image.screenshot({'path': 'verify_image.jpg'})
    er.single()
    # change_to_1.changFormat('1')
    # crop_image.crop_img()
    # del_noise.main()
    verify_code = rc.get_code()
    # verify_code = image6.OCR_lmj('verify_image.png')
    if len(verify_code) == 4:
        await page.type('#Check_Code', verify_code)
        await page.waitFor(1000)
        await page.click(
            "body > div > div:nth-child(2) > form > div > div.col-lg-7.col-md-7.col-sm-6 > div:nth-child(4) "
            "> div > button")
        await asyncio.sleep(2)
        error = await page.querySelector('.validation-summary-errors')
        if error is not None:
            # print(error)
            page_content = (await page.content()).__str__()
            if page_content.__contains__('请输入更加精确的医疗机构名称'):
                print(1)
                return False
            await page.evaluate('document.querySelector("#Check_Code").value=""')
            await recognize_code(page)
        else:
            print(2)
            # print(await page.content())
            page_content = (await page.content()).__str__()
            if page_content.__contains__('未查询到符合条件的医疗机构'):
                return False
            else:
                return True
    else:
        print(3)
        await page.click('.a')
        await recognize_code(page)




title_head = {'ID': 'id', 'PROVINCENAME': '省份', 'KEYWORD': '查询关键字', 'ORGNAME': '医疗机构名称', 'ADDRESSLINE': '地址',
                  'APPROVERNAME': '审批机关', 'REGISTRATIONNO': '登记号', 'SPECIALTYPRACTICE': '诊疗科目', 'LEVELNAME': '级别',
                  'LEGALPERSON': '法人', 'CORPORATION': '负责人', 'LICENCEPERIOD': '执业许可证有效期', 'DETAILHREF': '详细',
                  'SEARCHBATCHNO': '查询批次', 'CREATEDATE': '创建日期', 'IMPFLAG': '是否已加入行业库'}

title = [[]]
for value in title_head.values():
    title[0].append(value)
ew.WriteExcel('excel01.xlsx', title).write_data_line()
r = eur.ReadExcel('../02.xlsx')
data1 = r.read_data_line()
for row in data1[1:]:
    province_name = row[0]
    institution_name = row[1]
    if len(institution_name) < 4:
        continue
    print(province_name,institution_name)
    asyncio.get_event_loop().run_until_complete(main(province_name, institution_name))
# province_name = '四川省'
# institution_name = '儿童医院'
# asyncio.get_event_loop().run_until_complete(main(province_name, institution_name))