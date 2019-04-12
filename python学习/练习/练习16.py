#!/usr/bin/python
#-*- coding:utf-8 -*-

import requests
import re
import json
# json.dumps()  将字典变成json数据
# json.loads()  将json数据变成字典

# ad={'name' : 123}
# j=json.dumps(ad)
# print(j)
# nj=json.loads(j)
# print(nj)

# 动态爬虫
class gaode:
    def jiexi(self):
        url='https://m.amap.com/service/poi/tips.json?words=%E7%81%AB%E8%BD%A6%E7%AB%99&adcode=true&user_loc=114.341447%2C34.797049&longitude=114.325585&latitude=34.802687&city=410200&uuid=5ceebef4-d921-49bc-9f3a-807a8815eb7f'
        head={
            'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Mobile Safari/537.36'
        }
        qingqiu = requests.get(url=url,headers=head)
        fenxi=qingqiu.content.decode('utf-8')
        fx=json.loads(fenxi)
        return fx
    def zhengze(self):
        nr = self.jiexi()
        a = nr['tip_list']
        return a
    def xeiru(self):
        b = self.zhengze()
        for i in b[1:]:
            c = i['tip']
            name = c['name']
            dz = c['district']
            with open('gd.txt','a',encoding='utf-8') as f:
                f.write('{},{}\n'.format(name,dz))
