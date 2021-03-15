# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import csv
import pymysql


class Json_Pipeline(object):
    def open_spider(self, spider):
        self.file = open('movie.json', 'w', encoding='utf-8')
        self.file.write('[')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.write(']')


class CSV_Pipeline(object):
    def __init__(self):
        self.file = open('movie.csv', 'w', encoding='utf-8')
        self.writer = csv.writer((self.file))
        header = ['name', 'year', 'director', 'type', 'area', 'language']
        self.writer.writerow(header)

    def process_item(self, item, spider):
        line = (item['name'], item['year'], item['director'], item['type'], item['area'], item['language'])
        self.writer.writerow(line)
        return item

    def close_spider(self, spider):
        self.file.close()

# class MySQL_Pipeline(object):
