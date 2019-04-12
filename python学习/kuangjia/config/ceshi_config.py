#! /usr/bin/python
# -*- coding: utf-8 -*-

import requests

class peijianhao(object):

    def peijian(self,x):
        url = 'https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/orderManage/list'
        head = {
            'Content-Type':'application/json',
                'x-dealer-code':'2100001',
                'x-position-code':'D_PO_1028',
                'x-resource-code':'pol4s_orderManage_list',
                'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
                'x-user-code':'dhxc1u',
                'x-access-token':'da05ee37e5676e7b27972b2892e0fdeb'
        }
        body = '{"queryTerms":{"partCode":"","partName":"","vehicleModel":"1","dimsPartType":"1","ugentLevel":"1","isCanSunPack":"-1","isTransfer":"-1","isDelay":"-1","isEffective":"-1","isDimsRecommend":"-1","orderNo":"","cancelStatus":"-1"},	"pageNum":%s}' %(x)
        res = requests.post(url=url,headers=head,data=body)
        msg = res.json()
        return msg

class dingdanmingxi(object):

    def dingdan(self,x):
        url = 'https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/partOrderDetailSearch'
        head = {'Content-Type':'application/json',
                'x-dealer-code':'2100005',
                'x-position-code':'D_PO_1028',
                'x-resource-code':'pol4s_partOrderSearch_partOrderDetailSearch',
                'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
                'x-user-code':'dhxc1u',
                'x-access-token':'da05ee37e5676e7b27972b2892e0fdeb',}
        body = '{"pageNum":"1","pgeSize":"10","queryTerms":{"orderNo":%s}}' %(x)
        res = requests.post(url=url,headers=head,data=body)
        msg = res.json()
        return msg

class dingdanliebiao(object):

    def liehao(self,x,y):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderList'
        head = {'Content-Type':'application/json',
                'x-dealer-code':'2100005',
                'x-position-code':'D_PO_1028',
                'x-resource-code':'pol4s_partOrder_orderList',
                'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
                'x-user-code':'dhxc1u',
                'x-access-token':'da05ee37e5676e7b27972b2892e0fdeb'}
        body = '{"pageNum":%s,"pageSize":%s,"queryTerms": {"orderType":"","orderStatus": "","orderDelayFlag":"","orderNo": "","startReportDate":"","endReportDate":""}}' %(x,y)
        res = requests.post(url=url,headers=head,data=body)
        msg = res.json()
        return msg

class peijianmingxi(object):

    def peijian(self,x):
        url = 'https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderPartDetail'
        head = {'Content-Type':'application/json',
                'x-dealer-code':'2100005',
                'x-position-code':'D_PO_1028',
                'x-resource-code':'pol4s_partOrder_orderPartDetail',
                'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
                'x-user-code':'dhxc1u',
                'x-access-token':'da05ee37e5676e7b27972b2892e0fdeb'}
        body = '{"partOrderItemId":%s}' %(x)
        res = requests.post(url=url,headers=head,data=body)
        msg = res.json()
        return msg

class shouye(object):

    def shouye(self):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderHomePage'
        head = {'Content-Type':'application/json',
                'x-dealer-code':'2100005',
                'x-position-code':'D_PO_1028',
                'x-resource-code':'pol4s_partOrder_orderHomePage',
                'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
                'x-user-code':'dhxc1u',
                'x-access-token':'da05ee37e5676e7b27972b2892e0fdeb'}
        res = requests.post(url=url,headers=head)
        msg = res.json()
        return msg

if __name__ == '__main__':
    a=peijianhao()
    print(a.peijian())