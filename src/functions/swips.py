import time

def swipeUp(driver, t=800, n=1):
    """向上屏幕滑动"""
    size = driver.get_window_size()
    x1 = size["width"] * 0.5 # x坐标
    y1 = size["height"] * 0.75 # 起点 y坐标
    y2 = size["height"] * 0.28 # 终点 y 坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)
        time.sleep(2)


def swipeDown(driver, t=800, n=1):
    """向下屏幕滑动"""
    size = driver.get_window_size()
    x1 = size["width"] * 0.5 # x1 坐标
    y1 = size["height"] * 0.25 # 起点y1坐标
    y2 = size["height"] * 0.75 # 终点y2坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)
        time.sleep(2)

def swipeLeft(driver, t=500, n=1):
    """向左屏幕滑动"""
    size = driver.get_window_size()
    x1 = size["width"] * 0.75 # 起点x1坐标
    y1 = size["height"] * 0.5 # y1 坐标
    x2 = size["width"] * 0.25 # 终点x2坐标
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)
        time.sleep(2)

def swipeRight(driver, t=500, n=1):
    """向右屏幕滑动"""
    size = driver.get_window_size()
    x1 = size["width"] * 0.25 #起点x1坐标
    y1 = size["height"] * 0.5 # y1坐标
    x2 = size["width"] * 0.75 #终点x2坐标
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)
        time.sleep(2)