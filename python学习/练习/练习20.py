#!/usr/bin/python
# -*- coding=utf-8 -*-

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