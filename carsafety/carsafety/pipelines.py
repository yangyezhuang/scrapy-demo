# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

import pymysql


class CarsafetyPipeline:
    def process_item(self, item, spider):
        return item


class JsonPipeline:
    def __init__(self):
        pass

    def process_item(self):
        pass

    def close_spider(self):
        pass


class CsvPipeline:
    def __init__(self):
        self.file = open('data.csv', 'w', newline='')
        header = []
        self.writer = csv.writer(header)

    def process_item(self, item, spider):
        return item

    def close_spider(self):
        pass


class MysqlPipeline:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            passwd='mysql',
            db='test_db',
            charset='utf8'
        )
        self.conn.cursor()

        def process_item(self, item, spider):
            keys = dict()
            values = dict

            return item

        def close_spider(self):
            self.conn.close()
