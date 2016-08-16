#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
import sys,getopt
from bs4 import BeautifulSoup

def usage():
	print "please enter:getmls -u username -n cardnumber"

opts,args=getopt.getopt(sys.argv[1:], "hu:n:")
username=""
userid=""
for op,value in opts:
	if op=="-u":
		username = value
	elif op=="-n":
		userid=value
	elif op=="-h":
		usage()
if username=='' or userid=='':
	usage()


data = {'name':username,'idnum':userid}
r = requests.post('http://www.runchina.org.cn/portal.php?mod=score&ac=personal',data)
bs = BeautifulSoup(r.text,"lxml")
for tr in bs.find("table",{"class":"table table-striped table-bordered  myScore defaultTable"}).findAll('tr'):
	if tr.find('td').string.find(u'比赛时间')>=0:
		continue
	s = ''
	for td in tr.findAll('td'):
		
		a = td.find('a')
		if a:
			if a.string.find(u'查看')>=0:
				continue
			s=s+a.string+'  '
		else:
			if td.string:
				
				s=s+td.string.strip()+'  '
			else:
				s=s+td.contents[0]+'  '
	print s
