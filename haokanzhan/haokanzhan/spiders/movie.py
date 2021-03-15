import scrapy
from scrapy import Request
from ..items import HaokanzhanItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.haokan95.com']
    start_urls = ['https://www.haokan95.com/dy.html']

    def parse(self, response):
        '''
        解析列表页
        :param response:
        :return:
        '''
        lists = response.xpath('//div[@class="ui-cnt"]/ul/li')
        for li in lists:
            item = HaokanzhanItem()
            li_url = li.xpath('./a/@href')
            url = 'https://www.haokan95.com' + li_url
            item['url'] = url

            yield Request(url=li_url, callback=self.parse_info, meta={'item': item}, dont_filter=True)

        # 判断并获取下一页
        next_page = response.xpath('//div[@class="ui-pages"]/a[-2]/href')
        if next_page:
            next_url = 'https://www.haokan95.com' + next_page
            yield scrapy.Request(next_url, callback=self.parse)


    def parse_info(self, response):
        '''
        解析详情页
        :param response:
        :return:
        '''
        item = response.meta['item']
        item['name'] = response.xpath('')
        item['year'] = response.xpath('')
        item['type'] = response.xpath('')
        item['area'] = response.xpath('')
        item['language'] = response.xpath('')
        yield item
