import scrapy
from scrapy import Request
from ..items import ScrapyCarItem


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['www.ciasi.org.cn']
    start_urls = ['http://www.ciasi.org.cn/Home/safety/index?sid=15&bid=&cid=&sss=1&year=51,50']

    def parse(self, response):
        lists = response.xpath('//div[@class="eval_by_item"]')
        for li in lists:
            item = ScrapyCarItem()
            item['品牌'] = li.xpath('.//div[@class="ev_i_brand"]//p[@class="ev_br_t"]/text()').extract_first()
            item['生产厂家'] = li.xpath('.//div[@class="ev_i_manu"]//p/text()').extract_first()
            item['测评车型'] = li.xpath('.//div[@class="ev_i_models"]//p/text()').extract_first()
            item['车辆级别'] = li.xpath('.//div[@class="ev_i_level"]//p/text()').extract_first()
            item['车辆型号'] = li.xpath('.//div[@class="ev_i_model"]//p/text()').extract_first()
            item['车内乘员'] = li.xpath('.//div[@class="ev_i_car"][2]//span/text()').extract_first()
            item['车外行人'] = li.xpath('.//div[@class="ev_i_outside"]//span/text()').extract_first()
            item['辅助安全'] = li.xpath('.//div[@class="ev_i_security"]//span/text()').extract_first()
            item['耐撞性与维修经济性'] = li.xpath('.//div[@class="ev_i_car"][1]//span/text()').extract_first()
            info_url = li.xpath('.//a/@href').extract_first()
            info_url = 'https://www.ciasi.org.cn' + info_url

            yield Request(url=info_url, callback=self.parse_info, meta={'item': item}, dont_filter=True)

    def parse_info(self, response):
        item = response.meta['item']
        # 安全装备配置
        lists = []
        info_list = response.xpath('//div[@class="pur_l_txt"]/p/text()').extract()
        color_list = response.xpath('//div[@class="pur_le_item"]//img/@src').extract()
        for i in range(len(color_list)):
            if color_list[i] == '/Public/Home/images/icon/icon-greenDi.png':
                s = info_list[i]
                lists.append(s)
        str = ''
        for j in lists:
            str += j + '-'

        item['安全装备配置'] = str.strip('-')
        item['低速碰撞'] = response.xpath('//div[@class="par_block"]/div[1]//div[@class="pa_t_bz"]/span/text()').extract_first()
        item['正面25偏置碰撞'] = response.xpath('//div[@class="par_block"]/div[2]//div[@class="pa_t_bz"]/span/text()').extract_first()
        item['侧面碰撞'] = response.xpath('//div[@class="par_block"]/div[3]//div[@class="pa_t_bz"]/span/text()').extract_first()
        item['车顶强度'] = response.xpath('//div[@class="par_block"]/div[4]//div[@class="pa_t_bz"]/span/text()').extract_first()
        item['座椅头枕'] = response.xpath('//div[@class="par_block"]/div[5]//div[@class="pa_t_bz"]/span/text()').extract_first()
        item['行人保护'] = response.xpath('//div[@class="par_block"]/div[6]//div[@class="pa_t_bz"]/span/text()').extract_first()
        item['FCW'] = response.xpath('//div[@class="par_block"]/div[7]//div[@class="pa_t_bz"]/span/text()').extract_first()
        item['指导价格'] = response.xpath('//div[@class="pa_bt_le"]/span/text()').extract_first().split('为')[-1].replace('元。', '')

        yield item
