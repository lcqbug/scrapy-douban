# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class BuxiusePipeline(ImagesPipeline):
    def process_item(self, item, spider):
        print(item['img_url'])
        return item
