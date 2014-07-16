#coding:utf-8
import os
import re
import urllib
import urllib2

f = open('proxy_list.txt','w')
exp1 = re.compile("(?isu)<tr[^>]*>(.*?)</tr>")
exp2 = re.compile("(?isu)<td[^>]*>(.*?)</td>")
proxy_ua = {'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
proxyHtml = urllib2.Request(url="http://www.getproxy.jp/cn",headers=proxy_ua)
proxySocket = urllib2.urlopen(proxyHtml)
htmlSource = proxySocket.read()
#print htmlSource
for row in exp1.findall(htmlSource):
   for col in exp2.findall(row)[:1]:
    #写入代理信息
    f.write(col+'\n')
    #print col
    #htmlSource.close()
f.close()