#-*- coding: utf-8 -*

import shutil
import re
import urllib

print '.'*20+'文件写入中'+'.'*20
#采集代理信息
f = open('proxy_list.txt','w')
exp1 = re.compile("(?isu)<tr[^>]*>(.*?)</tr>")
exp2 = re.compile("(?isu)<td[^>]*>(.*?)</td>")
htmlSource = urllib.urlopen("http://cn-proxy.com/").read()
for row in exp1.findall(htmlSource):
   for col in exp2.findall(row)[:2]:
    #写入代理信息
    f.write('\n'+col)

f.close()
#删除指定字符
with open('proxy_list.txt', 'r') as f:
    with open('proxy_list.txt.new', 'w') as g:
        for line in f.readlines():
            if '服务器地址' not in line:
                g.write(line)
shutil.move('proxy_list.txt.new', 'proxy_list.txt')
#删除指定字符
with open('proxy_list.txt', 'r') as f:
    with open('proxy_list.txt.new', 'w') as g:
        for line in f.readlines():
            if '端口' not in line:
                g.write(line)
shutil.move('proxy_list.txt.new', 'proxy_list.txt')

#读取文件合并行
file = open("proxy_list.txt",'r')
lines = file.readlines() #列出文件所有行
newlines = [] #新行
j = 1
for i in range(len(lines)):
    if(j!=len(lines)-2):
        string = lines[j].replace('\n','')+':'+lines[j+1].replace('\n','')
        newlines.append(string)
        j=j+2

#print(newlines)


open("proxy_list.txt","w").write('%s' % '\n'.join(newlines))
file.close()

print '#'*50
print '.'*20+'写入完成,请继续运行Start.bat'+'.'*20
