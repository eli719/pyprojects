import scrapy
from scrapy01.items import Scrapy01Item


class JobPositionSpider(scrapy.Spider):
    name = 'job_position'
    allowed_domains = ['ygdy8.net']
    # 这里写上你要爬取的页面
    start_urls = ['https://www.ygdy8.net/html/gndy/china/index.html']

    # 爬取的方法
    def parse(self, response):
        # 注意在上面导入MoviespiderItem包
        item = Scrapy01Item()
        # 匹配
        for jobs_primary in response.xpath('//table[@class="tbspan"]'):
            item['name'] = jobs_primary.xpath('./tr/td/b/a[2]/text()').extract()
            item['uri'] = jobs_primary.xpath('./tr/td/b/a[2]/@href').extract()
            # 不能使用return
            yield item
