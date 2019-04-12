#!/usr/bin/python
# -*- coding=utf-8 -*-

import time
from time import sleep
import threading    #   多线程模块
# def asd():
#     for i in range(3):
#         print('111')
#         sleep(2)
# def sd():
#     for j in range(3):
#         print('222')
#         sleep(2)
# threading.Thread(target=asd).start()
# threading.Thread(target=sd).start()

# print(time.time())
# print(time.localtime())
# print(time.strftime('%Y-%m-%d %H-%M-%S',time.localtime()))
# print(time.strptime('1977-12-13','%Y-%m-%d'))
# print(time.mktime((2019,2,28,10,20,30,10,30,10)))

# def riqi(x):
#     a=time.strptime(x,'%Y-%m-%d')
#     if a[0] % 4 ==0:
#         if a[0] % 100 == 0:
#             if a[0] %400 == 0:
#                 print('{}年是闰年'.format(a[0]))
#             else:
#                 print('{}年不是闰年'.format(a[0]))
#         else:
#             print('{}年是闰年'.format(a[0]))
#     else:
#         print('{}年不是闰年'.format(a[0]))
#     print('今天星期{}'.format(a[6]+1))
#     print('今天是一年中的{}天'.format(a[7]))
# riqi('2000-2-22')

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