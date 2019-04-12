#!/usr/bin/python
#-*- coding:utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup
class qiushi(object):
    def qingqiu(self,page):
        url = 'https://www.qiushibaike.com/text/page/{}/'.format(page)
        #   伪装成浏览器
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }
        # 发送请求
        xingying = requests.get(url=url,headers=head)
        #   读取响应    1.text(以字符串的方式读取)
        #              2.content(以字节的方式读取) content.decode('utf-8')编码方式以网站的编码方式为准
        html = xingying.content.decode('utf-8')
        #   html = xingying.text
        #   返回结果赋值
        return html
    def guolv(self,c):
        shuju = []
        #   编译正则，并查找
        patt = re.compile(r'<div class="content">(.*?)</span>',re.S)
        items = patt.findall(c)
        for i in items:
            i = i.replace('<span>', '').replace('<br/>', '').strip()
            shuju.append(i)
        return shuju
    def save(self, qwe):
            with open('a.txt', 'w', encoding='utf-8') as f:
                for i in qwe:
                    f.write(i + '\n')
a=qiushi()
html = a.qingqiu(page=1)
shuju = a.guolv(html)
a.save(shuju)