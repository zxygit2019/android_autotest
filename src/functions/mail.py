#!/usr/bin/env python3
# coding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

'''
发送多张图片邮件的python代码
'''
img_list = 'd:\\tool\\android_auto\\appiumtest\\Picture\\2021-02-05-14-11'
allfile = []

'''
遍历文件夹获得所有图片绝对路径
'''


def getallfile(path):
    allfilelist = os.listdir(path)
    for file in allfilelist:
        filepath = os.path.join(path, file)
        if os.path.isdir(filepath):
            getallfile(filepath)
        else:
            allfile.append(filepath)
    print(filepath)
    return allfile


def sendmail(filelist):
    sender = 'zhaixingyu@migu.cn'
    receiver = '327615230@qq.com'
    subject = '咪咕视频APP自动化测试报告'
    smtpserver = 'mail.migu.cn'
    # 发送邮箱用户名密码
    user = 'zhaixingyu@migu.cn'
    # smp 如果是qq邮箱是输入指定授权码
    password = 'migu202016!@'

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'python email'
    '''
    图片id加入所在位置 
    '''
    content = '<b>Some <i>HTML</i> text</b> and an image.<br>'
    for index in range(len(filelist)):
        if index % 2 == 0:
            content += '<img src="cid:' + str(index) + '"><br>'
        else:
            content += '<img src="cid:' + str(index) + '">'

    msgText = MIMEText(content, 'html', 'utf-8')
    msgRoot.attach(msgText)

    '''
    将图片和id位置对应起来
    '''
    index = 0
    for file in filelist:
        fp = open(file, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', '<' + str(index) + '>')
        index += 1
        msgRoot.attach(msgImage)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    # SSL协议端口号使用456
    smtp = smtplib.SMTP_SSL(smtpserver, 465)

    # 向服务器标识用户身份
    smtp.helo(smtpserver)
    # 服务器返回结果确认
    smtp.ehlo(smtpserver)
    # 登录邮箱账户密码
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    print("邮件发送成功")
    smtp.quit()


if __name__ == '__main__':
    sendmail(getallfile(img_list))