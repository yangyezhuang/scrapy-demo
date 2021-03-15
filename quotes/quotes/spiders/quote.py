import scrapy
from ..items import QuotesItem


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        print(response.request.headers['User-Agent'])  # 打印随机请求头
        lists = response.xpath('//div[@class="col-md-8"]/div[@class="quote"]')
        for li in lists:
            item = QuotesItem()
            item['sentence'] = li.xpath('.//span[1]/text()').extract_first()
            item['author'] = li.xpath('.//span[2]/small/text()').extract_first()
            item['tags'] = li.xpath('.//div[@class="tags"]/a/text()').extract()

            yield item

        next_page = response.xpath('.//li[@class="next"]/a/@href').extract_first()
        if next_page:
            next_url = 'http://quotes.toscrape.com' + next_page
            yield scrapy.Request(next_url, callback=self.parse, dont_filter=True)
