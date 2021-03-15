from itemadapter import ItemAdapter

import json
import pymysql


class JingdongPipeline(object):
    """
    json存储
    """

    def __init__(self):
        # def open_spider(self, spider):
        self.file = open('jd.json', 'w', encoding='utf-8')
        self.file.write('[')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.write(']')


class MysqlPipeline:
    """
    MySQL同步存储
    """

    def __init__(self):
        self.db = pymysql.connect(host='localhost', database='spider_data', user='root', password='mysql', port=3306)
        self.cursor = self.db.cursor()
        print('连接成功')

    def process_item(self, item, spider):
        data = dict(item)
        table = 'jd'
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = 'insert into %s (%s) values (%s)' % (table, keys, values)
        self.cursor.execute(sql, tuple(data.values()))
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
