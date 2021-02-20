import configparser

import os

curpath = "D:\\tool\\android_auto\\config"

cfgpath = os.path.join(curpath, "conf.ini")

print(cfgpath)  # cfg.ini的路径

# 创建管理对象

conf = configparser.ConfigParser()

# 读ini文件

conf.read(cfgpath, encoding="utf-8")  # python3

# conf.read(cfgpath)  # python2


# 获取所有的section

sections = conf.sections()

print(sections)  # 返回list

items = conf.items("send_email")

print(items)  # list里面对象是元祖

smtpserver = conf.get('send_email', 'smtp_server')

print(smtpserver)