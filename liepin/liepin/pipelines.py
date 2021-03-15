from itemadapter import ItemAdapter
import json
import pymysql


class LiepinPipeline:
    '''
    json存储
    '''

    # 打开文件
    def __init__(self):
        self.file = open('job.json', 'w', encoding='utf-8')

    # 调用该方法处理数据
    def process_item(self, item, spider):
        # 读取item中的数据
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # 写入文件
        self.file.write(line)
        # 返回item
        return item

    # 该方法在spider被开启时被调用。
    def open_spider(self, spider):
        pass

    # 该方法在spider被关闭时被调用。
    def close_spider(self, spider):
        pass


class MysqlPipeline:
    '''
    MySQL存储
    '''

    def __init__(self):
        self.db = pymysql.connect(host='localhost', database='spider_data', user='root', password='mysql', port=3306)
        self.cursor = self.db.cursor()
        print('连接成功')

    def process_item(self, item, spider):
        data = dict(item)
        table = 'liepin'
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = 'insert into %s (%s) values (%s)' % (table, keys, values)
        self.cursor.execute(sql, tuple(data.values()))
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
