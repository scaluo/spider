from scrapy.spiders import CSVFeedSpider
from stockcsv.items import StockcsvItem
import scrapy

class StockcsvSpider(CSVFeedSpider):
    name = "stockcsv"
    start_urls = ["http://xueqiu.com/S/SH600109/historical.csv"]
    delimiter = ','
    quotechar = '"'
    headers = ["symbol","date","open","high","low","close","volume"]

    def parse_row(self,response,row):
        item = StockcsvItem()
        item['symbol'] = row["symbol"]
        item['date'] = row["date"]
        item['close'] = row["close"]
        print item['symbol']+':'+item['date']+":"+item['close']
        return item

    def start_requests(self):
        return [scrapy.Request("http://xueqiu.com/S/SH600109/historical.csv",headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                   "Accept-Encoding":"gzip, deflate, sdch",
                                   "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
                                   "AlexaToolbar-ALX_NS_PH":"AlexaToolbar/alxg-3.3",
                                   "Cache-Control":"max-age=0",
                                   "Connection":"keep-alive",
                                   "Cookie":"s=24k13e7urh; bid=ff73e0de2b082aa5c48ae8cfde09b12f_iihhjcmt; webp=1; __utmt=1; last_account=scaluo%40gmail.com; xq_a_token=240b35abe842280c58a331952ad6f35f5f45553f; xq_r_token=34d85993042acb9bcef56244c4e1946070169d6b; __utma=1.514356554.1417621001.1459668725.1459757730.114; __utmb=1.2.10.1459757730; __utmc=1; __utmz=1.1417621001.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1457534292,1459668721; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1459757868",
                                   "Host":"xueqiu.com",
                                   "Referer":"http://xueqiu.com/S/SH600109",
                                   "Upgrade-Insecure-Requests":"1",
                                   "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36})"
                                   })]
