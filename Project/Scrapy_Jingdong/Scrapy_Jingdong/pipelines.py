from itemadapter import ItemAdapter
import json
import csv
import pymysql


class Json_Pipeline(object):
    """
    Json
    """
    def open_spider(self, spider):
        self.file = open('jd.json', 'w', encoding='utf-8')
        self.file.write('[')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.write(']')


class CSV_Pipeline(object):
    """
    CSV
    """
    def __init__(self):
        pass