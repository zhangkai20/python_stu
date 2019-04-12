#!/usr/bin/python
#-*- coding:utf-8 -*-
# day1
#1.   Python的简介   面向对象
#   解释型
#   编译型
#   作什么？
#      安装    3.5版本以上
#               将Python的安装路径添加到环境变量里

#     手动将Python的安装路径添加到环境变量里
#  编辑器的安装  pycharm   sublime text

# day2 和 ay3

#2. 输入和输出   3.0版本以下   raw_input  print
#  变量名 = input('提示语')
#  print()

#3. 变量    定义变量   变量名的规则

# 4. 数据类型
# 字符串的函数   upper  swapcase  replace  split  format  strip
# 列表的函数    append   remove  pop  insert  sort  reverse copy
# 元组的函数    index   count
# 字典的函数    keys  values  items  pop  popitem  update
# 集合的函数    add  remove  pop  | 并集  & 交集  - 差集
# a = {123,415,6}
# b = {45,64,36,6}
# print(a-b)

#5. day4  运算符

# 算数运算符  +  -  *  /  //  %  **
# 赋值运算符  += -= *= ....
# 比较运算符  >  <  >=  <=  !=  ==
# 逻辑运算符  and   or  not
# 成员运算符  in   not in

#6.  条件控制语句    if  语句
# 格式   if 条件：  缩进  执行语句
# 单分支  双分支  多分支  嵌套判断

#7.  循环控制语句   for    while
#  格式：  for  变量名  in  范围:  缩进  执行语句
#   range()    enumerate()
#  格式：  while  条件：  缩进  执行语句
# for  else      while   else
#  break   continue

#8.  异常处理    try...except...
# try..except....except...
# try...except...else...
# try...except...finally...
# raise  触发异常

#9. 文件操作    open(文件名，权限，编码方式)

# 文件名的处理     r 或者  双 \
# 权限 ：      w, r, a    read   readlines  readline
#        w+  r+  a+    wb   rb  ab

#10. 函数   具有某种功能，可重复使用的代码块
# 格式:    def 函数名():  缩进  执行语句
# 1.变量的作用域 （局部变量，全局变量）  global
# 2. return   函数的返回值和结束
# 3. 参数    必须参数    默认参数   可变长参数  *args   **kwargs

# 格式： lambda  匿名函数  表达式
#   变量名 = lambda 参数名 : 表达式

#11.  列表推导式   将控制语句写在列表中，使产生的结果直接存在在列表中
#  格式  变量名 = [变量  控制语句]  结果的变量在最前面

# python 的内置函数    len  type  sum  max  min  hex

#12. 导入语句   import语句

# import  文件名
# # form 文件名  import 函数名
# # if __name__ == '__main__'
#
# # 安装模块   1.pip安装  2. pycharm安装  3.文件安装

# 上下文管理器   with语句
# 格式：  with 操作的对象  as  变量名： 缩进 执行语句
#  with语句的机制，能够自动释放资源
# __enter__   __exit__

#13. 模块的使用
# random  产生随机数
# a = random.randint(10,100)

# copy  复制
# 浅复制  b = copy.copy(a)
# 深复制  b = copy.deepcopy(a)

# xlwt       excel表格的写入
# xlrd       excel表格的读取
# xlutils    excel表格的追加

# re  正则表达式    筛选数据

# os  与操作系统的交互









