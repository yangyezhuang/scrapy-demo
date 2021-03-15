import scrapy
from ..items import ScrapySunItem


class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']

    def parse(self, response):
        lists = response.xpath('//li[@class="clear"]')
        for li in lists:
            item = ScrapySunItem()
            num = li.xpath('.//span[1]/text()').extract_first()
            state = li.xpath('.//span[2]/text()').extract_first()
            title = li.xpath('.//span[3]//a/text()').extract_first()
            response_time = li.xpath('.//span[4]/text()').extract_first()
            question_time = li.xpath('.//span[5]/text()').extract_first()

            item['num'] = num
            item['state'] = state.replace('\n', '').strip(' ')
            item['title'] = title
            item['response_time'] = response_time.replace('\n', '').strip(' ').split('：')[-1]
            item['question_time'] = question_time
            yield item

        for i in range(2, 11):
            next_url = f'http://wz.sun0769.com/political/index/politicsNewest?id=1&page={str(i)}'
            yield scrapy.Request(next_url, callback=self.parse)
