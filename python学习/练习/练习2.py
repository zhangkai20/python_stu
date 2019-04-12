#!/usr/bin/python
#-*- coding:utf-8 -*-


#三角形判断
# def sanjiaoxing():
#     abc = input('输入数字，以逗号隔开')
#     abc = abc.split(',')
#     abc = [int(abc[0]),int(abc[1]),int(abc[2])]
#     abc.sort()
#     if abc[0]+abc[1]>abc[2]:
#         if abc[0]**2+abc[1]**2>abc[2]**2:
#             print('锐角三角形')
#         elif abc[0]**2+abc[1]**2<abc[2]**2:
#             print('钝角三角形')
#         else:
#             print('直角三角形')
#     else:
#         print('不能构成三角形')

#水仙花数
# def shuixianhua():
#     for i in range(100,1000):
#         i=str(i)
#         a=int(i[0])
#         b=int(i[1])
#         c=int(i[-1])
#         if a**3+b**3+c**3 ==int(i):
#             print(int(i))

# for i in range(100,1000):
#     a=i//100
#     b=i//10%10
#     c=i%10
#     if a**3+b**3+c**3==i:
#         print(i)

# 九九乘法表
# def jiujiu():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print('{}*{}={}'.format(i,j,i*j),end='\t')
#         print()


#回文字符串
# def huiwen():
#     a=input('输入内容')
#     b=len(a)//2
#     for i in range(b):
#         c=-1-i
#         if a[i]!=a[c]:
#             print('不是回文字符串')
#             break
#     else:
#         print('是回文字符串')

#质数之和
# def zishu():
#     x=2
#     for i in range(3,101,2):
#         for j in range(2,i+1):
#             if i%j == 0:
#                 break
#         if i == j:
#             x=x+i
#     return x
