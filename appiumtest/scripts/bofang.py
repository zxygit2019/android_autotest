import self as self
from selenium import webdriver
# from appium import webdriver
import time
from appiumtest.scripts import isElementPresent
# 初始化信息

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.1.1',
    'deviceName': 'SM-N9208',
    'appPackage': 'com.cmcc.cmvideo',
    'appActivity': 'com.cmcc.cmvideo.MainActivity'
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(8)

# driver.find_element_by_id("com.cmcc.cmvideo:id/title").click()
driver.find_element_by_name("我的").click()
time.sleep(2)
driver.find_element_by_id("com.cmcc.cmvideo:id/sign_detail_tv").click()
time.sleep(2)
driver.find_element_by_name("手机号/和通行证/用户名/邮箱").click()
driver.find_element_by_name("手机号/和通行证/用户名/邮箱").send_keys("15216890993")
time.sleep(3)
driver.find_element_by_xpath("//*[@class='android.widget.EditText' and @index='1']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@class='android.widget.EditText'and @index='1']").send_keys("123456")
driver.find_element_by_name("登录").click()
time.sleep(3)
#def isElementPresent(by, value):
#    try:
#        driver.find_element(by=by, value=value)
#    except Exception as e:  # 打印异常信息
#        print(e)  # 发生了 NoSuchElementException异常，说明页面中未找到该元素，返回False
#        return False
#    else:  # 没有发生异常，表示在页面中找到了该元素，返回True
#        return True


def test_isElementPresent(self):

    res = isElementPresent.isElementPresent("name", "再试一次")
    if res is True:
        driver.find_element_by_name("再试一次").click()
    elif res is False:
        driver.find_element_by_name("确定").click()

test_isElementPresent(self)
time.sleep(2)
driver.find_element_by_class_name("android.widget.ImageView").click()
time.sleep(2)
driver.find_element_by_name("首页").click()
time.sleep(2)
driver.find_element_by_id("com.cmcc.cmvideo:id/cover_image").click()

time.sleep(8)

driver.quit()
