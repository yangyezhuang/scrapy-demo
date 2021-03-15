import scrapy
from scrapy import Request
from ..items import DoubanItem
from ..settings import DEFAULT_COOKIE


class MovieSpider(scrapy.Spider):
    name = 'movie1'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        '''
        解析列表页
        :param response:
        :return:
        '''
        lists = response.xpath('//div[@class="article"]/ol[@class="grid_view"]/li')
        for li in lists:
            item = DoubanItem()
            item['name'] = li.xpath('.//div[@class="hd"]/a/span/text()').extract_first()
            item['title'] = li.xpath('.//div[@class="bd"]/p[@class="quote"]/span/text()').extract_first().replace('。','')
            info_url = li.xpath('.//div[@class="hd"]/a/@href').extract_first()

            yield Request(url=info_url, callback=self.info_parse, meta={'item': item}, dont_filter=True,cookies=DEFAULT_COOKIE)

        # 获取下一页url
        next_page = response.xpath('//div[@class="paginator"]/span[3]/a/@href').extract()
        if next_page:
            next_page = next_page[0]
            url = self.start_urls[0] + next_page
            yield scrapy.Request(url, callback=self.parse)

    def info_parse(self, response):
        '''
        解析详情页
        :param response:
        :return:
        '''
        item = response.meta['item']
        item['comment'] = response.xpath('//span[@property="v:votes"]/text()').extract_first()
        item['score'] = response.xpath('//strong[@class="ll rating_num"]/text()').extract_first()
        item['time'] = response.xpath('//span[@property="v:runtime"]/text()').extract_first()
        item['daoyan'] = response.xpath('//span[@class="attrs"]/a/text()').extract_first()
        yield item
