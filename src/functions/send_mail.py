import os
import smtplib
import configparser
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def send_mail(latest_report,filelist):
	# 读取测试报告内容
    f = open(latest_report,'rb')
    mail_content = f.read()
    # print(latest_report.file)
    # print(mail_content)
    f.close()
    # 发送邮件
    curpath = "D:\\tool\\android_auto\\config"

    cfgpath = os.path.join(curpath, "conf.ini")

    print(cfgpath)  # cfg.ini的路径

    # 创建管理对象

    conf = configparser.ConfigParser()

    # 读ini文件

    conf.read(cfgpath, encoding="utf-8")  # python3 # conf.read(cfgpath)  # python2

    # 获取所有的section
    #sections = conf.sections()
    #items = conf.items('send_email')

    # 发送邮箱服务器
    smtpserver = conf.get('send_email','smtp_server')

    # 发送邮箱用户名密码
    user = conf.get('send_email','sender')
    # smp 如果是qq邮箱是输入指定授权码
    password = conf.get('send_email','psw')

    # 发送和接收邮箱
    sender = conf.get('send_email','sender')
    receive = [conf.get('reserver','reserver')]
    #receive = ['zhaixingyu@migu.cn,327615230@qq.com']
    # 多用户发送

    # 发送邮件主题
    subject = '咪咕视频APP自动化测试报告'
    # 构造html附件内容
    send_file = open(latest_report, 'rb').read()
    att = MIMEText(send_file, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    # 取文件名作为 发送附件的名字
    att["Content-Disposition"] = 'attachment;filename="{}"'.format(latest_report[12:])

    content = '<b>测试报告中包含 <i>HTML</i> 文档附件以及</b> 自动化测试运行中的所有截图文件<br>'
    msgRoot = MIMEMultipart()
    msgRoot.attach(MIMEText(mail_content, 'html', 'utf-8'))

    #构造截图作为附件内容

    index = 0
    for file in filelist:
        fp = open(file, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', '<' + str(index) + '>'+'.png')
        index += 1
        msgRoot.attach(msgImage)

    msgRoot.attach(att)
    msgRoot['Subject'] = Header(subject, 'utf-8')
    msgRoot['From'] = 'zhaixingyu@migu.cn'
    msgRoot['To'] = ','.join(receive)

    # SSL协议端口号使用456
    smtp = smtplib.SMTP_SSL(smtpserver, 465)

    # 向服务器标识用户身份
    smtp.helo(smtpserver)
    # 服务器返回结果确认
    smtp.ehlo(smtpserver)
    # 登录邮箱账户密码
    smtp.login(user, password)

    print('开始发送邮件')
    smtp.sendmail(sender, msgRoot['To'].split(','), msgRoot.as_string())
    smtp.quit()
    print('邮件发送完成')
