#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import HTMLTestRunner

def baogao(aaa):
    suit = unittest.TestSuite()
    dis = unittest.defaultTestLoader.discover(r'C:\Users\zk\Desktop\python学习\kuangjia\test',aaa)
    for i in dis:
        suit.addTests(i)
    f = open(r'C:\Users\zk\Desktop\python学习\kuangjia\report\a.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='{}'.format(aaa), tester='zk', description='结果如下')
    runner.run(suit)
    f.close()

