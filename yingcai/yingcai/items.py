# Define here the models for your scraped items

import scrapy


class YingcaiItem(scrapy.Item):
    job_url = scrapy.Field()  # 详情页面url
    record_date = scrapy.Field()  # 爬取数据的时间
    job_tag = scrapy.Field()  # 爬取数据的浏览标签或检索词
    job_name = scrapy.Field()  # 招聘名称
    job_info = scrapy.Field()  # 职位信息
    job_salary = scrapy.Field()  # 工资
    job_welfare = scrapy.Field()  # 职位福利
    job_exp_require = scrapy.Field()  # 经验要求
    job_edu_require = scrapy.Field()  # 学历要求

    company_name = scrapy.Field()  # 公司名称
    company_industry = scrapy.Field()  # 公司行业
    company_nature = scrapy.Field()  # 公司性质
    company_people = scrapy.Field()  # 公司人数
    company_location = scrapy.Field()  # 公司地址
    company_overview = scrapy.Field()  # 公司概况
    company_financing_stage = scrapy.Field()  # 公司融资阶段
