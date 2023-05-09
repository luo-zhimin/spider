import scrapy

from scrapy_.items import ScrapyItem


class MoviceSpider(scrapy.Spider):
    name = "movice"
    allowed_domains = ["www.ygdy8.net"]
    start_urls = ["https://www.ygdy8.net/html/gndy/china/index.html"]

    def parse(self, response):
        # 要第一个的名字 和 第二页的图片
        # movie_name = response.xpath("//a[@class='ulink'][2]/text()")
        # movie_image = response.xpath("//a[@class='ulink'][2]/@href")
        a_list = response.xpath("//a[@class='ulink'][2]")
        print("====movie====")
        for a in a_list:
            movie_name = a.xpath("./text()").extract_first()
            # 需要进行组装 二次请求拿取图片 管道
            # 第二页地址 https://www.ygdy8.net/
            href = a.xpath("./@href").extract_first()
            url = 'https://www.ygdy8.net' + href
            # 对第二页链接发起访问
            print(movie_name, url)
            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name': movie_name})

    def parse_second(self, response):
        # print('parse_second~~~')
        # 拿不到数据的情况下 检查xpath
        # image = response.xpath('//span/img/@src').extract_first()
        image = response.xpath("//div[@id='Zoom']//img/@src").extract_first()
        # 接收到请求 meta的参数
        movie_name = response.meta['name']
        # print(image)
        movie = ScrapyItem(movie_name=movie_name, movie_image=image)
        yield movie
        # pass
