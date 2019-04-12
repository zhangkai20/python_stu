#!/usr/bin/python
#-*- coding:utf-8 -*-

#一

# def huiwen(zifu):
#     for i in range(len(zifu)//2):
#         if zifu[i] != zifu[-1-i]:
#             print('不是回文字符')
#             break
#     else:
#         print('是回文字符')

#二

# def function(a,b,c):
#     d=[a,b,c]
#     d.sort()
#     if d[0]+d[1] > d[2]:
#         if d[0] ** 2 +d[1] ** 2 > d[2] ** 2:
#             print('锐角三角形')
#         elif d[0]**2+d[1]**2<d[2]**2:
#             print('钝角三角形')
#         else:
#             print('直角三角形')
#     else:
#         print('不能构成三角形')

#三


#四

# for i in range(1,50):
#     for j in range(1,100):
#         for k in range(1,100):
#             if 2*i+j+0.5*k==100:
#                 if i+j+k==100:
#                     print(i,j,k)

#五

# c=[]
# for i in [1,2,3,4,3,5,2]:
#     if i not in c:
#         c.append(i)
# print(c)

#六


#七


#八

# def chuancan(a,b):
#     for i in range(len(a)):
#         for j in range(i+1,len(a)):
#             if a[i]+a[j] == b:
#                  print(a[i],a[j])
# chuancan([1,2,3,4,5,6,7],7)

#九

import xlwt
import xlrd
import xlutils

# f=xlrd.open_workbook('练习.xls')
# sheet=f.sheets()[0]
# with open('a.txt','w',encoding='utf-8') as e:
#     for i in range(sheet.nrows):
#         i = sheet.row_values(i)
#         for j in i:
#             if j == i[-1]:
#                 e.write(j+'\n')
#             else:
#                 e.write(j+',')

#十

# with open('c.txt','r',encoding='utf-8') as f:
#     d=f.readlines()
# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('hb')
# for i,j in enumerate(d):
#     j = j.replace('\n','').split(',')
#     for k in range(len(j)):
#         sheet.write(i,k,j[k])
# f.save('hb2.xls')

#十一

# def dayin(a):
#     c=[]
#     for i in a:
#         if i not in c:
#             c.append(i)
#     c.sort()
#     for i in a:
#         if i == c[-1]:
#             print('第一大{}'.format(i))
#         elif i == c[-2]:
#             print('第二大{}'.format(i))

#十二
# def zhengshu(a):
#     c=0
#     a=list(a)
#     a.reverse()
#     for i,j in enumerate(a):
#         for k in range(10):
#             if j == str(k):
#                 c =c+k*(10**i)
#     return c
# print(zhengshu('12'))

#十三
# def jinzhi(a):
#     jihe=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
#     kong=[]
#     while True:
#         yv=a%16
#         kong.append(jihe[yv])
#         a=a//16
#         if a == 0:
#             break
#     kong.reverse()
#     m=kong[0]
#     for i in kong[1:]:
#         m = m+i
#     return m
# print(jinzhi(100))

#十四
