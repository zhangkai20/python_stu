#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
import xlrd

def qingqiu():
    f = xlrd.open_workbook(r'C:\Users\zk\Desktop\python学习\练习\qq.xlsx')
    sheet = f.sheets()[0]
    now = sheet.nrows
    for i in (1,now):
        dr = webdriver.Firefox()
        dr.get('https://qzone.qq.com/')
        dr.switch_to.frame('login_frame')
        unit = ui.WebDriverWait(dr,10)
        unit.until(lambda dr:dr.find_element_by_id('switcher_plogin').is_displayed())
        dr.find_element_by_id('switcher_plogin').click()
        dr.find_element_by_id('u').send_keys('{}'.format(int(sheet.row_values(i)[0])))
        dr.find_element_by_id('p').send_keys('{}'.format(sheet.row_values(i)[1]))
        dr.find_element_by_id('login_button').click()
        # dr.switch_to.frame('newVcodeArea')
        # w = dr.find_elements_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/img')
        # ActionChains(dr).drag_and_drop_by_offset(w,195,0).perform()
        dr.quit()

class ceshi(unittest.TestCase):

    def test_1(self):

        self.assertEqual()
