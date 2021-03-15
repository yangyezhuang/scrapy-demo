import scrapy


class JingdongSpider(scrapy.Spider):
    name = 'jingdong'
    allowed_domains = ['search.jd.com']
    start_urls = ['http://search.jd.com/']

    def parse(self, response):
        pass
