# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HaokanzhanItem(scrapy.Item):
    name = scrapy.Field()
    year = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    language = scrapy.Field()
    url = scrapy.Field()
