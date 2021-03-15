import scrapy
from scrapy import Request
from urllib.parse import quote
from ..items import LiepinItem


class JobSpider(scrapy.Spider):
    name = 'lp'
    allowed_domains = ['www.liepin.com']
    max_page = 3
    keyword = quote('java')
    start_urls = 'https://www.liepin.com/zhaopin/?&key={keyword}&curPage={page}'

    def start_requests(self):
        """
        生成初始请求
        :return: 初始请求第1页
        """
        page = 0
        yield Request(url=self.start_urls.format(keyword=self.keyword, page=page), callback=self.parse,
                      meta={'page': page})


    def parse(self, response):
        '''
        列表页
        :param response:
        :return:
        '''
        lists = response.xpath('//ul[@class="sojob-list"]/li')
        for li in lists:
            item = LiepinItem()
            info_url = li.xpath('./div[@class="sojob-item-main clearfix"]/div[@class="job-info"]//a/@href').extract_first()
            item['job_url'] = info_url
            item['job_tag'] = self.keyword
            # item['record_date'] = response.xpath('')
            item['job_name'] = li.xpath('.//div[@class="job-info"]//a/text()').extract_first().strip()
            item['job_salary'] = li.xpath('.//p[@class="condition clearfix"]/span[1]/text()').extract_first().strip()
            item['job_edu_require'] = li.xpath('.//p[@class="condition clearfix"]/span[2]/text()').extract_first().strip()
            item['job_exp_require'] = li.xpath('.//p[@class="condition clearfix"]/span[3]/text()').extract_first().strip()
            # item['job_welfare'] = li.xpath('//p[@class="temptation clearfix"]/span/text()').extract() # <—— bug：如果加点(即在li列表下进行xpath)就不能写入到json
            item['job_welfare'] = '，'.join(li.xpath('.//p[@class="temptation clearfix"]/span/text()').extract())
            item['company_name'] = li.xpath('.//p[@class="company-name"]/a/text()').extract_first().strip()

            yield Request(url=info_url, callback=self.info_parse, meta={'item': item}, dont_filter=True)

        # 翻页
        # page = response.meta['page'] + 1
        # if page < self.max_page:
        #     yield Request(url=self.start_urls.format(keyword=self.keyword, page=page), callback=self.parse,
        #                   meta={'page': page})

        for i in range(1, 3):
            print(f'开始爬取 第 {i + 1} 页：')
            next_url = self.start_urls.format(keyword=self.keyword, page=i)
            yield scrapy.Request(next_url, callback=self.parse)

    def info_parse(self, response):
        '''
        解析详情页
        :param response:
        :return:
        '''
        item = response.meta['item']
        # 职位信息
        item['job_info'] = "".join(response.xpath('//div[@class="content content-word"]/text()').extract()).strip()
        # 融资阶段
        item['company_financing_stage'] = response.xpath('//ul[@class="new-compintro"]/li[1]/text()').extract_first().split('：')[-1]
        # 公司人数
        item['company_people'] = response.xpath('//ul[@class="new-compintro"]/li[2]/text()').extract_first().split('：')[-1]
        # 公司地址
        item['company_location'] = response.xpath('//ul[@class="new-compintro"]/li[3]/text()').extract_first().split('：')[-1]
        # # 公司性质
        # item['company_nature'] = "".join(response.xpath('//span[@class="i_flag"]/../text()').extract()).strip()
        # # 公司概况
        # item['company_overview'] = "".join(response.xpath('//div[@class="tmsg inbox"]//text()').extract()).strip()
        # # 公司行业
        # item['company_industry'] = "".join(response.xpath('//span[@class="i_trade"]/../text()').extract()).strip()
        yield item
