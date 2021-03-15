import scrapy


class ScrapySunItem(scrapy.Item):
    response_time = scrapy.Field()
    question_time = scrapy.Field()
    num = scrapy.Field()
    state = scrapy.Field()
    title = scrapy.Field()


class ScrapyCarItem(scrapy.Item):
    品牌 = scrapy.Field()
    生产厂家 = scrapy.Field()
    测评车型 = scrapy.Field()
    车辆级别 = scrapy.Field()
    车辆型号 = scrapy.Field()
    耐撞性与维修经济性 = scrapy.Field()
    车内乘员 = scrapy.Field()
    车外行人 = scrapy.Field()
    辅助安全 = scrapy.Field()
    安全装备配置 = scrapy.Field()
    指导价格 = scrapy.Field()
    低速碰撞 = scrapy.Field()
    正面25偏置碰撞 = scrapy.Field()
    侧面碰撞 = scrapy.Field()
    车顶强度 = scrapy.Field()
    座椅头枕 = scrapy.Field()
    行人保护 = scrapy.Field()
    FCW = scrapy.Field()


class ScrapyDamaiItem(scrapy.Item):
    name = scrapy.Field()
    city = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()
    high_price = scrapy.Field()
    low_price = scrapy.Field()
    actor = scrapy.Field()
    state = scrapy.Field()
