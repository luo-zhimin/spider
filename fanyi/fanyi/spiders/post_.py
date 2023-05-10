import scrapy
import json


class PostSpider(scrapy.Spider):
    name = "post_"
    allowed_domains = ["fanyi.baidu.com"]

    # post 请求 如果没有参数 这个请求没有任何意义
    # 所以 start_urls 没有作用
    # start_urls = ["http://fanyi.baidu.com/"]

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'

        data = {
            'kw': 'final'
        }

        # url: 要发送的post地址
        # headers：可以定制头信息
        # callback: 回调函数
        # formdata: post所携带的数据，这是一个字典
        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)

    def parse_second(self, response):
        content = response.text
        # print(content)
        # transform json return response
        print(json.loads(content))
