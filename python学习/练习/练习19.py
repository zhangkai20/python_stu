#!/usr/bin/python
# -*- coding=utf-8 -*-

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



# with paramiko.SSHClient() as ssh123:
#     ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#     ssh123.connect(hostname='192.168.0.60', port=22, username='root', password='123456')
#     while True:
#         f = input('>>>')
#         if f =='exit':
#             break
#         else:
#             try:
#                 a, b, c = ssh123.exec_command(f)
#                 print(b.read().decode())
#             except:
#                 continue

import socket

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


# #   客户端(UDP)
# sock =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #   发送请求
# host = ('127.0.0.1',8888) # 服务器端的IP地址和端口号
# while True:
#     b = input('>>>>')
#     if b != 'exit':
#         sock.sendto(b.encode('utf-8'),host)
# #   接收数据
#         msg=sock.recv(1024)
#         print(msg.decode('utf-8'))
#     else:
#         break
# sock.close()
