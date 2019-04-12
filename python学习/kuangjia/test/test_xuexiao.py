#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from kuangjia.data.xuexiao_duqu import mingcheng
from kuangjia.config.xuexiao import xuexiao

class xuexiao_case(unittest.TestCase):
    shujv = mingcheng()
    shujv = shujv.shujv()

    def test_1(self):
        diqu = xuexiao()
        xiangying = diqu.jiekou(self.shujv[0][0])
        self.assertEqual(xiangying['code'],0)

    def test_2(self):
        diqu = xuexiao()
        xiangying = diqu.jiekou(self.shujv[1][0])
        self.assertEqual(xiangying['code'],1)

    def test_3(self):
        diqu = xuexiao()
        xiangying = diqu.jiekou(int(self.shujv[2][0]))
        self.assertEqual(xiangying['code'],0)

    def test_4(self):
        diqu = xuexiao()
        xiangying = diqu.jiekou(self.shujv[3][0])
        self.assertEqual(xiangying['code'],1)

    def test_5(self):
        diqu = xuexiao()
        xiangying = diqu.jiekou(self.shujv[4][0])
        self.assertEqual(xiangying['code'], 1)

if __name__ == '__main__':
    unittest.main()