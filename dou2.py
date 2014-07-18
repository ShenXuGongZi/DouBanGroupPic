#-*- coding: utf-8 -*
import urllib
import urllib2
import re
import time
import sys
import os
import random

print '#'*50
print '#'*2 + u'\t\t\t\t豆瓣小组采集器\t\t\t\t\t'+'#'*2
print '#'*50
print '*'*20+u'开始采集代理'+'*'*20
#采集代理信息
f = open('proxy_list.txt','w')
exp1 = re.compile("(?isu)<tr[^>]*>(.*?)</tr>")
exp2 = re.compile("(?isu)<td[^>]*>(.*?)</td>")
#加入UA模拟浏览器
proxy_ua = {'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
proxyHtml = urllib2.Request(url="http://www.site-digger.com/html/articles/20110516/proxieslist.html",headers=proxy_ua)
try: #检查代理是否写入成功
    proxySocket = urllib2.urlopen(proxyHtml)
    htmlSource = proxySocket.read()
#print htmlSource
except Exception: #如果错误
    print '-'*50
    print '代理程序采集出错！请确认您的网络正常!'
    print '-'*50
    raw_input('按回车结束程序:')
else: #成功继续执行
    for row in exp1.findall(htmlSource):
       for col in exp2.findall(row)[:1]:
        #写入代理信息
        f.write(col+'\n')
        #print col
    f.close()


#针对http://cn-proxy.com/网站所写的一些采集后文件内操作
#删除指定字符
# with open('proxy_list.txt', 'r') as f:
#     with open('proxy_list.txt.new', 'w') as g:
#         for line in f.readlines():
#             if '服务器地址' not in line:
#                 g.write(line)
# shutil.move('proxy_list.txt.new', 'proxy_list.txt')
# #删除指定字符
# with open('proxy_list.txt', 'r') as f:
#     with open('proxy_list.txt.new', 'w') as g:
#         for line in f.readlines():
#             if '端口' not in line:
#                 g.write(line)
# shutil.move('proxy_list.txt.new', 'proxy_list.txt')
#
# #读取文件合并行
# file = open("proxy_list.txt",'r')
# lines = file.readlines() #列出文件所有行
# newlines = [] #新行
# j = 1
# for i in range(len(lines)):
#     if(j!=len(lines)-2):
#         string = lines[j].replace('\n','')+':'+lines[j+1].replace('\n','')
#         newlines.append(string)
#         j=j+2

#print(newlines)

# open("proxy_list.txt","w").write('%s' % '\n'.join(newlines))
# file.close()

print '*'*20+u'代理采集完成'+'*'*20
##########################################################################################3
### 代理模块(全局代理)
print '#'*50
print '#'*2 + u'\t\t\t\t肾虚公子 亲情制作\t\t\t\t\t'+'#'*2
print '#'*2 + u'\t\t\t\t主页: Douban.miaowu.asia\t\t\t'+'#'*2
print '#'*50
print u'说明:本程序可以采集豆瓣任何小组的图片.'
print u'说明:采集的图片在文件夹Doubanimg内.'
print u'注意:代理没有验证，如果不成功请重新运行.'
print '#'*50

#读取代理文件的每一行
f0=open('proxy_list.txt','r')
dat0=f0.readlines()
f0.close()
#随即选取代理文件的一行
proxy_SJ = random.choice(dat0)
#代理
#proxy_input = raw_input('请输入采集代理服务器:')
proxy_handler = urllib2.ProxyHandler({'http':'%s'%proxy_SJ})
opener = urllib2.build_opener(proxy_handler)
urllib2.install_opener(opener)

#采集本地路径全局变量
#img_LuJ = raw_input("图片下载路径:".decode('utf-8'))
#img_LuJ2 = os.path.abspath(img_LuJ)
print u'请输入小组代码,默认采集豆瓣害羞组[ID=haixiuzu]'
print u'小组ID就是(http://www.douban.com/group/这里的字符/)'
print u'请输入小组ID(默认按回车继续):',
Douban_group = raw_input('') or 'haixiuzu'
Douban_group_url = 'http://www.douban.com/group/'

#模块化输出
#获取帖子单页html
def gethtml2(url2):
    Douban_ua = {'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
    Douban_Html = urllib2.Request(url=(url2),headers=Douban_ua)
    Douban_Socket = urllib2.urlopen(Douban_Html)
    html2 = Douban_Socket.read().decode('utf-8')
    return  html2

#打开帖子列表
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
            time.sleep(0.5)
            i+=1
            print (imgurl)
    return download_img


print '-'*50
print u'请输入采集帖子数,默认采集10个帖子'
print u'输入数字即可(默认按回车继续):',
page_end = int(raw_input('')or 10)
print '-'*50
print u'正在采集图片中，程序可能用较长时间,此时您可以干点别的，比如喝杯咖啡？'
print '-'*50

num_end = page_end*25
num = 0
page_num = 1
try: #判断输出错误
    while num<=num_end:
        #获取帖子列表,从0页开始
        html2 = gethtml2(Douban_group_url+Douban_group+"/discussion?start=%d"%num)
        #抽取下载图片
        topicurl = gettoimg(html2)
        topic_page = gethtml2(topicurl)
        download_img=download(topic_page)
        num = page_num*25
        page_num+=1
    #print('程序采集完成')
except Exception:
    print u'错误：图片下载失败！请检查小组名称是否正确!!请重新运行本程序'
    print '-'*50
    print u'按回车结束程序:',
    raw_input('')
else:
    print '#'*20 + u'下载完成' + '#'*20
    print u'程序采集已经结束感谢您的使用!'+u'网站:http://Douban.miaowu.asia'
    print '#'*20 + u'程序结束' + '#'*20
    print u'按回车结束程序:',
    JS = raw_input('')
    print JS

