import json, pymysql, csv


class Json_Pipeline:
    '''
    Json 写入
    '''

    def __init__(self):
        self.file = open('sina.json', 'w', encoding='utf-8')
        self.file.write('[')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.write(']')


class Mysql_Pipeline:
    '''
    MySQL 同步写入
    '''

    def open_spider(self, spider):
        self.db = pymysql.connect(host='localhost', port=3306, user='root', password='mysql', database='spider_data')
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        data = dict(item)
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = 'insert into sina_news (%s) values (%s)' % (keys, values)
        self.cursor.execute(sql, tuple(data.values()))
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.db.cursor.close()
        self.db.close()
