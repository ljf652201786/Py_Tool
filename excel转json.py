#!/usr/bin/python3
# -*- coding:utf-8 -*-

import json
import tablib
import os

# json.text文件的格式： [{"authenticate":-99,"last_ip":"156.2.98.429","last_time":"2020/05/23 01:41:36","member_id":5067002,"mg_id":1,"name":"yuanfang","status":0,"username":"L7898"},{"authenticate":-99,"last_ip":"156.2.98.421","last_time":"2020/05/20 14:16:02","member_id":1012304,"mg_id":1,"name":"管理员","status":0,"username":"aaaap"},{"authenticate":-99,"last_ip":"134.212.156.178","last_time":"2020/04/20 14:16:03","member_id":1012305,"mg_id":1,"name":"lily","status":0,"username":"aaaaa8"}]
# 获取json数据

path = os.getcwd()

with open(path+'/json.txt', 'r',encoding='utf-8',errors='ignore') as f:
    rows = json.load(f)
# 将json中的key作为header, 也可以自定义header（列名）
header=tuple([ i for i in rows[0].keys()])
data = []
# 循环里面的字典，将value作为数据写入进去
for row in rows:
    body = []
    for v in row.values():
        body.append(v)
    data.append(tuple(body))
#将含标题和内容的数据放到data里
data = tablib.Dataset(*data,headers=header)

open(path+'/data.xls', 'wb').write(data.xls)
