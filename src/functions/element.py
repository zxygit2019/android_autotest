def isElementPresent(driver,by, value):
    try:
        driver.find_element(by=by, value=value)
    except Exception as e:  # 打印异常信息
        print(e)  # 发生了 NoSuchElementException异常，说明页面中未找到该元素，返回False
        return False
    else:  # 没有发生异常，表示在页面中找到了该元素，返回True
        return True
