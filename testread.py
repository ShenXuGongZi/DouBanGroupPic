#-*- coding: utf-8 -*
#读取文件
file = open("proxy_list.txt",'r')
lines = file.readlines() #列出文件所有行
newlines = [] #新行
j = 1
for i in range(len(lines)):
    if(j!=len(lines)-2):
        string = lines[j].replace('\n','')+':'+lines[j+1].replace('\n','')
        newlines.append(string)
        j=j+2

print(newlines)


open("proxy_list.txt","w").write('%s' % '\n'.join(newlines))
file.close()



#随即读取
'''
f0=file('proxy_list.txt','r')
dat0=f0.readlines()
f0.close()
a = random.choice(dat0)

print a
'''