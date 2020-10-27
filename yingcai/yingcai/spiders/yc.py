import scrapy
from scrapy import Request
from ..items import YingcaiItem


class JobSpider(scrapy.Spider):
    name = 'yc'
    allowed_domains = ['search.chinahr.com']
    start_urls = 'https://search.chinahr.com/su/job/pn{page}/?key=php'

    def start_requests(self):
        """
        生成初始请求
        :return: 初始请求
        """
        # 请求列表页的第1页
        page = 1
        yield Request(url=self.start_urls.format(page=page), callback=self.parse, meta={'page': page})


    def parse(self, response):
        '''
        解析列表信息
        '''
        lists = response.xpath('//div[@class="job-list-box"]/div[@class="jobList pc_search_listclick"]')
        for li in lists:
            item = YingcaiItem()
            item['job_url'] = li.xpath('./@data-detail').extract_first().strip()
            item['job_name'] = li.xpath('.//li[@class="job-name"]/text()').extract_first().strip()
            item['job_salary'] = li.xpath('.//li[@class="job-salary"]/text()').extract_first().strip()
            item['company_name'] = li.xpath('.//li[@class="job-company"]/text()').extract_first().strip()
            # item['job_exp_require'] = li.xpath('.//li[@class="job-address"]/text()').extract().strip()
            item['job_info'] = li.xpath('./p[@class="l3"]/text()').extract_first().strip()
            yield item


        # 翻页
        page = response.meta['page'] + 1
        yield Request(url=self.start_urls.format(page=page), callback=self.parse, meta={'page': page})

