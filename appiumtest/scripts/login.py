from threading import Timer

from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import time
import unittest
import warnings
from src.functions import swips
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '9',
    'deviceName': '8c42cd94',
    'appPackage': 'com.cmcc.cmvideo',
    'appActivity': 'com.cmcc.cmvideo.splash.SplashActivity'
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# 'appActivity':'com.cmcc.cmvideo.main.application.CompatibleMainActivity'
#driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(5)
driver.quit()
picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

class TestAPP(unittest.TestCase):

    def test_login(self):
        warnings.simplefilter("ignore", ResourceWarning)
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        time.sleep(10)
        try:
            driver.find_element_by_id("com.cmcc.cmvideo:id/mgguide_page_fourth_dialog_right_btn").click()
        except BaseException as msg:
            print(msg)
        time.sleep(35)
        # 在搜索框输入关键词
        try:
            driver.find_element_by_id("com.cmcc.cmvideo:id/bottom_layout").click()
        except BaseException as msg:
            print(msg)
        time.sleep(3)
        driver.find_element_by_name("我的").click()

        # 等待时间
        time.sleep(5)
        try:
            driver.find_element_by_id("com.cmcc.cmvideo:id/iv_big_close").click()
        except BaseException as msg:
            print(msg)

        time.sleep(3)
        driver.find_element_by_id("com.cmcc.cmvideo:id/tv_login_tip").click()
        time.sleep(5)
        # driver.find_element_by_class_name("android.widget.EditText").click()
        # driver.find_element_by_class_name("android.widget.EditText").send_keys("15216890993")
        driver.find_element_by_name("密码登录").click()
        #driver.find_element_by_name("手机号/用户名/邮箱").click()
        #driver.find_element_by_name("手机号/用户名/邮箱").send_keys("18019974027")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@class='android.widget.EditText' and @index='2']").click()
        driver.find_element_by_xpath("//*[@class='android.widget.EditText' and @index='2']").send_keys("aaaa8888")
        time.sleep(1)
        driver.find_element_by_class_name("android.widget.Button").click()
        time.sleep(1)
        #driver.find_element_by_class_name("android.widget.Button").click()
        time.sleep(2)
        #driver.find_element_by_id("com.cmcc.cmvideo: id/iv_big_close").click()
        time.sleep(2)
        try:
            driver.find_element_by_name("刷新重试").click()
        except Exception as e:  # 打印异常信息
            print(e)  # 发生了 NoSuchElementException异常，说明页面中未找到该元素，返回False
        time.sleep(3)
        #滑屏三次到底部
        swips.swipeUp(driver, n=3)
        driver.find_element_by_xpath("//android.widget.RelativeLayout[@index = '16']").click()
        time.sleep(2)
        # 滑屏三次到底部
        swips.swipeUp(driver, n=3)
        driver.find_element_by_id("com.cmcc.cmvideo:id/uesr_set_logout").click()
        time.sleep(2)
        driver.find_element_by_id("com.cmcc.cmvideo:id/base_dialog_right_btn").click()
        time.sleep(2)
        driver.quit()