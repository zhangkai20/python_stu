#! /usr/bin/python
# -*- coding: utf-8 -*-

import HTMLTestRunner
import unittest

def moer(pipei):
    suit = unittest.TestSuite()
    dis = unittest.defaultTestLoader.discover(r'C:\Users\zk\Desktop\python学习\APP\test',pipei)
    for i in dis:
        suit.addTest(i)
    with open(r'C:\Users\zk\Desktop\python学习\APP\report\a.html','wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='摩尔芯球',tester='zk',description='结果如下')
        runner.run(suit)


