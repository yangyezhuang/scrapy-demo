# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyYiqingItem(scrapy.Item):
    地区 = scrapy.Field()
    # 新增 = scrapy.Field()
    # 现有 = scrapy.Field()
    累计 = scrapy.Field()
    治愈 = scrapy.Field()
    死亡 = scrapy.Field()
