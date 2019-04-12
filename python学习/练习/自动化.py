#! /usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import unittest
import HTMLTestRunner
import time

#   HTMLTestRunner  产生测试报告的模块

# url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
# head = {'Content-Type':'application/json',
# 'x-dealer-code':'2100150',
# 'x-position-code':'D_PO_1028',
# 'x-resource-code':'BASIC_DATA',
# 'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
# 'x-user-code':'djy0mx',
# 'x-access-token':'da05ee37e5676e7b27972b2892e0fdeb'}
# body='{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize":10,"curPage":1}'.encode('utf-8')
# res = requests.post(url,headers=head,data=body)
# # msg = json.loads(res.text)
# msg = res.json()
# #   assert  断言函数
# assert msg['data']['applicationType'][0]['name'] == '多装'

#   unittest    单元测试框架，Python自带模块，主要是对用例进行管理和执行
#   所有用例函数必须以 test 开头
def jiekou():
    url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
    head = {'Content-Type': 'application/json',
            'x-dealer-code': '2100150',
            'x-position-code': 'D_PO_1028',
            'x-resource-code': 'BASIC_DATA',
            'x-track-code': '4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
            'x-user-code': 'djy0mx',
            'x-access-token': 'da05ee37e5676e7b27972b2892e0fdeb'}
    body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize":10,"curPage":1}'.encode('utf-8')
    res = requests.post(url, headers=head, data=body)
    msg = res.json()
    return msg

class suopei(unittest.TestCase):

    def setUp(self):
        #   每次执行用例之前执行
        #   初始化测试环境
        pass

    def tearDown(self):
        #   每次执行用例之后执行
        #   清理测试环境
        #   保证任何测试用例都要在相同的环境下执行
        pass

    def test_1(self):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
        head = {'Content-Type':'application/json',
                'x-dealer-code':'2100150',
                'x-position-code':'D_PO_1028',
                'x-resource-code':'BASIC_DATA',
                'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
                'x-user-code':'djy0mx',
                'x-access-token':'da05ee37e5676e7b27972b2892e0fdeb'}
        body='{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize":10,"curPage":1}'.encode('utf-8')
        res = requests.post(url,headers=head,data=body)
        msg = res.json()
        self.assertEqual(msg['data']['applicationType'][0]['name'],'多装')

    def test_2(self):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
        head = {'Content-Type': 'application/json',
                'x-dealer-code': '2100150',
                'x-position-code': 'D_PO_1028',
                'x-resource-code': 'BASIC_DATA',
                'x-track-code': '4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
                'x-user-code': 'djy0mx',
                'x-access-token': 'da05ee37e5676e7b27972b2892e0fdeb'}
        body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize":11,"curPage":www}'.encode('utf-8')
        res = requests.post(url, headers=head, data=body)
        msg = res.json()
        self.assertEqual(msg['message'],'get error')

    def test_3(self):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
        head = {'Content-Type': 'application/json',
                'x-dealer-code': '2100150',
                'x-position-code': 'D_PO_1028',
                'x-resource-code': 'BASIC_DATA',
                'x-track-code': '4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
                'x-user-code': 'djy0mx',
                'x-access-token': 'da05ee37e5676e7b27972b2892e0fdeb'}
        body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize":qqqq,"curPage":11}'.encode('utf-8')
        res = requests.post(url, headers=head, data=body)
        msg = res.json()
        self.assertEqual(msg['message'],'get error')

    def test_4(self):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
        head = {'Content-Type': 'application/json',
                'x-dealer-code': '2100150',
                'x-position-code': 'D_PO_1028',
                'x-resource-code': 'BASIC_DATA',
                'x-track-code': '4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
                'x-user-code': 'djy0mx',
                'x-access-token': 'da05ee37e5676e7b27972b2892e0fdeb'}
        body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize":qqqq,"curPage":sss}'.encode('utf-8')
        res = requests.post(url, headers=head, data=body)
        msg = res.json()
        self.assertEqual(msg['message'],'get error')

    def test_5(self):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
        head = {'Content-Type': 'application/json',
                'x-dealer-code': '2100150',
                'x-position-code': 'D_PO_1028',
                'x-resource-code': 'BASIC_DATA',
                'x-track-code': '4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
                'x-user-code': 'djy0mx',
                'x-access-token': 'da05ee37e5676e7b27972b2892e0fdeb'}
        body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize":1@!,"curPage":12}'.encode('utf-8')
        res = requests.post(url, headers=head, data=body)
        msg = res.json()
        self.assertEqual(msg['message'], 'get error')

    def test_6(self):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
        head = {'Content-Type': 'application/json',
                'x-dealer-code': '2100150',
                'x-position-code': 'D_PO_1028',
                'x-resource-code': 'BASIC_DATA',
                'x-track-code': '4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
                'x-user-code': 'djy0mx',
                'x-access-token': 'da05ee37e5676e7b27972b2892e0fdeb'}
        body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize":,"curPage":12}'.encode('utf-8')
        res = requests.post(url, headers=head, data=body)
        msg = res.json()
        self.assertEqual(msg['message'], 'get error')

    def test_7(self):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
        head = {'Content-Type': 'application/json',
                'x-dealer-code': '2100150',
                'x-position-code': 'D_PO_1028',
                'x-resource-code': 'BASIC_DATA',
                'x-track-code': '4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
                'x-user-code': 'djy0mx',
                'x-access-token': 'da05ee37e5676e7b27972b2892e0fdeb'}
        body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize"10:,"curPage":}'.encode('utf-8')
        res = requests.post(url, headers=head, data=body)
        msg = res.json()
        self.assertEqual(msg['message'], 'get error')

if __name__ == '__main__':
    #   创建一个测试套件
    suit = unittest.TestSuite()
    #   添加测试用例
    for i in range(1,8):
        suit.addTest(suopei('test_{}'.format(i)))
    now = time.strftime('%Y-Ym-Yd,%H:%M:%S',time.localtime(time.time()))
    f = open('abc.html','wb')
    #   定义测试报告内容
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='索赔测试报告',tester='zk',description='结果如下')
    runner.run(suit)
    f.close()
#   main 检测类中所有以 test 开头的函数
#   比较 test 后面的字符，谁在前就执行谁
#         unittest.main()

