# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 要下载的数据有什么

    # 当当网
    # 图片
    image = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()

    # 电影 电影天堂
    # 电影名字
    movie_name = scrapy.Field()
    # 电影图片
    movie_image = scrapy.Field()
