import urllib.request
import json
import http.cookiejar

CookieJar = http.cookiejar.CookieJar()
CookieProcessor = urllib.request.HTTPCookieProcessor(CookieJar)
opener = urllib.request.build_opener(CookieProcessor)
urllib.request.install_opener(opener)

#登陆获得cookie
params = urllib.parse.urlencode({'username':'scaluo@gmail.com','password':'monkey'}).encode(encoding='UTF8')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'}
request = urllib.request.Request('http://xueqiu.com/user/login',headers=headers)
httpf = opener.open(request, params)

count = 0
for i in range(200):
	url = 'https://xueqiu.com/stock/cata/stocklist.json?page='+str(i+1)+'&size=30&order=desc&orderby=percent&type=11'
	req = urllib.request.Request(url,headers=headers)
	html = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(html)
	stockdata = data['stocks']
	if len(stockdata)==0:
		print(str(count))
		break
	for i in range(len(stockdata)):
		print(stockdata[i]['symbol']+","+stockdata[i]['name']+","+stockdata[i]['current'])
		count  += 1
    