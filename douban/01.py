from bs4 import BeautifulSoup
import requests
import re
import sqlite3
import openpyxl

detail_url_pattern = r'<a href="(.*?)">'
img_url_pattern = r'<img.*src="(.*?)"'
title_pattern = r'<span class="title">(.*)</span>'
rating_pattern = r'<span class="rating_num" property="v:average">(.*)</span>'
viewer_pattern = r'<span>(\d*)人评价</span>'
idea_pattern = r'<span class="inq">(.*)</span>'
about_pattern = r'<p class="">(.*?)</p>'


def get_one_page(bul):
    datalist = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.88 Safari/537.36'}
    for i in range(0, 10):
        page = i * 25
        url = bul + str(page)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # print(response.content.decode('utf-8'))
            soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
            for item in soup.find_all('div', class_='item'):
                # print(item)
                item = str(item)
                data = []
                detail_url = re.findall(re.compile(detail_url_pattern), item)[0]
                data.append(detail_url)
                img_url = re.findall(re.compile(img_url_pattern, re.S), item)[0]
                data.append(img_url)
                title = re.findall(re.compile(title_pattern), item)
                if len(title) == 2:
                    ctitle = title[0]
                    data.append(ctitle)
                    etitle = title[1].replace("/", "")
                    data.append(etitle)
                else:
                    data.append(title[0])
                    data.append(" ")
                rating = re.findall(re.compile(rating_pattern), item)[0]
                data.append(rating)
                viewer = re.findall(re.compile(viewer_pattern), item)[0]
                data.append(viewer)
                try:
                    idea = re.findall(re.compile(idea_pattern), item)[0]
                    data.append(idea)
                except Exception:
                    data.append(" ")

                about = re.findall(re.compile(about_pattern, re.S), item)[0]
                about = re.sub(r'<br(\s+)?/>(\s+)?', "", about)
                about = re.sub("/", "", about)
                data.append(about.strip())
                datalist.append(data)
    return datalist


def save_data(data, path):
    book = openpyxl.Workbook()
    sheet = book.create_sheet('豆瓣电影Top')
    title = ['电影详情', '图片链接', '影片中文名', '影片英文名', '评分', '评分人数', '概括', '相关']
    sheet.append(title)
    for i in data:
        sheet.append(i)
    book.save(path)
    return None


def init_db():
    conn = sqlite3.connect('movies.db')
    print('create successfully')
    c = conn.cursor()
    sql = '''
        create table movies 
            (id integer primary key autoincrement,
            info_link text,
            pic_link text,
            cname varchar,
            ename varchar,
            score numeric,
            rated numeric,
            instruction text,
            info text)
    '''
    c.execute(sql)
    conn.commit()
    conn.close()


def save_to_DB(datalist):
    init_db()
    conn = sqlite3.connect('movies.db')
    print('open successfully')
    c = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 5 or index == 4:
                continue
            data[index] = '"' + data[index] + '"'
        sql = '''insert into movies (
                        info_link,
                        pic_link,
                        cname,
                        ename,
                        score,
                        rated,
                        instruction,
                        info)values(%s)'''%",".join(data)
        c.execute(sql)
        conn.commit()
    c.close()
    conn.close()


if __name__ == '__main__':
    baseurl = "https://movie.douban.com/top250?start="
    da = get_one_page(baseurl)
    # path = '豆瓣电影Top250.xls'
    # save_data(da,path)
    save_to_DB(da)
