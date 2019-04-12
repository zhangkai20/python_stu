#! /usr/bin/python
# -*- coding: utf-8 -*-

from appium import webdriver
import unittest
from time import sleep
import xlrd
import warnings


def shujv():
    a = []
    f = xlrd.open_workbook(r'C:\Users\zk\Desktop\python学习\APP\app.xlsx')
    sheet = f.sheets()[0]
    nro = sheet.nrows
    for i in range(nro):
        a.append(sheet.row_values(i))
    return a


class wangyi(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        desired = {'platformName': 'Android',
                   'deviceName': '127.0.0.1:62001',
                   'appPackage': 'com.netease.cloudmusic',
                   'appActivity': '.activity.LoadingActivity'}
        self.dr = webdriver.Remote('http://localhost:4723/wd/hub', desired)
        sleep(15)
        self.dr.find_element_by_id('com.netease.cloudmusic:id/qc').click()
        sleep(3)
        self.dr.find_element_by_id('com.netease.cloudmusic:id/ik').send_keys('15139513258')
        sleep(2)
        self.dr.find_element_by_id('com.netease.cloudmusic:id/ii').send_keys('qqq1389954')
        sleep(2)
        self.dr.find_element_by_id('com.netease.cloudmusic:id/qc').click()
        sleep(10)
        self.dr.find_element_by_id('com.netease.cloudmusic:id/qn').click()
        sleep(2)

    def test_1(self):
        b = self.dr.find_element_by_id('com.netease.cloudmusic:id/af4').text
        self.assertEqual(b,'空乱无')

    def tearDown(self):

        self.dr.quit()

if __name__ == '__main__':
    unittest.main()