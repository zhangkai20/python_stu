#!/usr/bin/python
#-*- coding:utf-8 -*-

# c=[]
# for i in range(2,100):
#     for j in range(2,i+1):
#         if i % j == 0:
#             break
#     if i == j:
#             c.append(i)
# for i in range(6,101,2):
#     for j in range(len(c)):
#         for k in range(j+1,len(c)):
#             if c[k]+c[j] == i:
#                 print('{}={}+{}'.format(i,c[j],c[k]))
#                 break

# class sdw:
#     def w3(self):
#         self.sd()
#         print('dss')
#     def sd(self):
#         self.__w2()
#         print('www')
#     def __w2(self):
#         print('222')
# class ns():
#     def w3(self):
#         print('333')
# class es(sdw,ns):
#     def w3(self):
#         print('123')
# class ss(sdw,ns):
#     pass

# class xm:
#     xxm = 111#可以不写
#     def __init__(self,x):
#         self.xxm=x
#     def masd(self):
#         print(self.xxm)
# a=xm(5)
# a.masd()

# 定义一个函数，接受三个参数，分别为字符串s、数值a1、数值a2，将字符串s从下标a1开始的a2个字符删除，并把结果返回。a2默认值为0

# def shanchu(a,b,c=0):
#     d = list(a)
#     try:
#         for i in range(c):
#             d.pop(b)
#     except:
#         for i in range(len(d[b:])):
#             d.pop(-1)
#     a =''.join(d)
#     return a
# s=shanchu('svnsarshsfa',3,10)
# print(s)

import os
# i=os.listdir()
# x=[]
# for k in i:
#     n = os.path.splitext(k)
#     x.append(n)
# c=[i[x.index(j)] for j in x if '.py' == j[1]]
# print(c)

# for i in range(10):
#     os.mkdir('{}'.format(i+1))
#     with open(r'{}\a.txt'.format(i+1),'w',encoding='utf-8') as f:
#         f.write('qw')

# import requests
# import re
#
# class wm_Ss(object):
#
#     def qingqiu(self,yeshu):
#         wangzhi = 'https://www.32us.com/html/0/90/977{}.html'.format(yeshu)
#         head = {
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.6.0.18627'
#         }
#         xiangying = requests.get(url=wangzhi,headers=head)
#         duqu = xiangying.content.decode('gbk')
#         return duqu
#
#     def guolv(self,abc):
#         shuju = []
#         ooo = re.compile(r'<dd id="contents">(.*?)</dd>',re.S)
#         items = ooo.findall(abc)
#         for i in items:
#             i = i.replace('<dd id="contents">','').replace('</dd>','').strip()
#             shuju.append(i)
#         return shuju
#     def save(self,qwe):
#         with open('o.py','a',encoding='utf-8') as f:
#             for i in qwe:
#                 f.write(i+'\n')
#
#
# qiu = wm_Ss()
# duqu = qiu.qingqiu(yeshu=1)
# shuju = qiu.guolv(abc=duqu)
# qiu.save(shuju)
