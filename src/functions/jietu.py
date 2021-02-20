import time

def jietu(driver, path):

    picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    try:
        picture_url = driver.get_screenshot_as_file(
            path + '\\' + picture_time + '.png')
        print("%s：截图成功！！！" % picture_url)
    except BaseException as msg:
        print(msg)