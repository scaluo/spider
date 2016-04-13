# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StreetPicItem(scrapy.Item):
    photographer = scrapy.Field()
    photographer_url = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
