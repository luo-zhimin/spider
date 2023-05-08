import scrapy


class TcSpider(scrapy.Spider):
    name = "tc"
    allowed_domains = ["https://sh.58.com/sou/?key=%E5%90%8E%E5%8F%B0&button=%E6%90%9C%C2%A0%E7%B4%A2"]
    start_urls = ["https://sh.58.com/sou/?key=%E5%90%8E%E5%8F%B0&button=%E6%90%9C%C2%A0%E7%B4%A2"]

    def parse(self, response):
        # pass
        # 字符串
        # content = response.text
        # 二进制数据
        # content = response.body
        content = response.xpath("//div[@id='filter']//a[@class='select']/span")[0]
        # content = response.xpath("//div[@id='filter']/div[@class='tabs']/a/span")[0]
        print("====")
        print(content.extract())
