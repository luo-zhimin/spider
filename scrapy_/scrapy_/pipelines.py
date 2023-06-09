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
        self.fp = open("./books/book.json", 'w', encoding='utf-8')
        # self.fp = open("./movie/movie.json", 'w', encoding='utf-8')

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


class MovieDownloadPipelines:

    def process_item(self, item, spider):
        name = './movie/' + item.get('movie_name') + ".jpg"
        urllib.request.urlretrieve(url=item.get("movie_image"), filename=name)
        return item


class BookDownloadPipelines:

    def process_item(self, item, spider):
        # download picture
        # name = './books/' + item.get('book_name') + ".jpg"
        # urllib.request.urlretrieve(url=item.get("book_image"), filename=name)
        return item


# 加载settings文件
from scrapy.utils.project import get_project_settings
import pymysql


class MysqlPipelines:

    # 链接mysql
    def open_spider(self, spider):
        # pass
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWORD']
        self.name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']

        self.connect()

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.name,
            charset=self.charset
        )

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # sql拼接
        sql = 'insert into book(name,image) values ("{}","{}")' \
            .format(item['book_name'], item['book_image'])

        # 执行
        self.cursor.execute(sql)
        # 提交
        self.conn.commit()

        return item

    def close_spider(self, spider):
        # pass
        # close
        self.cursor.close()
        self.conn.close()
