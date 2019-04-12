#! /usr/bin/python
# -*- coding: utf-8 -*-

import HTMLTestRunner
import unittest
from kuangjia.test.test_suopei import suopei_case

def baogao(aa):
    suit = unittest.TestSuite()
    # suit.addTest(unittest.makeSuite(suopei_case))
    dis = unittest.defaultTestLoader.discover(r'C:\Users\zk\Desktop\python学习\kuangjia\test',aa)
    #   两个参数：参数1：路径(test文件存放)，参数2：匹配条件
    #   到这个路径下，匹配所有以test开头的文件
    #   test开头文件中找到函数以test开头
    for i in dis:
        suit.addTest(i)
    f = open(r'C:\Users\zk\Desktop\python学习\kuangjia\report\a.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='索赔测试报告', tester='zk', description='结果如下')
    runner.run(suit)
    f.close()

