# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem

class StreetPicPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            image_url = image_url.split('?')[0]
            yield scrapy.Request(image_url, meta={'item': item})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        # 从URL提取图片的文件名
        image_guid = request.url.split('/')[-1]
        # 拼接最终的文件名,格式:full/{书名}/{章节}/图片文件名.jpg
        filename = 'kimwebphoto/'+item["photographer"][0]+'/'+image_guid
        print filename
        return filename
