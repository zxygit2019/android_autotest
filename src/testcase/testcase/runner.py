from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import time
import unittest
import warnings

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '10',
    'deviceName': '24196c6a',
    'appPackage': 'com.baidu.searchbox',
    'appActivity': 'com.baidu.searchbox.SplashActivity'
}
# 'appActivity':'com.cmcc.cmvideo.main.application.CompatibleMainActivity'
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(5)
driver.find_element_by_id("com.cmcc.cmvideo:id/mgguide_page_fourth_dialog_right_btn").click()
driver.quit()
time.sleep(5)
picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
