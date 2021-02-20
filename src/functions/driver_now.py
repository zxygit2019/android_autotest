from appium import webdriver
def qudong_MI6():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '9',
        'deviceName': '8c42cd94',
        'appPackage': 'com.cmcc.cmvideo',
        'appActivity': 'com.cmcc.cmvideo.splash.SplashActivity'
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    return driver

def qudong_oppo9():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '8.1.0',
        'deviceName': 'c98b3cce',
        'appPackage': 'com.cmcc.cmvideo',
        'appActivity': 'com.cmcc.cmvideo.splash.SplashActivity'
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    return driver

