#!/usr/bin/python
#-*- coding:utf-8 -*-


# s=2
# for i in range(3,101,2):
#     for j in range(2,i+1):
#         if i%j == 0:
#             break
#     if i == j:
#         s = s+i
# print(s)

# a=input('输入内容，以逗号隔开')
# a=a.split(',')
# c=[]
# for i in a:
#     if i not in c:
#         c.append(i)
# print(c)


# a=input('输入内容，以逗号隔开')
# la=a.split(',')
# lb=la.copy()
# lb.sort()
# lc=[]
# ld=[]
# for i in lb:
#     if i == lb[-1]:
#         lc.append(i)
# print('第一大元素为：',lc)
# for j in lc:
#     if j == lb[-1]:
#         lb.remove(j)
# for k in lb:
#     if k == lb[-1]:
#         ld.append(k)
# print('第二大元素为：',ld)


# a=int(input('输入数字'))
# ib=1
# ic=0
# for i in range(1,a+1):
#     ib=ib*i
#     ic=ic+ib
# print(ic)


# for i in range(1,1000):
#     s = 0
#     for j in range(1,i):
#         if i % j == 0:
#             s=s+j
#     if s == i:
#         print(i)


# a = input('输入数字')
# x=0
# s=a[::-1]
# for i,j in enumerate(s):
#     for k in range(10):
#         if j == str(k):
#             x=x+k*(10**i)
# print(x)

# a=input('数字')
# a=a.split(',')
# b=len(a)
# for i in range(b):
#     for j in range(i+1,b):
#         if int(a[i]) > int(a[j]):
#             a[i] ,a[j] = a[j],a[i]
# print(a)