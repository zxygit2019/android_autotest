import time

from appium.webdriver.common.touch_action import TouchAction

from appium.webdriver import webdriver

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.1.1',
    'deviceName': 'SM-N9208',
    'appPackage': 'com.cmcc.cmvideo',
    'appActivity': 'com.cmcc.cmvideo.MainActivity'
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

def isElementPresent(by, value):
    try:
        driver.find_element(by=by, value=value)
    except Exception as e:  # 打印异常信息
        print(e)  # 发生了 NoSuchElementException异常，说明页面中未找到该元素，返回False
        return False
    else:  # 没有发生异常，表示在页面中找到了该元素，返回True
        return True



def swipeScreen_xpath():
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
#while循环10次
    i = 0
    while i < 10:
        try:
            driver.find_element_by_xpath("path").click()  # 尝试点击元素
            break
        except Exception as e:
            driver.swipe(width / 2, height * 0.8, width / 2, height * 0.2)  # 滑动屏幕
            i = i + 1

def swipeScreen_id(id):
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
#while循环10次
    i = 0
    while i < 10:
        try:
            driver.find_element_by_id(id).click()  # 尝试点击元素
            break
        except Exception as e:
            driver.swipe(width / 2, height * 0.8, width / 2, height * 0.2)  # 滑动屏幕
            i = i + 1

#获得机器屏幕大小x,y
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

#屏幕向上滑动
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)    #x坐标
    y1 = int(l[1] * 0.75)   #起始y坐标
    y2 = int(l[1] * 0.25)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)

def swipe_until(driver):
    # 进入全部菜单页等待5s
    time.sleep(5)
    flag = True
    i = 0
    while flag:
        time.sleep(2)
        try:
            driver.find_element_by_xpath("//android.widget.TextView[@text='5G超高清']").click()
            time.sleep(5)
            i = i + 1
            swipeUp(driver)
            if i == 10:
                flag = False
        except:
            swipeUp(driver)

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