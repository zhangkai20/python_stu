#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import requests
from kuangjia.config.suopei import suopei
from kuangjia.data.suopei_duqu import suopei_shujv

class suopei_case(unittest.TestCase):
    shujv = suopei_shujv()
    shujv = shujv.duqu_shujv()

    def test_1(self):
        suo = suopei()
        asd = suo.jichushujv(int(self.shujv[0][0]),int(self.shujv[0][1]))
        self.assertEqual(asd['data']['applicationType'][0]['name'],'多装')

    def test_2(self):
        suo = suopei()
        asd = suo.jichushujv(self.shujv[1][0], int(self.shujv[1][1]))
        self.assertEqual(asd['message'],'get error')

    def test_3(self):
        suo = suopei()
        asd = suo.jichushujv(int(self.shujv[2][0]), self.shujv[2][1])
        self.assertEqual(asd['message'],'get error')

if __name__ == '__main__':
    unittest.main()