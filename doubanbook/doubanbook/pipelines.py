# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import csv
import pymysql


# 以json保存
class Json_Pipeline(object):
    def __init__(self):
        self.file = open('book.json', 'w', encoding='utf-8')

    # 该方法用于处理数据
    def process_item(self, item, spider):
        # 读取item中的数据
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(line)
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass


# 保存为csv文件
class CSV_Pipeline(object):
    def __init__(self):
        self.file = open('book.csv', 'w', encoding='utf-8', newline='')
        self.writer = csv.writer(self.file)
        header = ["name", "title", "score", "comment", "price", "author", "data", "store", "translate"]
        self.writer.writerow(header)

    def process_item(self, item, spider):
        line = (
        item['name'], item['title'], item['score'], item['comment'], item['price'], item['author'], item['data'],
        item['store'], item['translate'])
        self.writer.writerow(line)
        return item

    def close_spider(self, spider):
        self.file.close()


#    MySQL同步存储
class Mysql_Pipeline:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', database='spider_data', user='root', password='mysql', port=3306)
        self.cursor = self.db.cursor()
        print('数据库连接成功')

    def process_item(self, item, spider):
        data = dict(item)
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = 'insert into doubanbook (%s) values (%s)' % (keys, values)
        self.cursor.execute(sql, tuple(data.values()))
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()


class Mysql_Pipeline_1(object):
    '''
    MySQL操作
    '''

    def __init__(self):
        self.connect = pymysql.connect(host='localhost', user='root', passwd='mysql', db='spider_data')
        self.cursor = self.connect.cursor()
        print("连接数据库成功")

    def process_item(self, item, spider):
        sql = """
        insert into doubanbook (name,title,score,comment,price,author,data,store,translate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        self.cursor.execute(sql, (
            item['name'], item['title'], item['score'], item['comment'], item['price'], item['author'], item['data'],
            item['store'], item['translate']))
        self.connect.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
