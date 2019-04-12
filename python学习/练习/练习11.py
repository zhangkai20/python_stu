#!/bin/python
#-*- coding:utf-8 -*-

import xlrd
import xlwt
import xlutils
import os
import re
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('练习')
# for i in range(1,10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,'{}*{}={}'.format(i,j,i*j))
# f.save('99.xls')

# f=xlrd.open_workbook('99.xls')
# sheet=f.sheets()[0]
# a=sheet.cell(7,7).value
# print(a)

# from xlutils.copy import copy
# f=xlrd.open_workbook('99.xls')
# d=copy(f)
# sheet=d.get_sheet(0)
# sheet.write(9,9,'eadade')
# d.save('99.xls')

# p=os.popen('ipconfig')
# print(p.read())
# w=os.path.split(r'c:/sd/ff/s')
# print(w)

# a='sqeadvadq\nsbslggsperenc'
# b=re.compile('d(.*?)g',re.S)
# c=b.findall(a)
# print(c)fxxc

# def wenjian(a):
# 	s=os.listdir(a)
# 	d=0
# 	f=0
# 	for i in s:
# 		if '.' in i:
# 			d +=1
# 		else:
# 			f +=1
# 	return d,f
# print(wenjian(r'C:\Users\zk\Desktop\python学习'))

# with open('a.txt','r',encoding='utf-8') as f:
# 	d = f.readlines()
# c=[]
# for i in d:
# 	if  i[-1] == '\n':
# 		i = i.replace('\n','')
# 		if i != '':
# 			c.append(i)
# print(c)

# with open(r'C:\Users\zk\Desktop\a.png','rb') as f:
# 	d=f.read()
# with open('c.png','wb') as f:
# 	f.write(d)

# def jinzhi(x):
# 	a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# 	c=[]
# 	while True:
# 		i=x%16
# 		c.append(a[i])
# 		x=x//16
# 		if x == 0:
# 			break
# 	c.reverse()
# 	m=c[0]
# 	for i in c[1:]:
# 		m +=i
# 	return '0x'+m
# print(jinzhi(100))
