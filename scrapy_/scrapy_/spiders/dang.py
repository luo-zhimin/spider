import scrapy

# from scrapy_project.items import ScrapyItem
from scrapy_.items import ScrapyItem


class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.31.04.00.00.00.html"]

    def parse(self, response):
        print("====dang====")
        # pipelines 管道 下载数据
        # items 定义数据结构
        # 定位 解析
        # src = //ul[@id='component_59']/li/a/img/@src
        # alt = //ul[@id='component_59']/li/a/img/@alt
        # price = //ul[@id='component_59']/li/p/span[@class='search_now_price']/text()
        # 所有的selector对象都可以再次调用xpath方法
        li_list = response.xpath("//ul[@id='component_59']/li")
        for li in li_list:
            # print(li)
            # 图片懒加载
            # 第一张图片和其他标签的属性不一样 第一张是src 其他是data-original
            src = li.xpath("./a/img/@data-original").extract_first()
            if src:
                src = src
            else:
                src = li.xpath("./a/img/@src").extract_first()

            name = li.xpath("./a/img/@alt").extract_first()
            price = li.xpath("./p/span[@class='search_now_price']/text()").extract_first()
            # print(src, name, price)

            book = ScrapyItem(image=src, name=name, price=price)
            # 交给pipelines 进行下载
            # 获取一个book就将book交给pipelines
            yield book
        # pass
