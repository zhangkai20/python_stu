#! /usr/bin/python
# -*- coding: utf-8 -*-

#   邮件
import smtplib
import email.mime.multipart
import email.mime.text

# fuwuqi = 'smtp.163.com' #   邮件服务器
# fasongzhe = '15139513258@163.com'   #   发件人
# shoujianren = '915389557@qq.com'   #   收件人
# shouquanma = 'qqq1389954'   #   授权码 允许登录客户端的密码(不是账号密码)
#
# #   创建一个空邮件
# youjian=email.mime.multipart.MIMEMultipart()
# youjian['From'] = fasongzhe #   邮件的发件人
# youjian['To'] = shoujianren #   邮件的接收者
# youjian['Subject'] = 'hao'  #   邮件主题
#   文件内容
# text = """
# hao
# """
# #   对正文进行编码
# text=email.mime.text.MIMEText(text,'plain','utf-8')
# #   将正文添加到邮件中
# youjian.attach(text)
# #   带附件的
# ##  对附近进行读取和编码
# fujian =email.mime.text.MIMEText(open('1.jpg','rb').read(),'base64','utf-8')
# ##  给附件添加头部信息
# fujian["Content-Type"] = 'application/octet-stream'
# fujian["Content-Disposition"] = 'attachment;filename="1.jpg"'
# ##  将附件添加到邮件里
# youjian.attach(fujian)
# #   登录服务器
# smtp=smtplib.SMTP_SSL(fuwuqi,465)
# #   登录服务器
# smtp.login(fasongzhe,shouquanma)
# #   发送邮件
# smtp.sendmail(fasongzhe,shoujianren,youjian.as_string())
# #   断开连接
# smtp.close()

#   socket
import socket
import time
# #   通过TCP协议进行通信
# #   服务器端
# #   创建一个套接字，规定使用TCP协议，ip的版本ipv4
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #   绑定ip、端口号。bind接收的是一个元组
# s.bind(('127.0.0.1',8888))
# #   监听服务是否开启，数字指的是最大等待数
# s.listen(3)
# while True:
#     #   接收请求    第一个：连接信息    第二个：客户端的ip和端口号
#     conn,addr=s.accept()
#     #   接收数据    1024表示一次性最大能接收1024字节数据
#     reg=conn.recv(1024)
#     print(reg.decode('utf-8'))
#     #   发送数据
#     a = input('>>>>')
#     conn.send(a.encode('utf-8'))
#     if a == 'exit':
#         break

#   通过udp协议进行通信
#   服务器端
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #   绑定主机
# s.bind(('127.0.0.1',8888))
# while True:
#     #   第一个变量：客户端发送的请求数据    第二个变量：客户端的ip和端口号
#     conn,addr = s.recvfrom(1024)
#     #   打印接收的数据
#     print(conn.decode('utf-8'))
#     #   发送响应
#     a = input('>>>>')
#     if a != 'exit':
#         s.sendto(a.encode('utf-8'),addr)  # addr为客户端的ip和端口号
#     else:
#         break


# #   客户端(TCP)
# ns = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #   连接服务器
# ns.connect(('127.0.0.1', 8888))
# while True:
# #   发送请求
#     a=input('>>>>>')
#     if a != 'exit':
#       ns.send(a.encode('utf-8'))
# #   接收数据
#       msg=ns.recv(1024)
#       b=msg.decode('utf-8')
#       print(b)
#     else:
#         break
# #   断开连接
# ns.close()



#   linux操作
import paramiko
# #   连接Linux，采用ssh协议
# #   创建一个远程客户端
# ssh123=paramiko.SSHClient()
# #   第一次连接主机，known_hosts 存放的主机地址，跳过查找
# #   允许连接不在known_hosts文件中的主机
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# #   连接主机
# ssh123.connect(hostname='192.168.0.60',port=22,username='root',password='123456')
# #   exec_command 执行命令 直接具有结果的命令
# a,b,c = ssh123.exec_command('ls -al /etc')
# #   第一个变量：表示输入的命令
# #   第二个变量：命令执行的结果
# #   第三个变量：命令的报错
# print(b.read().decode())
# ssh123.close()

# #   传输文件
# #   建立一个传输通道
# ssh = paramiko.Transport('192.168.0.60',22)
# #   连接Linux
# ssh.connect(username='root',password='123456')
# #   创建一个传输文件的对象
# ftp = paramiko.SFTPClient.from_transport(ssh)
# #   从Linux到Windows传文件
# #   第一个参数：表示要传输的文件
# #   第二个参数：表示存放的本机位置
# # ftp.get('install.log',r'.\a.log')   # 从Linux传输到Windows
# ftp.put('a.txt',r'./a.txt') # 从Windows传输到Linux
# ssh.close()

#   连接mysql
import pymysql
#   连接数据库
# lj = pymysql.connect(host='192.168.0.89',   #主机ip地址
#                       port=3306,    #数据库端口号
#                       user='root',  #用户
#                       password='123456',    #数据库密码
#                       charset='utf8')   #编码方式
# #   创建游标(控制器)
# yb = lj.cursor()
# #   执行sql语句
# yb.execute('use py;')
# # yb.execute('insert into biao values("xiaogang","20","boy"),("xiaohong","31","girl");')
# #   提交  对数据库数据进行更改的时候
# #   是由连接数据库的变量来提交，不是由游标的变量来提交
# # lj.commit()
# yb.execute('select * from biao;')
# #   任何结果都需要有变量来接收
# # print(yb.fetchall())   #只接受上一个SQL语句执行的结果
# # print(yb.fetchmany())      #接收上一个sql语句的结果，默认只接收第一行，在括号里写入数字几就接收多少行
# print(yb.fetchone())    #接收上一个sql语句的结果,每次只接受一行，本身具有迭代的功能
# print(yb.fetchone())
# #   断开数据库
# lj.close()