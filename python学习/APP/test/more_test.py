#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from APP.config.more import moerxinqiu
from APP.data.more import moer_data

class test_moer(unittest.TestCase):
    shujv = moer_data()
    shujv = shujv.shujv()

    def test_denglv1(self):
        de = moerxinqiu()
        de = de.moer_denglu()
        