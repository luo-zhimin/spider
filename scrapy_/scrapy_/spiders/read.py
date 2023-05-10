import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_.items import ScrapyItem


class ReadSpider(CrawlSpider):
    name = "read"
    allowed_domains = ["www.dushu.com"]
    start_urls = ["https://www.dushu.com/book/1617_1.html"]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/112.0.0.0 Safari/537.36',
    }

    rules = (
        Rule(LinkExtractor(allow=r"/book/1617_\d+\.html"),
             callback="parse_item",
             # 是否更进 爬取 所有符合规则的
             follow=True),
    )

    def parse_item(self, response):
        # 图片 + 名字
        img_list = response.xpath("//div[@class='bookslist']//img")
        for img in img_list:
            picture = img.xpath("./@data-original").extract_first()
            # picture = img.xpath("./@src").extract_first()
            name = img.xpath("./@alt").extract_first()

            book = ScrapyItem(book_name=name, book_image=picture)
            yield book
        # return item
