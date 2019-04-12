#! /usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()
dr.get('https://www.baidu.com')
sleep(2)
dr.find_element_by_id('kw').send_keys('京东')
sleep(2)
dr.find_element_by_id('su').click()
sleep(2)
print(dr.window_handles)
dr.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[4]/div[3]/h3/a[1]').click()
sleep(2)
qq = dr.window_handles
dr.switch_to.window(qq[-1])
dr.find_element_by_xpath('//*[@id="key"]').clear()
sleep(2)
dr.find_element_by_xpath('//*[@id="key"]').send_keys('python')
sleep(2)
dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div[2]/button/i').click()
sleep(2)
dr.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[7]/a[3]').click()
sleep(2)
qq = dr.window_handles
dr.switch_to.window(qq[-1])
dr.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/div/div[2]/div[3]/a[1]').click()
sleep(2)
dr.quit()

