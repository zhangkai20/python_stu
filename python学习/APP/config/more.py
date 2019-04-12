#! /usr/bin/python
# -*- coding: utf-8 -*-

from appium import  webdriver
from time import sleep
import  warnings
from appium.webdriver.common.touch_action import TouchAction

# class moer():
#
#     def more(self):
#         des = {'platformName':'Android',
#            'deviceName':'127.0.0.1:62001',
#            'appPackage':'com.ss.android.article.news',
#            'appActivity':'.activity.SplashBadgeActivity'
#
#         }
#         self.dr = webdriver.Remote('http://localhost:4723/wd/hub',des)
#         sleep(15)
#         self.dr.find_element_by_id('com.ss.android.article.news:id/cy1').click()
#         sleep(15)
#         a = self.dr.find_elements_by_class_name('android.widget.FrameLayout')
#         print(a)
#
#
#
#
# if __name__ == '__main__':
#    a=moer()
#    a.more()







class moerxinqiu(object):

    def moer_denglu(self):
        warnings.simplefilter("ignore", ResourceWarning)
        drivces_caps={'platformName':'Android',
                      'deviceName':'127.0.0.1:62001',
                      'appPackage':'com.mooreshare.app',
                      'appActivity':'.ui.activity.splash.SplashActivity'}
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',drivces_caps)
        sleep(20)
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        for i in range(3):
            x1 = int(x * 0.9)
            y1 = int(y * 0.5)
            x2 = int(x * 0.1)
            self.driver.swipe(x1,y1,x2,y1,2000)
            sleep(2)
        self.driver.find_element_by_class_name('android.widget.ImageView').click()
        b=self.driver.find_element_by_id('com.mooreshare.app:id/fl_menutab')
        sleep(1)
        c=b.find_elements_by_class_name('android.widget.RelativeLayout')
        sleep(1)
        d=c[0]
        sleep(1)
        d.find_element_by_id('com.mooreshare.app:id/rl_menu4').click()
        sleep(5)
        self.driver.find_element_by_id('com.mooreshare.app:id/rl_avatar').click()
        sleep(2)
        self.driver.find_element_by_id('com.mooreshare.app:id/rl_login_by_mail').click()
        sleep(2)
        s = self.driver.find_elements_by_id('com.mooreshare.app:id/rl_content')
        s[0].send_keys('937818840@qq.com')
        s[1].send_keys('qqq1389954 ')
        self.driver.find_element_by_id('com.mooreshare.app:id/login_bt').click()
        self.driver.quit()


moerxinqiu().moer_denglu()
