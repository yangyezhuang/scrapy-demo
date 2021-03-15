# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanbookItem(scrapy.Item):
    name=scrapy.Field()
    title = scrapy.Field()
    score =scrapy.Field()
    comment = scrapy.Field()
    price=scrapy.Field()
    author=scrapy.Field()
    data=scrapy.Field()
    store = scrapy.Field()
    translate=scrapy.Field()



