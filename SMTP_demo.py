#coding:utf8
import sys,os
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
import smtplib

_user = '461547449@qq.com'
_pwd = 'aimtractwdeubiga'
_to = '912458418@qq.com'




msg = MIMEText('test')
msg['Subject'] = 'dont panic'
msg['From'] = _user
msg['To'] = _to

try:
        
    server = SMTP_SSL('smtp.qq.com',port=465)
    server.login(_user,_pwd)
    server.sendmail(_user,_to,msg.as_string())
    server.quit()
    print('Get it')
except smtplib.SMTPException as e:
        print('Failed',e)


#aimtractwdeubiga
