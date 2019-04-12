#! /usr/bin/python
# -*- coding: utf-8 -*-

from appium import webdriver
from time import sleep


desired = {'platformName':'Android',
           'deviceName':'127.0.0.1:62001',
           'appPackage':'com.netease.cloudmusic',
           'appActivity':'.activity.LoadingActivity'}
dr = webdriver.Remote('http://localhost:4723/wd/hub',desired)
sleep(15)
dr.find_element_by_id('com.netease.cloudmusic:id/qc').click()
sleep(3)
dr.find_element_by_id('com.netease.cloudmusic:id/ik').send_keys('15139513258')
sleep(2)
dr.find_element_by_id('com.netease.cloudmusic:id/ii').send_keys('qqq1389954')
sleep(2)
dr.find_element_by_id('com.netease.cloudmusic:id/qc').click()
sleep(10)
dr.find_element_by_id('com.netease.cloudmusic:id/qn').click()   #   点击抽屉菜单
sleep(2)
a = dr.find_element_by_id('com.netease.cloudmusic:id/af4').text
if a == '空乱无':
    print('pass')
else:
    print('fail')

dr.quit()