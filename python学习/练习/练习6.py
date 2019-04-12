#!/usr/bin/python
#-*- coding:utf-8 -*-

# s=2
# for i in range(3,100,2):
#     for j in range(2,i):
#         if i % j ==0:
#             break
#     else:
#         s=s+i
# print(s)

# a=input('输入数字')
# b=a.split(',')
# c,d,f=[],[],[]
# for i in b:
#     if int(i) not in c:
#         c.append(int(i))
# c.sort()
# for i in b:
#     if int(i) == c[-1]:
#         d.append(int(i))
#     elif int(i) == c[-2]:
#         f.append(int(i))
# print('第一大元素',d,'第二大元素',f)

# b=[2,6,5,4,1]
# a=b.copy()
# a.sort()
# for i in b:
#     if i == a[0]:
#         b.remove(i)
#         b.append(i)
#     elif i == a[-1]:
#         b.remove(i)
#         b.insert(0,i)
# print(b)

# f=open(r'c:\Users\zk\Desktop\z.txt','w',encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,i+1):
#             f.write('{}*{}={}\t'.format(i,j,i*j))
#     f.write('\n')
# f.close()


# f=open('a.txt','r',encoding='utf-8')
# x=f.readlines()
#f.close
# a=len(x)
# for i in x:
#     if i == '\n':
#         a -= 1
#     elif i[0] == '#':
#         a -=1
# print(a)


# f=open('1.png','rb')
# a=f.read()
# print(a)
# f.close()
#
# d=open('2.png','wb')
# d.write(a)
# d.close()


# def abx():
#     a = 31
#     return a+10


# def tongji():
#     f=open(r'c:\Users\zk\Desktop\z.txt','r',encoding='utf-8')
#     x=f.readlines()
#     b=len(x)
#     return b