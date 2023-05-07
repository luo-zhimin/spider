import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字 用于运行时候 使用的值
    name = "baidu"
    # 允许访问的域名
    allowed_domains = ["www.baidu.com"]
    # 起始的url域名 第一次要访问的域名
    # start_urls 是在allowed_domains的前面添加一个http:// 后面又添加了一个/
    start_urls = ["http://www.baidu.com/"]

    # 运行了statr_urls 之后执行的方法
    def parse(self, response):
        pass
