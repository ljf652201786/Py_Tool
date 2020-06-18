'''
Created on 2019年1月29日
@author:  Yvon_fajin
'''
import os ,os.path ,time
import datetime
from threading import Thread
import math
import threading
# 创建锁对象
lock = threading.Lock()

def rename(keyword):
    ''' file: 文件路径    keyWord: 需要修改的文件中所包含的关键字 '''
    #start =time.clock()
    # 取到锁 可以执行
    lock.acquire()
    os.chdir(file)
    items = os.listdir(file)

    # 线程列表
    thread_list = []
    #设置线程数
    times_num = 100
    # 每个线程处理的数据大小
    split_count = math.ceil(len(items) / times_num)
    count = 0
    for item in range(times_num):
        _list = items[count: count + split_count]
        # 线程相关处理
        thread = Thread(target=thread_execute_rename, args=(_list,keyword,))
        thread_list.append(thread)
        # 在子线程中运行任务
        thread.start()
        count += split_count

    # 线程同步，等待子线程结束任务，主线程再结束
    for _item in thread_list:
        _item.join()

    #释放锁
    lock.release()


def thread_execute_rename(items,keyword):
    for name in items :
        print(name)
        # 遍历所有文件
        #判断对象是否为一个目录
        if not os.path.isdir(name):
            #文件名中包含keyword 替换为空
            # if keyword in name :
            #     new_name = name.replace(keyword,'')
            #     os.renames(name,new_name)
            #文件名中拼接keyword
            new_name = keyword+name
            os.renames(name,new_name)
            pass
        else:
            rename(file + '\\' + name, keyword)
            os.chdir('...')
    print('-----------------------分界线------------------------')
    items = os.listdir(file)
    for name in items:
        print(name)

file = 'C:\\Users\\ljf\\Desktop\\PY\\data\\linjingfeng'
begin = datetime.datetime.now()
rename('林靖峰_')
end = datetime.datetime.now()
total_time = end - begin
print ('执行时间： ',total_time)
