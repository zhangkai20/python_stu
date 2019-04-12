#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import re
import os
import json
class xinxian:
    def fenxi(self,page):
        url = 'https://www.qiushibaike.com/textnew/page/{}/?s=5167696'.format(page)
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
                }
        xiangying = requests.get(url=url,headers=head)
        fenxi = xiangying.content.decode('utf-8')
        return fenxi
    def zengze(self,s):
        leibiao = []
        zifu = self.fenxi(s)
        b = re.compile(r'<div class="content">(.*?)</span>',re.S)
        c = b.findall(zifu)
        for i in c:
            i = i.replace('<span>','').replace('<br/>','').strip()
            leibiao.append(i)
        return leibiao
    def xieru(self,s):
        neirong = self.zengze(s)
        with open('a.txt', 'a', encoding='utf-8') as f:
            for i in neirong:
                    f.write(i + '\n')

class doutu:
    def xiangying(self,x):
        url = 'https://www.doutula.com/article/list/?page={}'.format(x)
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
        }
        xiangying=requests.get(url=url,headers=head)
        fenxi=xiangying.content.decode('UTF-8')
        return fenxi
    def pipei(self,x):
        wjm=[]
        klb=[]
        wenjian=[]
        nr=self.xiangying(x)
        b=re.compile(r'</div> <div class="col-sm-9">(.*?)<div class="text-center">',re.S)
        d=b.findall(nr)
        for k in d:
            aa = re.compile(r'<div class="list-group-item random_list">.*?</div>',re.S)
            wj = aa.findall(k)
            for i in wj:
                k = k.replace(i,'')
            wjm.append(k)
        for i in wjm:
            zz=re.compile(r'<a href="(.*?)" class=',re.S)
            wz=zz.findall(i)
            klb.append(wz)
        for i in wjm:
            wjm = re.compile(r'<div class="random_title">(.*?)<div class="date">',re.S)
            mz = wjm.findall(i)
            wenjian.append(mz)
        return klb[0],wenjian[0]
    def xieru(self,x):
        lb=[]
        tiaojian=self.pipei(x)
        for i in tiaojian[0]:
            head = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
            }
            xy=requests.get(url=i,headers=head)
            jx=xy.content.decode('utf-8')
            tj=re.compile(r"this.src='(.*?)'",re.S)
            tp=tj.findall(jx)
            lb.append(tp)
        for j in tiaojian[1]:
            os.mkdir(r'C:\Users\zk\Desktop\python学习\{}'.format(j))
        for i in range(len(lb)):
            for m,k in enumerate(lb[i]):
                os.chdir(r'C:\Users\zk\Desktop\python学习\{}'.format(tiaojian[1][i]))
                head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
                xy = requests.get(url=k, headers=head)
                erjinzhi=xy.content
                if '.gif' in k:
                    with open('{}.gif'.format(m),'wb') as f:
                        f.write(erjinzhi)
                else :
                    with open('{}.jpg'.format(m),'wb') as f:
                        f.write(erjinzhi)

