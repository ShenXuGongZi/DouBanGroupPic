#-*- coding: utf-8 -*
# coding=cp936
import urllib
import urllib2
import re
import time
import random
import sys
import os
type = sys.getfilesystemencoding()

print '#'*50
print '#'*2 + '\t\t\t\t豆瓣小组采集器\t\t\t\t\t'.decode('UTF-8').encode('GBK')+'#'*2
print '#'*50

mkmulu = os.path.exists('Doubanimg')

if not mkmulu:
    print '#'*50
    print '目录创建成功!图片将下载到Doubanimg目录'.decode('UTF-8').encode('GBK')
    print '#'*50
    os.mkdir('Doubanimg')
    # return True
else:
    print '#'*50
    print '目录存在,图片下载到Doubanimg目录'.decode('UTF-8').encode('GBK')
    print '#'*50
    # return False

print '#'*50
print '#'*2 + '\t肾虚公子 亲情制作'.decode('UTF-8').encode('GBK') 
print '#'*2 + '\t主页: Douban.miaowu.asia'.decode('UTF-8').encode('GBK') 
print '#'*50
print '说明:本程序可以采集豆瓣任何小组的图片.'.decode('UTF-8').encode('GBK') 
print '说明:采集的图片在文件夹Doubanimg内.'.decode('UTF-8').encode('GBK') 
print '注意:代理没有验证，如果不成功请重新运行.'.decode('UTF-8').encode('GBK') 
print '#'*50


print '请输入小组代码,默认采集豆瓣害羞组[ID=haixiuzu]'.decode('UTF-8').encode('GBK') 
print '小组ID就是(http://www.douban.com/group/这里的字符/)'.decode('UTF-8').encode('GBK') 
Douban_group = raw_input('请输入小组ID(默认按回车继续):'.decode('UTF-8').encode('GBK') )or 'haixiuzu'
Douban_group_url = 'http://www.douban.com/group/'

def gethtml2(url2):
    Douban_ua = {'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
    Douban_Html = urllib2.Request(url=(url2),headers=Douban_ua)
    Douban_Socket = urllib2.urlopen(Douban_Html)
    html2 = Douban_Socket.read().decode('utf-8')
    return  html2

def gettoimg(html2):
    reg2 = r'http://www.douban.com/group/topic/\d+'
    toplist = re.findall(reg2,html2)
    x = 0
    for topicurl in toplist:
        x+=1
    return topicurl

def download(topic_page):
    reg3 = r'http://img3.douban.com/view/group_topic/large/public/.+\.jpg'
    imglist = re.findall(reg3,topic_page)
    i = 1
    download_img = None
    for imgurl in imglist:
        img_numlist = re.findall(r'p\d{7}',imgurl)
        for img_num in img_numlist:
            download_img = urllib.urlretrieve(imgurl,'Doubanimg/%s.jpg'%img_num)
            time.sleep(0.5)
            i+=1
            print (imgurl)
    return download_img


print '-'*50
print '请输入采集帖子数,默认采集10个帖子'.decode('UTF-8').encode('GBK') 
page_end = int(raw_input('输入数字即可(默认按回车继续):'.decode('UTF-8').encode('GBK'))or 10) 
print '-'*50
print '正在采集图片中，程序可能用较长时间,此时您可以干点别的，比如喝杯咖啡？'.decode('UTF-8').encode('GBK') 
print '-'*50

num_end = page_end*25
num = 0
page_num = 1
try:
    while num<=num_end:
        html2 = gethtml2(Douban_group_url+Douban_group+"/discussion?start=%d"%num)
        topicurl = gettoimg(html2)
        topic_page = gethtml2(topicurl)
        download_img=download(topic_page)
        num = page_num*25
        page_num+=1
except Exception:
    print '错误：图片下载失败！请检查小组名称是否正确!!请重新运行本程序'.decode('UTF-8').encode('GBK') 
    print '-'*50
    raw_input('按回车结束程序:'.decode('UTF-8').encode('GBK') )
else:
    print '#'*20 + '下载完成'.decode('UTF-8').encode('GBK')  + '#'*20
    print '程序采集已经结束感谢您的使用!'+'网站:http://Douban.miaowu.asia'.decode('UTF-8').encode('GBK') 
    print '#'*20 + '程序结束'.decode('UTF-8').encode('GBK')  + '#'*20
    JS = raw_input('按回车结束程序:'.decode('UTF-8').encode('GBK') )
    print JS