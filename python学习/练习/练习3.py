#!/usr/bin/python
#-*- coding:utf-8 -*-

# def foe():
#     while True:
#         yield None
# for i in foe():
#     print('yes')


# x=0
# i=1
# while i < 101:
#     x=i+x
#     i += 1
# print(x)


# while True:
#     a=input('输入数字')
#     if a[0] == '-':
#         break
#     else:
#         d=0
#         c = a.split(',')
#         b = len(c)
#         for i in c:
#             d=d+int(i)
#         print('平均分为：',d/b)
#         for j in c:
#             if int(j) <= d/b:
#                 print('低于平均分的是：',j)

#冒泡排序
# a=input('请输入数字，以逗号隔开')
# a=a.split(',')
# b=len(a)
# for i in range(b-1):
#     for j in range(b-1-i):
#         if int(a[j]) > int(a[j+1]):
#             a[j],a[j+1] = a[j+1],a[j]
# print(a)


# a=input('请输入数字，以逗号隔开')
# a=a.split(',')
# c=len(a)
# b=int(input('请输入数字'))
# for i in range(c):
#     for j in range(i+1,c):
#         if int(a[i]) + int(a[j]) == b :
#             print(a[i],a[j])

# from 练习6 import tongji
# print(tongji())