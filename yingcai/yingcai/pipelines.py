from itemadapter import ItemAdapter
import json

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
