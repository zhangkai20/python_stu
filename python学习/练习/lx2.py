#! /usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

dr = webdriver.Firefox()
dr.get('https://jd.com')
dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/ul[2]/li[1]/a[1]').click()
dr.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/a').click()
dr.find_element_by_id('loginname').send_keys('15139513258')
dr.find_element_by_id('nloginpwd').send_keys('qqq1389954')
dr.find_element_by_id('loginsubmit').click()
star = dr.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div[3]')
#   drag_and_drop(起始位置，结束位置)
#   drag_and_drop_by_offset(起始位置，x轴坐标，y轴坐标)
while True:
    try:
        ActionChains(dr).drag_and_drop_by_offset(star,68,0).perform()
        sleep(2)
    except:
        break