import scrapy

from ..settings import DEFAULT_COOKIE
from ..items import ScrapySinaItem


class SinaNewsSpider(scrapy.Spider):
    name = 'sina_news'
    # allowed_domains = ['sina.com.cn']
    start_urls = ['http://sina.com.cn/']

    def parse(self, response):
        urls = response.xpath('//div[@id="syncad_0"]//li/a[1]/@href').extract()
        for url in urls:
            item = ScrapySinaItem()
            if 'sina.com.cn' in url:
                yield scrapy.Request(url=url, callback=self.pare_info, meta={'item': item}, dont_filter=True,
                                     cookies=DEFAULT_COOKIE)

    def pare_info(self, response):
        item = response.meta['item']
        item['url'] = response.url
        item['title'] = response.xpath('//h1[@class="main-title"]/text()').extract_first()
        item['content'] = response.xpath('//div[@class="article"]/p[2]/text()').extract_first().strip()
        yield item
