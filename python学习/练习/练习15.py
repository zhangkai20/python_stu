#!/usr/bin/python
#-*- coding:utf-8 -*-

import xlrd
import pymysql
#   连接数据库
# lj = pymysql.connect(host='192.168.0.89',   #主机ip地址
#                       port=3306,    #数据库端口号
#                       user='root',  #用户
#                       password='123456',    #数据库密码
#                       charset='utf8')   #编码方式
# #   创建游标(控制器)
# yb = lj.cursor()
# #   执行sql语句
# yb.execute('use py;')
# # yb.execute('insert into biao values("xiaogang","20","boy"),("xiaohong","31","girl");')
# #   提交  对数据库数据进行更改的时候
# #   是由连接数据库的变量来提交，不是由游标的变量来提交
# # lj.commit()
# yb.execute('select * from biao;')
# #   任何结果都需要有变量来接收
# # print(yb.fetchall())   #只接受上一个SQL语句执行的结果
# # print(yb.fetchmany())      #接收上一个sql语句的结果，默认只接收第一行，在括号里写入数字几就接收多少行
# print(yb.fetchone())    #接收上一个sql语句的结果,每次只接受一行，本身具有迭代的功能
# print(yb.fetchone())
# #   断开数据库
# lj.close()


# gb=lj.cursor()
# while True:
#     a=input('输入SQL语句')
#     try:
#         if a == 'exit':
#             break
#         else:
#             gb.execute(a)
#             print(gb.fetchall())
#     except:
#         continue
# lj.close()


# lj = pymysql.connect(host='192.168.0.89',
#                       port=3306,
#                       user='root',
#                       password='123456',
#                       charset='utf8')
# guangbi = lj.cursor()
# guangbi.execute('use py;')
# f = xlrd.open_workbook('douban.xls')
# sheet = f.sheets()[0]
# a=sheet.nrows
# b=sheet.ncols
# k=''
# lb=[]
# for i in range(b):
#     j = sheet.cell(0,i).value
#     lb.append(j)
# for i in lb:
#     if i != lb[-1]:
#         z=('{} char(50),').format(i)
#     else:
#         z = ('{} char(50)').format(i)
#     k=k+z
# guangbi.execute('create table douban({});'.format(k))
# for i in range(1,a):
#     kb=[]
#     kzf=''
#     for j in range(b):
#         x = sheet.cell(i,j).value
#         kb.append(x)
#     for k in kb:
#         if k != kb[-1]:
#             kzf = (kzf+'"{}"'+',').format(k)
#         else:
#             kzf = (kzf+'"{}"').format(k)
#     guangbi.execute('insert into douban values({});'.format(kzf))
#     lj.commit()
# lj.close()

