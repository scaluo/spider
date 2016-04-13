import scrapy
from scrapy.spiders import Spider
from street_pic.items import StreetPicItem

class SteetPicSpider(Spider):
    name = 'streetpic'
    start_urls = ['http://erickimphotography.com/blog/start-here/']

    def parse(self,response):
        for sel in response.xpath('//ul[@class="xoxo blogroll"]/li/a'):
            item = StreetPicItem()
            item["photographer"] = sel.xpath('text()').extract()
            item["photographer_url"] = sel.xpath('@href').extract()[0]
            print item["photographer"]
            print item["photographer_url"]
            yield scrapy.Request(url=item["photographer_url"],meta={'item':item},callback=self.parse_pic)

    def parse_pic(self,response):
        item = response.meta['item']
        #for sel in response.xpath('//img[contains(@class,"alignnone")]'):
            #print sel.xpath('@src').extract()
        item["image_urls"] = [url for url in response.xpath('//img/@src').extract()]
        #print item["image_urls"]
        return item
