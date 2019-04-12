#!/usr/bin/python
#-*- coding:utf-8 -*-

import requests
import re
import xlwt
import xlrd
import xlutils
import os
class douban:
    def jiexi(self,x):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(x)
        head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
                }
        xiangying = requests.get(url=url,headers=head)
        fenxi=xiangying.content.decode('utf-8')
        return fenxi
    def pipei(self,x):
        lb=[]
        neirong = self.jiexi(x)
        b=re.compile(r'<span class="title">.*</p>',re.S)
        c=b.findall(neirong)
        for i in c:
            ming = re.compile(r'<span class="title">(.*?)</span>',re.S)
            pian = ming.findall(i)
            daoyan = re.compile(r'导演: (.*?)&',re.S)
            dao = daoyan.findall(i)
            jianjie=re.compile(r'<span class="inq">(.*?)</span>',re.S)
            jj=jianjie.findall(i)
        pingjia = re.compile(r'<div class="star">(.*?)</div>',re.S)
        pj = pingjia.findall(neirong)
        for k in pj:
            l=re.compile(r'<span>(.*?)</span>',re.S)
            lbpj=l.findall(k)
            lb.append(lbpj[0])
        for j in pian:
            if '&nbsp' in j:
                pian.remove(j)
        return pian,dao,jj,lb
    def xieru(self,x):
        neirong=self.pipei(x)
        d=os.listdir('.')
        if 'douban.xls'  in d:
            from xlutils.copy import copy
            f = xlrd.open_workbook('douban.xls')
            sd=f.sheets()[0]
            z = sd.nrows
            nf = copy(f)
            sheet = nf.get_sheet(0)
            for i,j in enumerate(neirong):
                for k in range(len(j)):
                    sheet.write(z+k,i,j[k])
            nf.save('douban.xls')
        else:
            f = xlwt.Workbook(encoding='utf-8')
            sheet = f.add_sheet('{}'.format(x))
            sheet.write(0, 0, '片名')
            sheet.write(0, 1, '导演')
            sheet.write(0, 2, '简介')
            sheet.write(0, 3, '评价')
            for i, j in enumerate(neirong):
                for k in range(len(j)):
                    sheet.write(k + 1, i, j[k])
            f.save('douban.xls')

class tupian:
    def jiexi(self,x):
        url = 'https://www.qiushibaike.com/imgrank/page/{}/'.format(x)
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
            }
        xiangying = requests.get(url=url, headers=head)
        fenxi = xiangying.content.decode('utf-8')
        return fenxi
    def zengzhe(self,x):
        shuju=[]
        zz=self.jiexi(x)
        pt=re.compile(r'<div class="thumb">(.*?)</a>',re.S)#过滤图片的网址
        items=pt.findall(zz)
        for i in items:
            tp=re.compile(r'src="(.*?)"',re.S)
            ss=tp.findall(i)
            shuju.append(ss[0])
        return shuju
    def baochun(self,x):
        tp=self.zengzhe(x)
        #   任何图片都是二进制
        #   请求图片的网址得到图片的源码
        for i,j in enumerate(tp):
            res =requests.get('https:'+j)
            ht = res.content    #   读取的结果是一个二进制
            with open('第{}页{}.jpg'.format(x,i+1),'wb') as f:
                f.write(ht)
def shanchu():
    i = os.listdir('.')
    for j in i:
        if '.jpg' in j:
            os.remove(j)

# a=tupian()
# for i in range(1,4):
#     a.baochun(i)
a=douban()
for i in range(0,50,25):
    a.xieru(i)