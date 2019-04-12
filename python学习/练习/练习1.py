#!/usr/bin/python
#-*- coding:utf-8 -*-

#判断成绩
# def chengji():
# #     a=input('分数')
# #     a=float(a)
# #     if a>90 and a<=100 :
# #         print('优秀')
# #     elif a<=90 and a>80 :
# #         print('良好')
# #     elif a<=80 and a>70 :
# #         print('一般')
# #     elif a<=70 and a>60 :
# #         print('及格')
# #     else:
# #         print('不及格')

#判断文件
# a=input("输入内容")
# if  a.startswith('a'):
#     if a.endswith('c') :
#       print('hello world')
#     else :
#       print('hello')
# elif a.endswith('c') :
#     print('world')
# else :
#     print('123')

#加
# a=0
# for i in  range(1,101):
#     a=i+a
# print(a)


#100以内奇数之和减偶数之和
# b=0
# for i in range(1,100,2):
#     b=b+i
# for i in range(2,100,2):
#     b=b-i
# print(b)

# b=0
# for i in range(1,100):
#     if i%2==0:
#         b=b-i
#     else:
#         b=b+i
# print(b)


#判断
# for a in ['ac','Asd','sdc','Ac','Adaw','cs','ca','acc','abd']:
#     if a.startswith('a') or a.startswith('A'):
#         if a.endswith('c'):
#             print(a)

#猜数字
# import random
# a = random.randint(1,10)
# #从1-10随机选中一个数，赋值给a
# for i in range(0,3):
#     s=input("请输入数字")
#     s=int(s)
#     if s < a :
#         print('小了')
#     elif s > a :
#         print('大了')
#     else :
#         print('恭喜中奖')
#         break
# else:
#     print('失败')
