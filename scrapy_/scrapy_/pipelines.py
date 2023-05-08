# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import urllib.request


class ScrapyPipeline:
    # before spider
    def open_spider(self, spider):
        self.fp = open("book.json", 'w', encoding='utf-8')

    # 如果要使用管道 需要在settings中开始管道 items 就是yield后面的book对象
    def process_item(self, item, spider):
        # 保存到文件
        # w 覆盖
        # with open('book.json', 'a', encoding='utf-8') as fp:
        #     # write 必须要写一个字符串
        #     # 文件操作过于频繁
        #     fp.write(str(item))
        #     fp.close()

        self.fp.write(str(item))
        return item

    # after spider
    def close_spider(self, spider):
        self.fp.close()


# 多条管道同时下载
# 定义管道类
# 在settings中开启管道

class DangDangDownloadPipelines:
    def process_item(self, item, spider):
        # 下载图片
        url = 'http:' + item.get('image')
        name = './books/' + item.get('name') + ".jpg"
        urllib.request.urlretrieve(url=url, filename=name)

        return item
