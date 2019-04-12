#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from kuangjia.config import ceshi_config
from kuangjia.data import ceshi_data

class peijianhao(unittest.TestCase):
    a = ceshi_data
    a = a.peijianhao()
    shujv = a.peijian()
    pei = ceshi_config
    pei = pei.peijianhao()

    def test_1(self):
        pei = self.pei.peijian(int(self.shujv[0][0]))
        self.assertEqual(pei['status'],1)
    def test_2(self):
        pei = self.pei.peijian(int(self.shujv[0][1]))
        self.assertEqual(pei['status'],1)


class peijianxiangxi(unittest.TestCase):
    a = ceshi_data
    a = a.peijianmingxi()
    shujv = a.peijian()
    pei = ceshi_config
    pei = pei.peijianmingxi()

    def test_1(self):
        pei = self.pei.peijian(int(self.shujv[0][0]))
        self.assertEqual(pei['status'],1)
    def test_2(self):
        pei = self.pei.peijian(int(self.shujv[0][1]))
        self.assertEqual(pei['status'], 0)


class dingdan(unittest.TestCase):
    a = ceshi_data
    a = a.dingdan()
    shujv = a.dingdan()
    ding = ceshi_config
    ding = ding.dingdanmingxi()

    def test_1(self):
        ding = self.ding.dingdan(int(self.shujv[0][0]))
        self.assertEqual(ding['status'],1)

    def test_2(self):
        ding = self.ding.dingdan(int(self.shujv[0][1]))
        self.assertEqual(ding['status'],0)

class liebiao(unittest.TestCase):
    a = ceshi_data
    a = a.liebiao()
    shujv = a.liebiao()
    lie = ceshi_config
    lie = lie.dingdanliebiao()

    def test_1(self):
        ding = self.lie.liehao(int(self.shujv[0][0]),int(self.shujv[1][0]))
        self.assertEqual(ding['status'],1)

    def test_2(self):
        ding = self.lie.liehao(int(self.shujv[0][1]),int(self.shujv[1][1]))
        self.assertEqual(ding['status'],0)

