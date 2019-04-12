# #!/usr/bin/python
# #-*- coding:utf-8 -*-

# def sangpin():
#     for i, j in enumerate(b):
#         print(i+1,j,a[j])
# x=int(input('输入金额'))
# a={'电脑':1999,'鼠标':10,'耳机':20,'键盘':998}
# b=list(a)
# m=[]
# # 显示商品序号、商品名、价钱
# sangpin()
# # 向购物车中添加，删除商品
# while True:
#     try:
#         c=input('输入序号添加购物车,exit退出,负序号删除商品')
#         if c == 'exit':
#             break
#         elif c[0]=='-':
#             m.remove(b[int(c[1:])-1])
#             print(m)
#         else:
#             m.append(b[int(c)-1])
#             print(m)
#     except:
#         print('错误,请重新输入')
# c = input('结账 yes or no')
# # 结账和充值
# if c == 'yes':
#     s=0
#     for i in m:
#         s=s+a[i]
#     while s > x:
#         print('余额不足')
#         print('共花费{},当前余额{},应补足{}'.format(s,x,s-x))
#         c = input('是否充值,yes or no')
#         try:
#             if c == 'yes':
#                 f=int(input('输入金额'))
#                 x=x+f
#             elif c=='no':
#                 t = input('是否删除商品 yes or no')
#                 if t == 'yes':
#                     sangpin()
#                     print(m)
#                     t = int(input('输入删除的商品号'))
#                     m.remove(b[int(t) - 1])
#                     print(m)
#                     s=s-a[b[int(t)-1]]
#                 else:
#                     break
#         except:
#             print('输入错误')
#     if s > x:
#         print('购买失败')
#     else:
#         x=x-s
#         print('购买成功')
#         print('剩余金额：',x)