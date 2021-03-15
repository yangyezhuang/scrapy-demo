from itemadapter import ItemAdapter
import json
import csv
import pymysql


class Json_Pipeline(object):
    """
    以json保存
    """

    # def __init__(self):
    def open_spider(self, spider):
        self.file = open('movie.json', 'w', encoding='utf-8')
        self.file.write('[')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.write(']')


# 保存为csv文件
class CSV_Pipeline(object):
    def __init__(self):
        self.file = open('job.csv', 'w', encoding='utf-8', newline='')
        self.writer = csv.writer(self.file)
        header = ["name", "time", "salary", "company", "area", "exp", "edu", "number", "tags"]
        self.writer.writerow(header)

    def process_item(self, item, spider):
        line = (item['name'], item['time'], item['salary'], item['company'], item['area'], item['exp'], item['edu'],
                item['number'], item['tags'])
        self.writer.writerow(line)
        return item

    def close_spider(self, spider):
        self.file.close()


class Mysql_Pipeline:
    """
    同步MySQL
    """

    def __init__(self):
        self.db = pymysql.connect(host='localhost', database='spider_data', user='root', password='mysql', port=3306)
        self.cursor = self.db.cursor()
        print('数据库连接成功')

    def process_item(self, item, spider):
        data = dict(item)
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = 'insert into douban (%s) values (%s)' % (keys, values)
        self.cursor.execute(sql, tuple(data.values()))
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
