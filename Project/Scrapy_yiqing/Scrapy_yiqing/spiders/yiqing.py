import scrapy
from ..items import ScrapyYiqingItem


class YiqingSpider(scrapy.Spider):
    name = 'yiqing'
    allowed_domains = ['m.sinovision.net']
    start_urls = ['http://m.sinovision.net/newpneumonia.php']

    def parse(self, response):
        lists = response.xpath('/html/body/div[2]/div[13]/div')
        '/html/body/div[2]/div[13]'
        item = ScrapyYiqingItem()
        for li in lists:
            item['地区'] = li.xpath('.//span[1]/text()').extract_first()
            # item['新增'] = li.xpath('./td[2]/text()').extract_first()
            # item['现有'] = li.xpath('./td[3]/text()').extract_first()
            item['累计'] = li.xpath('.//span[2]/text()').extract_first()
            item['死亡'] = li.xpath('.//span[3]/text()').extract_first()
            item['治愈'] = li.xpath('.//span[4]/text()').extract_first()

            print(item)
            yield item
