import scrapy


class DoubanItem(scrapy.Item):
    name = scrapy.Field()
    daoyan = scrapy.Field()
    title = scrapy.Field()
    # score = scrapy.Field()
    # comment = scrapy.Field()
    # time=scrapy.Field()
