#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import HTMLTestRunner
from kuangjia.test.test_xuexiao import xuexiao_case

def baogao():
    suit = unittest.TestSuite
    dis = unittest.defaultTestLoader.discover(r'C:\Users\zk\Desktop\python学习\kuangjia\test','test_xuexiao.py')
    for i in dis:
        suit.addTest(i)
    # f = open(r'C:\Users\zk\Desktop\python学习\kuangjia\report\xuexiao.html','wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='学校查询',description='结果如下',tester='zk')
    # runner.run(suit)
    # f.close()

baogao()

