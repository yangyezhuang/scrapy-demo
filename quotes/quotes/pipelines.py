import pymysql
import json
import csv

class Json_Pipeline(object):
    '''
    Json形式保存
    '''
    def __init__(self):
    # def open_spider(self, spider):
        self.file = open('quotes.json', 'w', encoding='utf-8')
        self.file.write('[')

    # 处理数据
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.write(']')



# 保存为csv文件
class CSV_Pipeline(object):
    def __init__(self):
        self.file = open('quotes.csv', 'w', encoding='utf-8',newline='')
        self.writer = csv.writer(self.file)
        header=["sentence", "author","tags"]
        self.writer.writerow(header)

    def process_item(self, item, spider):
        line = (item['sentence'],item['author'],item['tags'])
        self.writer.writerow(line)
        return item

    def close_spider(self, spider):
        self.file.close()



class Mysql_Pipeline:
    """
    MySQL同步存储
    """
    def __init__(self):
        self.db = pymysql.connect(host='localhost', database='spider_data', user='root', password='mysql', port=3306)
        self.cursor = self.db.cursor()
        print('连接成功')

    def process_item(self, item, spider):
        data = dict(item)
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = 'insert into quotes (%s) values (%s)' % (keys, values)
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
        # sql语句
        sql = """
        insert into quotes (sentence,author,tags) VALUES (%s,%s,%s)
        """
        # 执行插入数据到数据库操作
        self.cursor.execute(sql, (item['sentence'], item['author'], item['tags']))
        # 提交，不进行提交无法保存到数据库
        self.connect.commit()
 
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()