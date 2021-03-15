from itemadapter import ItemAdapter
import json
import csv
import pymysql


class Json_Pipeline(object):
    """
    Json
    """

    def open_spider(self, spider):
        self.file = open('car.json', 'w', encoding='utf-8')
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
        self.file = open('damai.csv', 'w', encoding='utf-8', newline='')
        self.writer = csv.writer(self.file)
        header = ['name', 'city', 'location', 'date', 'high_price', 'low_price', 'actor', 'state']
        self.writer.writerow(header)

    def process_item(self, item, spider):
        line = (item['name'], item['city'], item['date'], item['actor'], item['state'],
                item['location'], item['low_price'], item['high_price'])
        self.writer.writerow(line)
        return item

    def close_spider(self, spider):
        self.file.close()


class Mysql_Pipeline():
    """
    MySQL同步
    """

    def __init__(self):
        self.db = pymysql.connect(host='localhost', database='spider_data', user='root', password='mysql', port=3306)
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        data = dict(item)
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = 'insert into sun (%s) value (%s)' % (keys, values)
        self.cursor.execute(sql, tuple(data.values()))
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()


class Mysql_Pipeline2(object):
    """
    MySQL_2
    """

    def __init__(self):
        self.connect = pymysql.connect(host='localhost', user='root', passwd='mysql', db='spider_data')
        self.cursor = self.connect.cursor()
        print('数据库连接成功')

    def process_item(self, item, spider):
        sql = 'insert into sun (response_time,question_time,num,state,title)'
        self.cursor.execute(sql,
                            (item['response_time'], item['question_time'], item['num'], item['state'], item['title']))
        self.connect.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
