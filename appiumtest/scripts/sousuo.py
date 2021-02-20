from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import time
import unittest
# 初始化信息
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '6.0.1',
    'deviceName': 'ab97d8ad',
    'appPackage': 'com.cmcc.cmvideo',
    'appActivity': 'com.cmcc.cmvideo.splash.SplashActivity'
}
# 'appActivity':'com.cmcc.cmvideo.main.application.CompatibleMainActivity'


def retest():
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    time.sleep(7)
    driver.find_element_by_id("com.cmcc.cmvideo:id/mgguide_page_fourth_dialog_right_btn").click()
    time.sleep(35)
    # 在搜索框输入关键词
    driver.find_element_by_id("com.cmcc.cmvideo:id/bottom_layout").click()
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
    driver.find_element_by_name("手机号/用户名/邮箱").click()
    driver.find_element_by_name("手机号/用户名/邮箱").send_keys("18019974027")
    time.sleep(1)
    driver.find_element_by_xpath("//*[@class='android.widget.EditText' and @index='2']").click()
    driver.find_element_by_xpath("//*[@class='android.widget.EditText' and @index='2']").send_keys("aaaa8888")
    time.sleep(1)
    driver.find_element_by_class_name("android.widget.Button").click()
    time.sleep(1)
    driver.find_element_by_class_name("android.widget.Button").click()
    time.sleep(2)
    driver.find_element_by_name("广场").click()
    time.sleep(2)
    driver.find_element_by_name("我的").click()
    time.sleep(2)
    driver.find_element_by_name("广场").click()
    time.sleep(2)
    driver.find_element_by_id("com.cmcc.cmvideo:id/mg_simple_drawable_view").click()

    picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print(picture_time)
    try:
        picture_url = driver.get_screenshot_as_file('D:\\tool\\appium\\appiumtest\\Picture\\' + picture_time + '.png')
        print("%s：截图成功！！！" % picture_url)
    except BaseException as msg:
        print(msg)
    # 截图两张进行对比，保证播放正常
    time.sleep(5)
    try:
        picture_url = driver.get_screenshot_as_file('D:\\tool\\appium\\appiumtest\\Picture\\' + picture_time + '.png')
        print("%s：截图成功！！！" % picture_url)
    except BaseException as msg:
        print(msg)
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
        picture_url = driver.get_screenshot_as_file('D:\\tool\\appium\\appiumtest\\Picture\\' + picture_time + '.png')
        print("%s：截图成功！！！" % picture_url)
    except BaseException as msg:
        print(msg)
    driver.find_element_by_id("com.cmcc.cmvideo:id/img_bar_back").click()
    time.sleep(2)
    driver.find_element_by_name("关注").click()
    time.sleep(5)
    driver.find_element_by_xpath(
        "//android.support.v7.widget.RecyclerView[@index='0']/android.view.ViewGroup[@index='2']//android.widget.TextView[@resource-id='com.cmcc.cmvideo:id/tv_video_title']").click()
    time.sleep(4)

    # driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.cmcc.cmvideo:id/main_view']/android.view.ViewGroup[@index='2']/android.widget.TextView[@index='5']").click()
    # driver.find_element_by_xpath("//android.view.ViewGroup[@index='2']/com.cmcc.cmvideo:id/tv_video_title[index='5']").click()

    # driver.find_element_by_id("com.cmcc.cmvideo:id/intercept_touch").click()

    def isElementPresent(by, value):
        try:
            driver.find_element(by=by, value=value)
        except Exception as e:  # 打印异常信息
            print(e)  # 发生了 NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False
        else:  # 没有发生异常，表示在页面中找到了该元素，返回True
            return True

    res = isElementPresent("id", "com.cmcc.cmvideo:id/iv_full_screen")

    print(res)

    # if res is True :
    #        time.sleep(3)
    #        driver.find_element_by_id("com.cmcc.cmvideo:id/intercept_touch").click()
    #        driver.find_element_by_id("com.cmcc.cmvideo:id/intercept_touch").click()
    #        driver.find_element_by_id("com.cmcc.cmvideo:id/iv_full_screen").click()
    # else:
    #        time.sleep(3)
    #        driver.find_element_by_id("com.cmcc.cmvideo:id/intercept_touch").click()
    #        driver.find_element_by_id("com.cmcc.cmvideo:id/intercept_touch").click()
    #        driver.find_element_by_id("com.cmcc.cmvideo:id/iv_full_screen").click()

    # driver.find_element_by_id("com.cmcc.cmvideo:id/iv_full_screen").click()
    time.sleep(1)
    driver.find_element_by_id("com.cmcc.cmvideo:id/iv_back").click()
    # driver.find_element_by_xpath("//android.widget.ImageView[@index='2']").click()
    time.sleep(2)
    driver.find_element_by_name("推荐").click()
    time.sleep(2)
    driver.find_element_by_name("视频彩铃").click()
    time.sleep(2)
    try:
        picture_url = driver.get_screenshot_as_file('D:\\tool\\appium\\appiumtest\\Picture\\' + picture_time + '.png')
        print("%s：截图成功！！！" % picture_url)
    except BaseException as msg:
        print(msg)
    time.sleep(2)

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

    # 滑屏操作，查看视频彩铃是否可以正常播放
    swipeUp(1000)
    time.sleep(2)
    try:
        picture_url = driver.get_screenshot_as_file('D:\\tool\\appium\\appiumtest\\Picture\\' + picture_time + '.png')
        print("%s：截图成功！！！" % picture_url)
    except BaseException as msg:
        print(msg)
    time.sleep(5)
    time.sleep(2)
    swipeUp(1000)
    try:
        picture_url = driver.get_screenshot_as_file('D:\\tool\\appium\\appiumtest\\Picture\\' + picture_time + '.png')
        print("%s：截图成功！！！" % picture_url)
    except BaseException as msg:
        print(msg)
    time.sleep(5)
    driver.find_element_by_xpath("//android.widget.ImageView[@index='7']").click()
    time.sleep(4)
    swipeUp(1000)
    time.sleep(5)
    back = isElementPresent("id", "com.cmcc.cmvideo:id/iv_back")
    if back is True:
        driver.find_element_by_id("com.cmcc.cmvideo:id/iv_back").click()
    else:
        try:
            driver.find_element_by_id("com.cmcc.cmvideo:id/backImg").click()
        except BaseException as msg:
            print(msg)
    time.sleep(4)
    swipeUp(1000)
    time.sleep(2)
    swipeUp(1000)
    time.sleep(10)
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
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='转到上一层级']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@text='热点']").click()
    time.sleep(1)
    driver.find_element_by_id("com.cmcc.cmvideo:id/ll_more_channel").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@text='直播']").click()
    time.sleep(8)
    # 下滑三次屏幕直到可以点击云端神州的直播页面
    a = 0
    while (a < 3):
        swipeUp(1000)
        time.sleep(2)
        a = a + 1

    driver.find_element_by_name("云游大美中国").click()
    time.sleep(5)
    driver.find_element_by_id("com.cmcc.cmvideo:id/item_world_multi_vision_iv_expend").click()
    # driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@index='0']/android.view.ViewGroup[@index='3']/android.widget.TextView[@index='1']").click()
    time.sleep(4)
    # driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@index='0']/android.widget.FrameLayout[@index='0']/android.widget.FrameLayout[@index='0']/android.widget.ImageView[@index='0']").click()
    # time.sleep(5)
    # driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@index='0']/android.widget.FrameLayout[@index='1']/android.widget.FrameLayout[@index='0']/android.widget.ImageView[@index='0']").click()
    # time.sleep(5)
    driver.find_element_by_id("com.cmcc.cmvideo:id/toolbar_back").click()
    time.sleep(2)
    driver.find_element_by_name("体育").click()
    time.sleep(1)
    driver.find_element_by_name("我的").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@text='我的资产']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//android.view.View[@content-desc='通看券']").click()
    try:
        picture_url = driver.get_screenshot_as_file('D:\\tool\\appium\\appiumtest\\Picture\\' + picture_time + '.png')
        print("%s：截图成功！！！" % picture_url)
    except BaseException as msg:
        print(msg)
    time.sleep(1)
    driver.find_element_by_id("com.cmcc.cmvideo:id/backImg").click()
    # picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # print(picture_time)
    try:
        picture_url = driver.get_screenshot_as_file('D:\\tool\\appium\\appiumtest\\Picture\\' + picture_time + '.png')
        print("%s：截图成功！！！" % picture_url)
    except BaseException as msg:
        print(msg)

    time.sleep(2)
    driver.quit()



while True:
    time_now = time.strftime("%H:%M:%S", time.localtime())  # 刷新
    if time_now == "10:20:00":  # 此处设置每天定时的时间

        # 此处3行替换为需要执行的动作
        retest()
        subject = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 定时发送测试"
        print(subject)

        time.sleep(2)  # 因为以秒定时，所以暂停2秒，使之不会在1秒内执行多次