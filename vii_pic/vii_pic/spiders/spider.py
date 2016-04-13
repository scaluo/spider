import scrapy
from scrapy.spiders import Spider
from vii_pic.items import ViiPicItem

class ViiPicSpider(Spider):
    name = 'viipic'
    start_urls = ['http://viiphoto.com/articles/']

    def parse(self,response):
        for sel in response.xpath('//div[@class="hp_full_box"]'):
            item = ViiPicItem()
            item["storyname"] = sel.xpath('.//div[@class="yellowbox"]/p/text()').extract()[0]
            suburl = sel.xpath('.//a/@href').extract()[1]
            yield scrapy.Request(url=suburl,meta={'item':item},callback=self.parse_pic)

    def parse_pic(self,response):
        item = response.meta['item']
        item["image_urls"] = [url for url in response.xpath('//img[@class="slide"]/@src').extract()]
        #print item["image_urls"]
        return item
