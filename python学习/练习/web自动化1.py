#! /usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui


# dr = webdriver.Chrome()
# dr.get('https://mail.qq.com/')
# sleep(2)
#   处理框架    iframe（窗口）
#   dr.switch_to.frame()    可以写框架的ID或name的值，或者先定位到框架
# dr.switch_to.frame('login_frame')   #   切换到某一个框架
# dr.switch_to.default_content()  #   回到最开始的页面中
# dr.switch_to.parent_frame()     #   回到父框架页面中
#   处理浏览器窗口
#   获取当前窗口的句柄
# print(dr.current_window_handle)
# #   获取所有窗口的句柄
# qq = dr.window_handles
# #   切换句柄    参数只能是句柄
# dr.switch_to.window(qq[-1])

#   模拟鼠标的操作
dr = webdriver.Firefox()
# dr.get('https://www.jd.com')
# sleep(2)
# w = dr.find_element_by_id('J_cate').find_elements_by_tag_name('li')
# for i in w:
#     #   控制鼠标来移动到元素的位置上      perform 执行
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)
# dr.quit()

#   处理弹出框
# dr.get('http://www.lwfree.cn/yurenjie/yuerenjie1.html')
# sleep(2)
# w = dr.switch_to.alert
#   获取弹出框上的内容
# print(w.text)
# w.accept()  #   点击确定
# w.dismiss() #   点击取消
# w.send_keys('内容')   #   输入

#   处理页面滚动条
dr.get('https://www.jd.com')
# sleep(2)
# #   JavaScript代码
# js = "var q=document.documentElement.scrollTop=1000"
# #   执行JavaScript语句
# dr.execute_script(js)

#   智能等待
#   设置一个最大等待时间
# unit = ui.WebDriverWait(dr,10)
# # 直到定位的元素出现，就不会继续等待
# unit.until(lambda dr: dr.find_element_by_class_name('label').is_displayed())
# print('yes')

#   获取定位到的元素某个属性的值
w = dr.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[7]/a[3]')
a = w.get_attribute('href')

#   截图
dr.get_screenshot_as_file('保存的文件名称')

#   刷新当前页面
dr.refresh()
