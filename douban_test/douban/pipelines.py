from itemadapter import ItemAdapter
import json
import pymysql
import paramiko


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


class Remote:
    # def __init__(self):
    def open_spider(self,spider):
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect('172.16.1.2', 22, 'root', 'passwd')
        self.sftp = self.client.open_sftp()
        self.fileObject = self.sftp.open('/home/data/text', 'wb')



    def save(self,item,spider):
        self.fileObject.write(item)
        return item

    def close_spider(self,spider):
        self.fileObject.close()

