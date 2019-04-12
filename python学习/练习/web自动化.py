#! /usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

# #   获取网址的标题
# print(dr.title)
# #   获取打开网页的网址
# print(dr.current_url)
# #   回退
# dr.back()
# sleep(2)
# #   前进
# dr.forward()
# sleep(2)
#   设置浏览器的大小
# dr.set_window_size(500,500)
# #   设置浏览器的位置
# dr.set_window_position(600,400)
# #   设置浏览器最大化（全屏）
# dr.maximize_window()
# #   最小化浏览器
# dr.minimize_window()


#   定义使用的浏览器
dr = webdriver.Chrome()
#   打开网址
dr.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
# sleep(2)
# dr.get('https://www.weibo.com')
# sleep(2)
#   定位
#   1.id 定位
#   通过 id 来定位，标签的id属性
# dr.find_element_by_id("kw").send_keys('11111')
# sleep(2)
# dr.find_element_by_id('su').click()
#   2.class_name 定位，标签的class属性
# dr.find_element_by_class_name('s_ipt').send_keys(111)
# dr.find_element_by_class_name('bg s_btn').click()
#   3.name 定位，标签上的name属性
# dr.find_element_by_name('wd').send_keys(222)
# dr.find_element_by_id('su').click()
#   4.link_text 定位  标签的文本定位
# dr.find_element_by_link_text('hao123').click()
#   5.partial_link_text 定位，标签的模糊文本定位
# dr.find_element_by_partial_link_text('123').click()
#   6.tag_name 定位，通过标签名称定位，最不唯一的一个定位，通常用来定位一组数据
# dr.find_elements_by_tag_name('input')
#   7.css_selector 定位，css来定位
# dr.find_element_by_css_selector('#kw').send_keys(111)
#   8.xpath 定位  路径定位    xpath,路径标记语言    xml，可扩展性标记语言
# dr.find_elements_by_xpath('//*[@id="kw"]').send_keys(111)
#   关闭浏览器
# dr.quit()   #   关闭浏览器，断开连接
#   dr.close()  #   关闭浏览器，不断开连接

#   定位一组数据  同时对多个数据进行操作时
# wd = dr.find_elements_by_class_name('mnav')
#   层级定位    遇到复杂的元素的定位
# wd = dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
# for i in wd:
#     i.click()
#     sleep(2)
#   模拟动作
#   send_keys() 输入
#   click()     点击
#   text()      获取定位到的元素的文本
#   clear()     清空定位到的元素上面的数据