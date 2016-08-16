from stock.items import StockItem
import scrapy
import json

class StockSpider(scrapy.Spider):
	name = "stock"
	def parse(self,response):
		# for sel in response.xpath('//tr[contains(@class,"stock_up")]'):	
		# 	item = StockItem()
		# 	item.stockCode = sel.xpath('.//td[0]/a/text()').extract()
		# 	item.stockName = sel.xpath('.//td[1]/a/text()').extract()
		# 	item.price = sel.xpath('.//td[2]/span/text()').extract()
		# 	print item
		# 	yield item
		items = json.load(response)
		for stock in items['stocks']:
			print stock['symbol']


	def start_requests(self):
		return [scrapy.Request("https://xueqiu.com/stock/cata/stocklist.json?page=1&size=30&order=desc&orderby=percent&type=11",headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
								"Accept-Encoding":"gzip, deflate, sdch",
								"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
								"Cache-Control":"max-age=0",	
								"AlexaToolbar-ALX_NS_PH":"AlexaToolbar/alx-4.0",
								"Connection":"keep-alive",
								"Cookie":"s=24k13e7urh; bid=ff73e0de2b082aa5c48ae8cfde09b12f_iihhjcmt; webp=1; last_account=scaluo%40gmail.com; xq_a_token=8f2a01e7c7fc6160aab83cba7a0b37d548025d91; xq_r_token=d279cb0b51dc17571cf8587dc39e8f988eb0753c; __utma=1.514356554.1417621001.1461849475.1461851938.119; __utmb=1.2.10.1461851938; __utmc=1; __utmz=1.1417621001.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1459668721; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1461852057",
								"Host":"xueqiu.com",
								'Accept':'*/*',
								"Referer":"https://xueqiu.com/hq",
								"Upgrade-Insecure-Requests":"1",
								"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
                                   })]

		#return [scrapy.Request("http://www.hupu.com/")]

  		# return [scrapy.Request("https://xueqiu.com/stock/cata/stocklist.json?page=1&size=30&order=desc&orderby=percent&type=11%2C12&_=1461852061649",
  		# 						headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
  		# 								 'Accept':'*/*'
    #                                })]	