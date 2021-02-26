# coding:utf-8
import time
import unittest

import HTMLTestRunner_PY3

import os

from src.functions.get_testcase import all_case
from src.functions.getallfile import getallfile
from src.functions.new_picture_path import new_picture_path
from src.functions.new_report import new_report
from src.functions.send_mail import send_mail
from src.testcase.testcase.test_MI6 import Test_MI6APP


# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")


#if __name__ == "__main__":
def run_cases():
    now = time.strftime("%Y-%m-%d %H%M%S", time.localtime(time.time()))
    print(now)
    report_path = "D:\\report\\report"
    filepath = os.path.join(report_path, now + '.html')
    print('报告存放路径  ：' + filepath)
    ts = unittest.TestSuite()
    ts.addTest(all_case())
    #ts.addTest(Test_MI6APP('test_1_login'))
    #ts.addTest(Test_MI6APP('test_guangchang'))
    #ts.addTest(Test_MI6APP('test_shipingcailing'))
    #ts.addTest(Test_MI6APP('test_shouye'))
    #ts.addTest(Test_MI6APP('test_myzichan'))
    #ts.addTest(Test_MI6APP('test_logout'))
    print(ts)
    # print(all_case())
    filename = open(filepath, 'wb')
    print(filename)
    htmlreport = HTMLTestRunner_PY3.HTMLTestRunner(stream=filename, title='咪咕视频APP冒烟测试报告',description='APP兼容性测试用例自动化测试报告')

    htmlreport.run(ts)
    filename.close()
    img_list_path = new_picture_path()
    #print(pathnow_new)
    report_html = new_report(report_path)
    send_mail(report_html, getallfile(img_list_path))


if __name__ == '__main__':
    unittest.main()
