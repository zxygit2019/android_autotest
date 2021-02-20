from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import time
import unittest

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '6.0.1',
    'deviceName': 'ab97d8ad',
    'appPackage': 'com.cmcc.cmvideo',
    'appActivity': 'com.cmcc.cmvideo.splash.SplashActivity'
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# 'appActivity':'com.cmcc.cmvideo.main.application.CompatibleMainActivity'
#driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(5)
driver.find_element_by_id("com.cmcc.cmvideo:id/mgguide_page_fourth_dialog_right_btn").click()
driver.quit()
picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


def isElementPresent(by, value):
    try:
        driver.find_element(by=by, value=value)
    except Exception as e:  # 打印异常信息
        print(e)  # 发生了 NoSuchElementException异常，说明页面中未找到该元素，返回False
        return False
    else:  # 没有发生异常，表示在页面中找到了该元素，返回True
        return True

def swipe(self, start_x, start_y, end_x, end_y, duration=None):
    """Swipe from one point to another point, for an optional duration.

    Args:
        start_x (int): x-coordinate at which to start
        start_y (int): y-coordinate at which to start
        end_x (int): x-coordinate at which to stop
        end_y (int): y-coordinate at which to stop
        duration (:obj:`int`, optional): time to take the swipe, in ms.

    Usage:
        driver.swipe(100, 100, 100, 400)

    Returns:
        `appium.webdriver.webelement.WebElement`
    """
    # `swipe` is something like press-wait-move_to-release, which the server
    # will translate into the correct action
    action = TouchAction(self)
    action \
        .press(x=start_x, y=start_y) \
        .wait(ms=duration) \
        .move_to(x=end_x, y=end_y) \
        .release()
    action.perform()
    return self

def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

def swipeUp(t):
    l = []
    l = getSize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[1] * 0.25)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)

class Test(unittest.TestCase):
    def test_login(self):
        print("打开咪咕视频APP：开始登陆")
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        time.sleep(5)
        driver.find_element_by_id("com.cmcc.cmvideo:id/mgguide_page_fourth_dialog_right_btn").click()
        time.sleep(35)
        # 在搜索框输入关键词
        driver.find_element_by_id("com.cmcc.cmvideo:id/bottom_layout").click()
        time.sleep(3)
        driver.find_element_by_name("我的").click()
        # 等待时间
        time.sleep(2)
        driver.find_element_by_id("com.cmcc.cmvideo:id/tv_login_tip").click()
        time.sleep(5)
        # driver.find_element_by_class_name("android.widget.EditText").click()
        # driver.find_element_by_class_name("android.widget.EditText").send_keys("15216890993")
        driver.find_element_by_name("密码登录").click()
        driver.find_element_by_name("手机号/用户名/邮箱").click()
        driver.find_element_by_name("手机号/用户名/邮箱").send_keys("18019974027")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@class='android.widget.EditText' and @index='2']").click()
        driver.find_element_by_xpath("//*[@class='android.widget.EditText' and @index='2']").send_keys("aaaa8888")
        time.sleep(1)
        try:
            picture_url = driver.get_screenshot_as_file(
                'D:\\tool\\android_auto\\appiumtest\\Picture\\' + picture_time + '.png')
            print("%s：截图成功！！！" % picture_url)
        except BaseException as msg:
            print(msg)
        driver.find_element_by_class_name("android.widget.Button").click()
        time.sleep(1)
        driver.find_element_by_class_name("android.widget.Button").click()
        time.sleep(2)
        print("登陆测试，登陆成功，登陆账号18019974027")
        time.sleep(50)


    def test_guangchang(self):
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        time.sleep(10)
        driver.find_element_by_name("广场").click()
        time.sleep(2)
        driver.find_element_by_name("我的").click()
        time.sleep(2)
        driver.find_element_by_name("广场").click()
        time.sleep(2)
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        try:
            picture_url = driver.get_screenshot_as_file(
                'D:\\tool\\android_auto\\appiumtest\\Picture\\' + picture_time + '.png')
            print("%s：截图成功！！！" % picture_url)
        except BaseException as msg:
            print(msg)
        driver.find_element_by_id("com.cmcc.cmvideo:id/mg_simple_drawable_view").click()
        # 截图两张进行对比，保证播放正常
        time.sleep(5)
        driver.find_element_by_id("com.cmcc.cmvideo:id/iv_back").click()
        time.sleep(2)
        driver.find_element_by_id("com.cmcc.cmvideo:id/tvMore").click()
        time.sleep(2)
        driver.find_element_by_name("热门").click()
        time.sleep(2)
        driver.find_element_by_xpath(
            "//android.support.v7.widget.RecyclerView[@resource-id='com.cmcc.cmvideo:id/main_view']/android.view.ViewGroup[1]/android.widget.TextView[1]").click()
        time.sleep(2)
        driver.find_element_by_name("去圈子").click()
        time.sleep(2)
        driver.find_element_by_name("已加入").click()
        time.sleep(2)
        driver.find_element_by_id("com.cmcc.cmvideo:id/confirm").click()
        time.sleep(2)
        driver.find_element_by_id("com.cmcc.cmvideo:id/ivBack").click()
        time.sleep(2)
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        print(picture_time)
        try:
            picture_url = driver.get_screenshot_as_file(
                'D:\\tool\\appium\\appiumtest\\Picture\\' + picture_time + '.png')
            print("%s：截图成功！！！" % picture_url)
        except BaseException as msg:
            print(msg)
        driver.find_element_by_id("com.cmcc.cmvideo:id/img_bar_back").click()
        time.sleep(2)
        driver.find_element_by_name("关注").click()
        time.sleep(2)
        driver.find_element_by_id("com.cmcc.cmvideo:id/iv_start").click()
        time.sleep(2)
        driver.find_element_by_xpath(
            "//android.support.v7.widget.RecyclerView[@resource-id='com.cmcc.cmvideo:id/main_view']/android.view.ViewGroup[@index='2']/android.widget.TextView[@index='5']").click()
        # driver.find_element_by_xpath("//android.view.ViewGroup[@index='2']/com.cmcc.cmvideo:id/tv_video_title[index='5']").click()
        res = isElementPresent("id", "com.cmcc.cmvideo:id/iv_full_screen")

        print(res)
        time.sleep(1)
        driver.find_element_by_id("com.cmcc.cmvideo:id/iv_back").click()
        # driver.find_element_by_xpath("//android.widget.ImageView[@index='2']").click()
        time.sleep(2)
        driver.find_element_by_name("推荐").click()
        time.sleep(2)
        driver.find_element_by_name("视频彩铃").click()
        time.sleep(2)
        # 滑屏操作，查看视频彩铃是否可以正常播放
        swipeUp(1000)
        time.sleep(5)
        swipeUp(1000)
        time.sleep(5)
        driver.find_element_by_xpath("//android.widget.ImageView[@index='7']").click()
        time.sleep(4)
        swipeUp(1000)
        time.sleep(5)
        driver.find_element_by_id("com.cmcc.cmvideo:id/iv_back").click()
        # driver.find_element_by_xpath("//android.widget.ImageView[@index='2']").click()
        time.sleep(4)
        swipeUp(1000)
        time.sleep(2)
        swipeUp(1000)
        time.sleep(10)

    def test_shouye(self):
        driver.find_element_by_name("首页").click()
        time.sleep(5)
        # 判断首页广告弹窗是否存在，存在则点击关闭，不存在就进行下一步
        guanggao_shouye = isElementPresent("id", "com.cmcc.cmvideo:id/iv_big_close")
        # xpath://android.widget.ImageView[@index='0']
        if guanggao_shouye is True:
            driver.find_element_by_id("com.cmcc.cmvideo:id/iv_big_close").click()
            time.sleep(3)
            driver.find_element_by_id("com.cmcc.cmvideo:id/ll_more_channel").click()
        else:
            driver.find_element_by_id("com.cmcc.cmvideo:id/ll_more_channel").click()

        # //android.widget.ImageView[@index='3']
        time.sleep(5)

        fiveg = isElementPresent("xpath", "//android.widget.TextView[@text='5G超高清']")
        a = 0
        while (a < 5):
            swipeUp(1000)
            a = a + 1
            if fiveg is True:
                driver.find_element_by_xpath("//android.widget.TextView[@text='5G超高清']").click()
                break

        time.sleep(5)
        swipeUp(1000)
        time.sleep(5)
        # xpath=//android.view.ViewGroup[@index='34'],5G超高清标题xpath=//android.widget.TextView[@text='5G超高清']
        driver.find_element_by_name("5G超高清").click()
        time.sleep(5)
        swipeUp(1000)
        time.sleep(5)
        swipeUp(1000)
        driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='转到上一层级']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='转到上一层级']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.TextView[@text='热点']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.TextView[@text='直播']").click()
        time.sleep(2)

        a = 0
        while (a < 4):
            zhiboshenzhou = isElementPresent("name", "【正在直播】云端神州，俯瞰大美中国")
            print(zhiboshenzhou)
            swipeUp(1000)
            time.sleep(2)
            a = a + 1
            if zhiboshenzhou is True:
                driver.find_element_by_name("【正在直播】云端神州，俯瞰大美中国").click()
                break

        time.sleep(5)
        driver.find_element_by_xpath("//android.widget.ImageView[@index='1']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.FrameLayout[@index='2']").click()
        time.sleep(5)
        driver.quit()

    def test03(self):
        print("执行测试用例03")

if __name__ == "__main__":
    unittest.main()