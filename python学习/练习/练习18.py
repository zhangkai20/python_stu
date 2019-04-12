#!/usr/bin/python
# -*- coding=utf-8 -*-

import time
import pymysql
import xlwt
# def shijian(x):
#     a=time.strptime(x,'%Y-%m-%d')
#     b=time.mktime(a)
#     c=b-86400
#     abc=time.localtime(c)
#     d=time.strftime('%Y-%m-%d',abc)
#     print(d)
# shijian('2018-1-1')

def ku():
    shujuku=pymysql.connect(host='192.168.0.60',port=3306,user='root',password='123456',charset='utf8')
    gb=shujuku.cursor()
    gb.execute('use py;')
    gb.execute('select * from douban;')
    a=gb.fetchall()
    gb.execute('desc douban')
    b=gb.fetchall()
    shujuku.close()
    with open('a.txt','w',encoding='utf-8') as f:
        for k in b:
            if k != b[-1]:
                f.write(k[0]+',')
            else:
                f.write(k[0]+'\n')
        for i in a:
            for j in range(len(i)):
                if i[j] != i[-1]:
                    f.write(i[j]+',')
                else:
                    f.write(i[j]+'\n')

def bk():
    ku=pymysql.connect(host='192.168.0.60',port=3306,user='root',password='123456',charset='utf8')
    gb=ku.cursor()
    gb.execute('use py;')
    gb.execute('select * from douban')
    a=gb.fetchall()
    gb.execute('desc douban;')
    b=gb.fetchall()
    f=xlwt.Workbook()
    sheet=f.add_sheet('db')
    for i in range(len(b)):
        sheet.write(0,i,b[i][0])
    for i in range(len(a)):
        for j in range(len(a[i])):
                sheet.write(i+1,j,a[i][j])
    f.save('1.xls')
