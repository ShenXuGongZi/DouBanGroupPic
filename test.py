# -*- coding: utf-8 -*-   
from threading import Thread    
def run_thread(n):    
        for i in range(n):    
            print i    
    
t1 = Thread(target=run_thread,args=(500000,))#指定目标函数，传入参数，这里参数也是元组
t1.start()  #启动线程  