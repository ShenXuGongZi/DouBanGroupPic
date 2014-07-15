#coding:utf-8
import os

Douban_group = raw_input('请输入小组代码:(默认害羞组)[haixiuzu]:')or 'haixiuzu'
Douban_group_url = 'http://www.douban.com/group/'
print (Douban_group_url+Douban_group+"/discussion?start=%d"%5)