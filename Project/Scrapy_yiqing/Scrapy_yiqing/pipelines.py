# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class ScrapyYiqingPipeline:
    def process_item(self, item, spider):
        return item


class Mysql_Pipeline:
    def open_spider(self,spider):
        self.db = pymysql.connect(host='localhost', user='root', password='mysql', database='flask', port=3306)
        self.cursor = self.db.cursor()
        print('连接成功')

    def process_item(self, item, spider):
        data = dict(item)
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = 'insert into yi(%s) values(%s)' % (keys, values)
        self.cursor.execute(sql, tuple(data.values()))
        self.db.commit()
        return item

    def close_spider(self):
        self.cursor.close()
        self.conn.close()
