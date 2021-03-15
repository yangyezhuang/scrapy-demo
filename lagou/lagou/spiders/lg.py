import scrapy
import json
from scrapy.http import FormRequest


class LgSpider(scrapy.Spider):
    name = 'lg'
    allowed_domains = ['lagou.com']
    key_word = 'python'
    start_urls = f'https://www.lagou.com/jobs/list_{key_word}'


    def start_requests(self):
        for i in range(3):
            from_data={'pn':f'{i}'}
            request = FormRequest(self.start_urls,formdata=from_data,callback=self.parse_list)
            yield request


    def parse_list(self, response):
        pass
        

