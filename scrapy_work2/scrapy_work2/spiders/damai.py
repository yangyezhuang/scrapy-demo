import scrapy
import json
from ..items import ScrapyDamaiItem


class DamaiSpider(scrapy.Spider):
    name = 'damai'
    allowed_domains = ['search.damai.cn']
    start_urls = [
        'https://search.damai.cn/searchajax.html?keyword=&cty=&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&sctl=&tsg=0&st=&et=&order=1&pageSize=30&currPage=1&tn=']

    def parse(self, response):
        item = ScrapyDamaiItem()
        dict = json.loads(response.text)
        list = dict.get('pageData').get('resultData')
        print(list)
        for li in list:
            name = li.get('name')
            city = li.get('cityname')
            location = li.get('venue')
            date = li.get('showtime')
            state = li.get('showstatus')
            actor = li.get('actors').split('：')[-1]
            low_price = li.get('price_str').split('-')[0]
            high_price = li.get('price_str').split('-')[-1]

            item['name'] = name
            item['city'] = city
            item['date'] = date
            item['actor'] = actor
            item['state'] = state
            item['location'] = location
            item['low_price'] = low_price
            item['high_price'] = high_price

            yield item

        for i in range(2, 11):
            url = f'https://search.damai.cn/searchajax.html?keyword=&cty=&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&sctl=&tsg=0&st=&et=&order=1&pageSize=30&currPage={str(i)}&tn='
            yield scrapy.Request(url, callback=self.parse)
