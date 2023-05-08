import scrapy


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["car.autohome.com.cn"]
    # 如果请求的接口是以html结尾的 是不需要在最后面加/
    start_urls = ["https://car.autohome.com.cn/price/brand-133.html"]

    def parse(self, response):
        # pass
        print("====car====")
        name_list = response.xpath("//div[@class='main-title']/a/text()")
        price_list = response.xpath("//span[@class='font-arial']/text()")
        # for name in name_list:
        #     print(name.extract())
        for i in range(len(name_list)):
            name = name_list[i].extract()
            price = price_list[i].extract()
            print({'name': name, 'price': price})
        # print(name_list)
