import scrapy
from ..items import DoubanbookItem


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250']

    def parse(self, response):
        print(response.request.headers['User-Agent'])# 打印随机请求头
        lists = response.xpath('//div[@class="indent"]/table')
        for li in lists:
            item = DoubanbookItem()
            item['name'] = li.xpath('.//div[@class="pl2"]/a/@title').extract_first()
            item['score'] = li.xpath('.//span[@class="rating_nums"]/text()').extract_first()
            item['comment'] = li.xpath('.//span[@class="pl"]/text()').extract_first().replace('(', '').replace(')','').replace(' ', '').strip('\n')
            item['title'] = li.xpath('.//span[@class="inq"]/text()').extract_first()
            info = li.xpath('.//p[@class="pl"]/text()').extract_first().split('/ ')
            if len(info) == 5:
                item['translate'] = info[0]
                item['author'] = info[1]
            else:
                item['author'] = info[0]
            item['price'] = info[-1].replace('元','')
            item['store'] = info[-3]
            item['data'] = info[-2]

            yield item

        next_page = response.xpath('//span[@class="next"]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse, dont_filter=True)
