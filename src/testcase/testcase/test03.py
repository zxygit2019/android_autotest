import warnings
import time

from src.functions import swips
from src.functions.driver_now import qudong_MI6


def test():
    warnings.simplefilter("ignore", ResourceWarning)
    driver = qudong_MI6()
    time.sleep(8)
    driver.find_element_by_id("com.cmcc.cmvideo:id/ll_more_channel").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@text='直播']").click()
    time.sleep(8)
    try:
        driver.find_element_by_name("允许").click()
    except Exception as e:  # 打印异常信息
        print(e)  # 发生了 NoSuchElementException异常，说明页面中未找到该元素，返回False
    # 下滑三次屏幕直到可以点击云端神州的直播页面
    swips.swipeUp(driver, n=3)
    time.sleep(2)
    driver.find_element_by_name("印象南塘 烟雨江南").click()
    time.sleep(5)

test()