# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MyItem(scrapy.Item):
    title = scrapy.Field()


# 需要抓取的数据的格式   抓取哪些字段
class BuxiuseItem(scrapy.Item):
    img_url = scrapy.Field()
    # name = scrapy.Field()
