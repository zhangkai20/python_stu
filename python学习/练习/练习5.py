#!/usr/bin/python
#-*- coding:utf-8 -*-

# a=input('输入内容')
# s=a.split(',')
# t=s[0]
# s.pop(0)
# s.append(t)
# print(s)

# l=[]
# d=[]
# a=input('输入数字')
# s=a.split(',')
# for i in  s:
#     for j in s:
#         for k in s:
#             m=i+j+k
#             l.append(m)
# for x in l:
#     if x not in d:
#         d.append(x)
# print(d)


# a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# sa=int(input('输入十进制数字'))
# lc=[]
# while True:
#     ib = sa % 16
#     sa=sa // 16
#     lc.append(a[ib])
#     if sa == 0:
#         break
# lc.reverse()
# m=lc[0]
# for l in lc[1::]:
#     m=m+l
# # m=''.join(lc)
# print(m)



# a=[1,2,3,4]
# b=int(input('输入数字'))
# a.append(b)
# l=len(a)
# for i in range(l):
#     if a[-1] < a[i]:
#         a.pop(-1)
#         a.insert(i,b)
#         break
# print(a)
