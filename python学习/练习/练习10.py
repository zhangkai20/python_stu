#!/usr/bin/python
#-*- coding:utf-8 -*-

import os
import re
# d=os.getcwd()
# d=os.listdir()
# os.rename('1','2')
# os.chdir(r'd:\programs')
# d=os.getcwd()
# print(d)
# os.makedirs(r'..\aa\bb')
# os.remove('..\wj.xls')
# os.mkdir('aa')
# os.rmdir('aa')

# ad =os.popen('calc')
# print(ad.read())

# a=os.path.split(r'C:/Users/zk/Desktop/python学习/练习/练习10.py')
# print(a)

# a=os.path.splitext(r'C:/Users/zk/Desktop/python学习/练习/练习10.py')
# print(a)
# d=[i for i in os.listdir() if os.path.splitext(i)[1] == '.py']
# print(d)

# for i in range(10):
#     os.mkdir('user{}'.format(i+1))

# for i in range(10):
#     os.rmdir('user{}'.format(i+1))

# m='Rrqexxdrbadg'
# b=re.compile('r.*d')
# b=re.compile('r(.*)d')
# c=b.findall(m)
# c=re.sub('[^\d]+','23',m)
# b=re.compile('r.*?d',re.S)
# c=b.findall(m)
# b=re.compile('r.*?d',re.I)
# c=b.findall(m)

# x=[]
# with open('c.txt','r',encoding='utf-8') as f:
#     d=f.readlines()
# for i in d:
#     b=re.compile('^(138\d{8}|151\d{8})$')
#     c=b.findall(i)
#     if c != []:
#         x.append(c)
# print(x)

# x=[]
# with open('c.txt','r',encoding='utf-8') as f:
#     d=f.readlines()
# for i in d:
#     b=re.compile('^\d+\.\d+\.\d+\.\d+$')
#     c = b.findall(i)
#     if c != []:
#         x.append(c)
# print(x)

# x=[]
# with open('c.txt','r',encoding='utf-8') as f:
#     d=f.readlines()
# for i in d:
#     b=re.compile('^\d{17}[0-9Xx]$')
#     c = b.findall(i)
#     if c != []:
#         x.append(c)
# print(x)