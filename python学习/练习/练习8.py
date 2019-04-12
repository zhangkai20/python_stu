# !/usr/bin/python
# -*- coding:utf-8 -*-

# def shiliu(b):
#     a=[str(i) for i in range(10) ]+[i for i in 'abcdef']
#     c=[]
#     while True:
#         b,s=divmod(b,16)
#         c.append(a[s])
#         if b ==0:
#             break
#     c=c[::-1]
#     m=c[0]
#     for i in c[1::]:
#         m += i
#     return m

# def im(x):
#     return x
# print(im('10'))

# def xuanzhe(x):
#     a=len(x)
#     for i in range(0,a):
#         for j in range(i+1,a):
#             if x[i] > x[j]:
#                 x[i],x[j] = x[j],x[i]
#     return x

# def fl(x):
#     b=x.copy()
#     c=[]
#     for i in b:
#        if int(i) not in c:
#            c.append(int(i))
#     c.sort()
#     d=[s for s in x  if s == c[-1]]
#     f=[w for w in x if w == c[-2]]
#     return d,f


# def jiecheng(x,y):
#     a=0
#     b=1
#     for i in range(x,y+1):
#         b=b*i
#         a=a+b
#     return a

# a='dsdad'
# b='-'
# print(b.join(a))