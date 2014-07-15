#-*- coding: utf-8 -*
import urllib
import urllib2
import re
import time
import sys
import os

#解决中文报错
reload(sys)
sys.setdefaultencoding('utf-8')

#HuoQ = 'http://www.douban.com/group/haixiuzu/?ref=sidebar'
### 代理模块(全局代理)
print '#'*50
print '本程序主要采集豆瓣<请不要害羞>小组的图片'
print '#'*50
print '采集前需要输入代理服务器地址，这样可以防止被豆瓣屏蔽.'
print '推荐一个代理地址: http://cn-proxy.com/'
print '只需要输入服务器地址以及端口号，不需要输入http'
print '例子:127.0.0.1:8080'
print '#'*50
proxy_input = raw_input('请输入采集代理服务器:')
proxy_handler = urllib2.ProxyHandler({'http':'%s'%proxy_input})
opener = urllib2.build_opener(proxy_handler)
urllib2.install_opener(opener)

#采集本地路径全局变量
#img_LuJ = raw_input("图片下载路径:".decode('utf-8'))
#img_LuJ2 = os.path.abspath(img_LuJ)

#模块化输出
#获取帖子单页html
def gethtml2(url2):
    html2 = urllib2.urlopen(url2).read().decode('utf-8')
    return  html2

#抽取图片并下载列表
def gettoimg(html2):
    #添加正则 匹配url路径数字 d+代表获取0-9无限循环\转义符号
    reg2 = r'http://www.douban.com/group/topic/\d+'
    toplist = re.findall(reg2,html2)
    x = 0
    #限制下载图片数量
    #输出topicurl 每次输出一个 的循环
    for topicurl in toplist:
        x+=1
    return topicurl

#下载图片到本地
def download(topic_page):
    #获取贴内图片  正则  ".+\" .匹配任意字符 + 匹配前一个字符或无限次 \ 转移符号 也就是 匹配所有字符
    reg3 = r'http://img3.douban.com/view/group_topic/large/public/.+\.jpg'
    imglist = re.findall(reg3,topic_page)
    i = 1
    download_img = None
    for imgurl in imglist:
#取图片id为文件名
        img_numlist = re.findall(r'p\d{7}',imgurl)
        for img_num in img_numlist:
            #获取用户输入路径
            #download_img = urllib.urlretrieve(imgurl,img_LuJ2 + '/%s.jpg'%img_num)
            #固定程序路径
            download_img = urllib.urlretrieve(imgurl,'Doubanimg/%s.jpg'%img_num)
            time.sleep(1)
            i+=1
            print (imgurl)
    return download_img

page_end = int(input('请输入采集页码数:'))
num_end = page_end*25
num = 0
page_num = 1
while num<=num_end:
    #获取页面数 从 0 开始
    html2 = gethtml2('http://www.douban.com/group/haixiuzu/discussion?start=%d'%num)
    #抽取下载图片
    topicurl = gettoimg(html2)
    topic_page = gethtml2(topicurl)
    download_img=download(topic_page)
   # download_img = download(topic_page)
    num = page_num*25
    page_num+=1

else:
    print('程序采集完成')
