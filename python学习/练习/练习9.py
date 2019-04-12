#!/usr/bin/python
# -*- coding:utf-8 -*-


import xlwt
from xlutils.copy import copy
import xlrd
# def yui(x):
#     f = open(x,'r',encoding='utf-8')
#     d = f.readlines()
#     f.close()
#     w = [i for i in d if '#' in i]
#     return w
# print(yui('a.txt'))

# for i in range(3):
#     j=3-i
#     print(' '*i,end='')
#     print('* '*j)

# import xlwt
# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('excel学习')
# for i in range(1,10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,'{}*{}={}'.format(i,j,i*j))
# f.save('xuexi.xls')


# with open('a.txt','r',encoding='utf-8') as f:
#     d = f.readlines()
# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('xu')
# for i,j in enumerate(d):
#     j = j.replace('\n','').split(',')
#     for k in range(len(j)):
#         sheet.write(i,k,j[k])
# f.save('wj.xls')


# with xlrd.open_workbook('xuexi.xls') as f:
#     print(f.nsheets)
#     sheet = f.sheets()[0]
    # new_sheet = f.sheet_by_name('excel学习')
    # print(sheet.nrows)
    # print(sheet.row_values(0))
    # print(sheet.ncols)
    # print(sheet.col_values(6))
    # print(sheet.cell(8,4).value)

# f = xlrd.open_workbook('xuexi.xls')
# sheet= f.sheets()[0]
# hang=sheet.nrows
# new_f = copy(f)
# sheet = new_f.get_sheet(0)
# for i in range(1,10):
#     for j in range(1,i+1):
#         sheet.write(hang+i-1,j-1,'{}*{}={}'.format(i,j,i*j))
# new_f.save('xuexi.xls')


# with open('a.txt','r',encoding='utf-8') as f:
#     d=f.readlines()
# with open('b.txt','r',encoding='utf-8') as f:
#     b=f.readlines()
# with open('d.txt','r',encoding='utf-8') as f:
#     c=f.readlines()
# x=d+b+c
# f=xlwt.Workbook('hebing.xls')
# sheet = f.add_sheet('he')
# for i,j in enumerate(x):
#     j=j.replace('\n','').split(',')
#     for k in range(len(j)):
#         sheet.write(i,k,j[k])
# f.save('hebing.xls')
#
# with open('c.txt','r',encoding='utf-8') as f:
#     d=f.readlines()
# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('hb')
# for i,j in enumerate(d):
#     j = j.replace('\n','').split(',')
#     for k in range(len(j)):
#         sheet.write(i,k,j[k])
# f.save('hb2.xls')

# with open('d.txt','r',encoding='utf-8') as f:
#     dd=f.readlines()
# f = xlrd.open_workbook('hb2.xls')
# sheet=f.sheets()[0]
# hang=sheet.nrows
# nf=copy(f)
# sheet =  nf.get_sheet(0)
# for x,y in enumerate(dd):
#     xx=y.replace('\n','').split(',')
#     for j in range(len(xx)):
#         sheet.write(hang+x,j,xx[j])
# nf.save('hb2.xls')
#
f = xlrd.open_workbook('hebing.xls')
sheet = f.sheets()[0]
hang=sheet.nrows
with open('c.txt','w',encoding='utf-8') as c:
    for j in range(hang):
        i = sheet.row_values(j)
        if i[-1] =='':
            i.pop(-1)
        for k in i:
            if k != i[-1]:
                c.write(k+',')
            else:
                c.write(k+'\n')
        if j == hang-1:
            c.write(k)