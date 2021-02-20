import time
import unittest
import warnings
from src.functions import swips, mkdir
from src.functions.driver_now import qudong_MI6
from src.functions.element import isElementPresent
from src.functions import jietu

class Test_MI6APP(unittest.TestCase):
    '''开始进行咪咕视频APP自动化测试'''
    @classmethod
    def setUpClass(self):
       '''这是前置函数，以后可以添加各种前置条件执行的代码'''
       warnings.simplefilter("ignore", ResourceWarning)
       self.driver = qudong_MI6()
       time.sleep(5)
       try:
           self.driver.find_element_by_id("com.cmcc.cmvideo:id/mgguide_page_fourth_dialog_right_btn").click()
       except BaseException as msg:
           print(msg)
       time.sleep(3)
       try:
           self.driver.find_element_by_id("com.cmcc.cmvideo:id/skip_button").click()
       except BaseException as msg:
           print(msg)
       picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
       self.pathnow = mkdir.mkdir("d:\\tool\\android_auto\\appiumtest\\Picture\\" + time.strftime("%Y-%m-%d-%H-%M",
                                                                                             time.localtime(
                                                                                                 time.time())) + "\\")
       print("当前照片存储文件夹为：" + self.pathnow)
       size = self.driver.get_window_size()
       # 屏幕的宽度 width
       print("当前手机的屏幕宽度是: " + str(size["width"]))
       # 屏幕的高度 height
       print("当前手机的屏幕高度是：" + str(size["height"]))

    def test_1_login(self):
        '''登陆测试脚本，登陆账号为：18019974027'''
        driver=self.driver
        pathnow=self.pathnow
        warnings.simplefilter("ignore", ResourceWarning)
        #driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        time.sleep(5)
        try:

            driver.find_element_by_id("com.cmcc.cmvideo:id/mgguide_page_fourth_dialog_right_btn").click()
        except BaseException as msg:
            print(msg)
        time.sleep(5)
        try:
            driver.find_element_by_id("com.cmcc.cmvideo:id/bottom_layout").click()
        except BaseException as msg:
            print(msg)
        #time.sleep(35)
        time.sleep(3)
        driver.find_element_by_name("我的").click()
        print("截图地址是:" + pathnow)
        jietu.jietu(driver, pathnow)
        # 等待时间
        time.sleep(5)
        try:
            driver.find_element_by_id("com.cmcc.cmvideo:id/iv_big_close").click()
        except BaseException as msg:
            print(msg)

        time.sleep(2)
        driver.find_element_by_id("com.cmcc.cmvideo:id/tv_login_tip").click()
        time.sleep(2)
        # driver.find_element_by_class_name("android.widget.EditText").click()
        # driver.find_element_by_class_name("android.widget.EditText").send_keys("15216890993")
        driver.find_element_by_name("密码登录").click()
        time.sleep(2)
        try:
            driver.find_element_by_name("手机号/用户名/邮箱").click()
            driver.find_element_by_name("手机号/用户名/邮箱").clear()
        except BaseException as msg:
            print(msg)
        time.sleep(2)
        try:
            driver.find_element_by_xpath(
                "//android.widget.RelativeLayout[@index='1']/android.widget.EditText[@index='0']").click()
            driver.find_element_by_xpath(
                "//android.widget.RelativeLayout[@index='1']/android.widget.EditText[@index='0']").clear()
        except BaseException as msg:
            print(msg)
        time.sleep(2)
        driver.find_element_by_name("手机号/用户名/邮箱").send_keys("18019974027")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@class='android.widget.EditText' and @index='2']").click()
        driver.find_element_by_xpath("//*[@class='android.widget.EditText' and @index='2']").send_keys("aaaa8888")
        time.sleep(1)
        driver.find_element_by_class_name("android.widget.Button").click()
        time.sleep(2)
        try:
            driver.find_element_by_class_name("android.widget.Button").click()
            time.sleep(4)
        except BaseException as msg:
            print(msg)
        try:
            driver.find_element_by_id("com.cmcc.cmvideo:id/mgguide_page_fourth_dialog_right_btn").click()
        except BaseException as msg:
            print(msg)
        time.sleep(5)
        try:
            driver.find_element_by_id("com.cmcc.cmvideo:id/bottom_layout").click()
        except BaseException as msg:
            print(msg)
        # 等待时间
        try:
            driver.find_element_by_id("com.cmcc.cmvideo:id/iv_big_close").click()
        except BaseException as msg:
            print(msg)

        print("登陆成功：登陆账号：18019974027")
        time.sleep(2)

    def test_2_guangchang(self):
        '''登陆完成后进入广场页面以及圈子和播放圈子里的视频脚本'''
        driver=self.driver
        pathnow=self.pathnow
        try:
            driver.find_element_by_id("com.cmcc.cmvideo:id/mgguide_page_fourth_dialog_right_btn").click()
        except BaseException as msg:
            print(msg)
        time.sleep(5)
        try:
            driver.find_element_by_id("com.cmcc.cmvideo:id/bottom_layout").click()
        except BaseException as msg:
            print(msg)
        driver.find_element_by_name("广场").click()
        time.sleep(2)
        driver.find_element_by_name("我的").click()
        time.sleep(2)
        driver.find_element_by_name("广场").click()
        time.sleep(5)
        # swips.swipeDown(driver, n=1)
        # time.sleep(5)
        driver.find_element_by_id("com.cmcc.cmvideo:id/mg_simple_drawable_view").click()

        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        print(picture_time)
        jietu.jietu(driver, pathnow)
        # 截图两张进行对比，保证播放正常
        time.sleep(8)
        #picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        jietu.jietu(driver, pathnow)
        driver.find_element_by_id("com.cmcc.cmvideo:id/iv_back").click()
        print("广场页面视频播放截图对比成功")
        time.sleep(3)
        driver.find_element_by_id("com.cmcc.cmvideo:id/tvMore").click()
        time.sleep(3)
        driver.find_element_by_name("热门").click()
        time.sleep(3)
        driver.find_element_by_xpath(
            "//android.support.v7.widget.RecyclerView[@resource-id='com.cmcc.cmvideo:id/main_view']/android.view.ViewGroup[@index='1']/android.widget.TextView[@resource-id='com.cmcc.cmvideo:id/tv_circle_join']").click()
        time.sleep(3)
        driver.find_element_by_name("去圈子").click()
        time.sleep(3)
        driver.find_element_by_name("已加入").click()
        time.sleep(3)
        driver.find_element_by_id("com.cmcc.cmvideo:id/confirm").click()
        time.sleep(4)
        driver.find_element_by_id("com.cmcc.cmvideo:id/ivBack").click()
        time.sleep(3)
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        print(picture_time)
        jietu.jietu(driver, pathnow)
        time.sleep(3)
        driver.find_element_by_id("com.cmcc.cmvideo:id/img_bar_back").click()
        time.sleep(3)
        driver.find_element_by_name("关注").click()
        time.sleep(5)
        swips.swipeDown(driver, n=1)
        time.sleep(3)
        driver.find_element_by_xpath(
            "//android.support.v7.widget.RecyclerView[@index='1']/android.view.ViewGroup[@index='2']/android.widget.TextView[@resource-id='com.cmcc.cmvideo:id/tv_video_title']").click()
        time.sleep(4)
        print("广场关注页面进入成功")
        # driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.cmcc.cmvideo:id/main_view']/android.view.ViewGroup[@index='2']/android.widget.TextView[@index='5']").click()
        # driver.find_element_by_xpath("//android.view.ViewGroup[@index='2']/com.cmcc.cmvideo:id/tv_video_title[index='5']").click()

        # driver.find_element_by_id("com.cmcc.cmvideo:id/intercept_touch").click()

        res = isElementPresent(driver, "id", "com.cmcc.cmvideo:id/iv_full_screen")

        print(res)
        time.sleep(3)
        driver.find_element_by_id("com.cmcc.cmvideo:id/iv_back").click()
        # driver.find_element_by_xpath("//android.widget.ImageView[@index='2']").click()
        time.sleep(3)

    def test_3_shipingcailing(self):
        '''进入视频彩铃页面并且播放以及上下滑动查看视频彩铃'''
        driver=self.driver
        pathnow=self.pathnow
        driver.find_element_by_name("推荐").click()
        time.sleep(3)
        driver.find_element_by_name("视频彩铃").click()
        time.sleep(3)
        print("进入视频彩铃页面并且截图成功")
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        jietu.jietu(driver, pathnow)
        time.sleep(2)

        # 滑屏操作，查看视频彩铃是否可以正常播放
        swips.swipeUp(driver, n=1)
        time.sleep(2)
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        jietu.jietu(driver, pathnow)
        time.sleep(2)
        swips.swipeUp(driver, n=1)
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        jietu.jietu(driver, pathnow)
        time.sleep(5)
        driver.find_element_by_xpath("//android.widget.ImageView[@index='7']").click()
        time.sleep(4)
        swips.swipeUp(driver, n=1)
        time.sleep(5)
        back = isElementPresent(driver, "id", "com.cmcc.cmvideo:id/iv_back")
        if back is True:
            driver.find_element_by_id("com.cmcc.cmvideo:id/iv_back").click()
        else:
            try:
                driver.find_element_by_id("com.cmcc.cmvideo:id/backImg").click()
            except BaseException as msg:
                print(msg)
        time.sleep(4)
        swips.swipeUp(driver, n=2)

        time.sleep(10)
        print("滑屏成功，查看截图对比滑屏前后页面变化")
        try:
            driver.find_element_by_id("com.cmcc.cmvideo:id/iv_back").click()
        except BaseException as msg:
            print(msg)
        time.sleep(2)

    def test_4_shouye(self):
        '''返回首页查看5G超高清以及直播内容'''
        driver=self.driver
        pathnow=self.pathnow
        driver.find_element_by_name("首页").click()
        time.sleep(5)
        # 判断首页广告弹窗是否存在，存在则点击关闭，不存在就进行下一步
        try:
            driver.find_element_by_id("com.cmcc.cmvideo:id/iv_big_close").click()
        except Exception as e:  # 打印异常信息
            print(e)  # 发生了 NoSuchElementException异常，说明页面中未找到该元素，返回False
        guanggao_shouye = isElementPresent(driver, "id", "com.cmcc.cmvideo:id/iv_big_close")
        # xpath://android.widget.ImageView[@index='0']
        if guanggao_shouye is True:
            driver.find_element_by_id("com.cmcc.cmvideo:id/iv_big_close").click()
            time.sleep(3)
            driver.find_element_by_id("com.cmcc.cmvideo:id/ll_more_channel").click()
        else:
            driver.find_element_by_id("com.cmcc.cmvideo:id/ll_more_channel").click()

        # //android.widget.ImageView[@index='3']
        time.sleep(5)

        fiveg = isElementPresent(driver, "xpath", "//android.widget.TextView[@text='5G超高清']")
        a = 0
        while (a < 5):
            swips.swipeUp(driver, n=1)
            a = a + 1
            if fiveg is True:
                driver.find_element_by_xpath("//android.widget.TextView[@text='5G超高清']").click()
                break

        time.sleep(5)
        swips.swipeUp(driver, n=1)
        time.sleep(5)
        # xpath=//android.view.ViewGroup[@index='34'],5G超高清标题xpath=//android.widget.TextView[@text='5G超高清']
        driver.find_element_by_name("5G超高清").click()
        print("进入菜单页面-5G超高清页面")
        time.sleep(5)
        swips.swipeUp(driver, n=1)
        time.sleep(5)
        swips.swipeUp(driver, n=1)
        driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='转到上一层级']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='转到上一层级']").click()
        time.sleep(3)
        try:
            driver.find_element_by_id("com.cmcc.cmvideo:id/iv_big_close").click()
        except Exception as e:  # 打印异常信息
            print(e)  # 发生了 NoSuchElementException异常，说明页面中未找到该元素，返回False
        driver.find_element_by_xpath("//android.widget.TextView[@text='热点']").click()
        time.sleep(1)
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
        time.sleep(3)
        driver.find_element_by_name("体育").click()
        print("进入体育菜单页面")
        time.sleep(3)
        try:
            driver.find_element_by_id("com.cmcc.cmvideo:id/iv_big_close").click()
        except Exception as e:  # 打印异常信息
            print(e)  # 发生了 NoSuchElementException异常，说明页面中未找到该元素，返回False
        driver.find_element_by_name("我的").click()
        time.sleep(3)
    def test_5_myzichan(self):
        driver=self.driver
        pathnow=self.pathnow
        '''进入我的页面，进入通看券tab页，查看个人资产并且截图'''
        try:
            driver.find_element_by_name("刷新重试").click()
        except Exception as e:  # 打印异常信息
            print(e)  # 发生了 NoSuchElementException异常，说明页面中未找到该元素，返回False
        time.sleep(2)
        try:
            driver.find_element_by_id("com.cmcc.cmvideo:id/iv_big_close").click()
        except Exception as e:  # 打印异常信息
            print(e)  # 发生了 NoSuchElementException异常，说明页面中未找到该元素，返回False
        time.sleep(4)
        driver.find_element_by_xpath("//android.widget.TextView[@text='我的资产']").click()
        time.sleep(8)
        driver.find_element_by_xpath("//android.view.View[@text='通看券']").click()
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        jietu.jietu(driver, pathnow)
        time.sleep(1)
        print("进入我的菜单页--我的资产--通看券页面，查看当前账号下的资产并且截图")
        driver.find_element_by_id("com.cmcc.cmvideo:id/backImg").click()
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        print(picture_time)
        jietu.jietu(driver, pathnow)
        time.sleep(2)

    def test_6_logout(self):
        '''退出登陆账号，完成测试闭环'''
        driver=self.driver
        pathnow=self.pathnow
        time.sleep(2)
        a = 0
        while (a < 3):
            swips.swipeUp(driver, n=1)
            time.sleep(2)
            a = a + 1
        try:
            #driver.find_element_by_xpath("//android.widget.RelativeLayout[@index = '13']").click()
            driver.find_element_by_name("我的设置").click()
        except Exception as e:  # 打印异常信息
            print(e)  # 发生了 NoSuchElementException异常，说明页面中未找到该元素，返回False

        time.sleep(2)
        a = 0
        while (a < 3):
            swips.swipeUp(driver, n=1)
            time.sleep(2)
            a = a + 1
        driver.find_element_by_id("com.cmcc.cmvideo:id/uesr_set_logout").click()
        time.sleep(2)
        driver.find_element_by_id("com.cmcc.cmvideo:id/base_dialog_right_btn").click()
        time.sleep(2)
        driver.quit()

    #def test_end(self):
     #   print("咪咕视频APP冒烟测试用例结束")
if __name__ == "__main__":
    unittest.main()