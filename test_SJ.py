import random

f0=file('proxy_list.txt','r')
dat0=f0.readlines()
f0.close()
a = random.choice(dat0)

print a