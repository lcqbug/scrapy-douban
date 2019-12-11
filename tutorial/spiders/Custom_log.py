import logging
import scrapy

import logging
logger = logging.getLogger(__name__)
logger.warning("This is a warning")

class MySpider(scrapy.Spider):

    name = 'myspider1'
    start_urls = ['https://scrapinghub.com']

    def parse(self, response):
        logger.info('Parse function called on %s', response.url)