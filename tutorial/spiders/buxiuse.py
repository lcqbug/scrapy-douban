# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import BuxiuseItem


class BuxiuseSpider(scrapy.Spider):
    name = 'buxiuse'
    allowed_domains = ['buxiuse.com']
    start_urls = ['http://buxiuse.com/']

    def parse(self, response):
        imageurls = response.xpath('//img/@src').extract()
        item = BuxiuseItem()
        for url in imageurls:
            item['img_url'] = [url]
            yield item
        # item['img_url'] = imageurls
        # yield item
