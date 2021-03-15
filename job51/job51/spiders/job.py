import scrapy
import json
import re
from ..items import Job51Item


class JobSpider(scrapy.Spider):
    name = 'job51'
    allowed_domains = ['search.51job.com']
    start_urls = [
        'https://search.51job.com/list/020000,000000,0000,32,0,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591,2,1.html?lang=c%27%27&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=']

    def parse(self, response):
        js = re.findall('window.__SEARCH_RESULT__ = (.*?)</script>', response.text, re.S)
        string = ''.join(js)
        d = json.loads(string)
        companies = d.get("engine_search_result")
        for company in companies:
            item = Job51Item()
            item['name'] = company.get('job_name')
            item['time'] = company.get('updatedate')
            item['salary'] = company.get('providesalary_text')
            item['company'] = company.get('company_name')
            item['area'] = company.get('workarea_text')
            info = company.get('attribute_text')
            item['exp'] = info[1]
            item['edu'] = info[2]
            item['number'] = info[-1]
            item['tags'] = company.get('jobwelf')

            yield item
