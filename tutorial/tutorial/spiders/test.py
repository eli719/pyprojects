import scrapy

from tutorial.items import TutorialItem


class test_spider(scrapy.Spider):
    name = 'test'
    start_urls = ['http://220.163.129.204:7788']

    # def start_requests(self):

    def parse(self, response):
        data = {
            'params': "{\"type\":\"read\",\"userid\":\"''\",\"commandcode\":\"Ruser\",\"returndata\":0,\"inparameters\":{\"userid\":\"''\",\"username\":\"'西安杨森'\",\"pwd\":\"'81dc9bdb52d04dc20036dbd8313ed055'\"}}"
        }
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
        }

        scrapy.FormRequest(url='http://220.163.129.204:7788/Service', formdata=data, callback=self.parse_item)

        params = [
            "{\"type\":\"read\",\"userid\":\"'U34GUIVTXT6'\",\"commandcode\":\"Gspkc\",\"returndata\":0,\"inparameters\":{\"userid\":\"'U34GUIVTXT6'\",\"entid\":\"'E31NG51MEJO'\",\"orgid\":\"'O31NG51M9J4'\",\"spid\":\"''\"}}"
            ,
            "{\"type\":\"read\",\"userid\":\"'U34GUIVTXT6'\",\"commandcode\":\"Gxslx\",\"returndata\":0,\"inparameters\":{\"start_rq\":\"'2020-07-01'\",\"end_rq\":\"'2020-08-05'\",\"userid\":\"'U34GUIVTXT6'\",\"entid\":\"'E31NG51MEJO'\",\"orgid\":\"'O31NG51M9J4'\",\"spid\":\"''\",\"pihao\":\"''\",\"billcode\":\"''\",\"fapiaoh\":\"''\",\"shpchd\":\"''\",\"djlx\":\"'all'\"}}"
            ,
            "{\"type\":\"read\",\"userid\":\"'U34GUIVTXT6'\",\"commandcode\":\"Gcglx\",\"returndata\":0,\"inparameters\":{\"start_rq\":\"'2020-07-01'\",\"end_rq\":\"'2020-08-05'\",\"userid\":\"'U34GUIVTXT6'\",\"entid\":\"'E31NG51MEJO'\",\"orgid\":\"'O31NG51M9J4'\",\"spid\":\"''\",\"pihao\":\"''\",\"billcode\":\"''\",\"fapiaoh\":\"''\",\"shpchd\":\"''\",\"djlx\":\"'all'\"}}"
        ]
        for i in params:
            print(params.index(i))
            yield scrapy.FormRequest(url='http://220.163.129.204:7788/Service', formdata={'params': i}, dont_filter=True,
                                     callback=lambda response, it=1: self.parse_item(response, params.index(i)))

    def parse_item(self, response, i):
        # print(i)
        item = TutorialItem()
        if i == 0:
            item['stock'] = response.json()
        elif i == 1:
            item['sale'] = response.json()
        else:
            item['purchase'] = response.json()
        yield item
