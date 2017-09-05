#coding:utf8
import os
from smtplib import SMTP_SSL
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import smtplib

_user = '461547449@qq.com'
_pwd = 'enamwkhnwbdjbjci'       #登陆QQsmtp服务器密码
_to = '461547449@qq.com'


msg = MIMEMultipart()								#创建多文本格式的传输类型
msg.attach(MIMEText('test','plain','utf-8'))         #发送的文本内容
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open(os.getcwd()+'\liuyan.jpg','rb') as f:
	# 设置附件的MIME和文件名，这里是png类型:
	mime = MIMEBase('image','png',filename='liuyan.jpg')
	# 设置必要的头信息
	mime.add_header('Content-Disposition','attachment',filename='liuyan.jpg')
	mime.add_header('Content-ID','<0>')
	mime.add_header('X-Attachment-Id','0')
	#把附件内容读进来
	mime.set_payload(f.read())
	#将信息用Base64编码
	encoders.encode_base64(mime)
	msg.attach(mime)

msg['Subject'] = '12-方玉锋-py201706017'    #主题信息
msg['From'] = _user              			#己方地址
msg['To'] = _to                  			#对方地址

try:        
    server = SMTP_SSL('smtp.qq.com',port=465)   #QQsmtp服务器,端口号固定465,SMTP_SSL加密的SMTP传输方法
    server.login(_user,_pwd)                       #登陆
    server.sendmail(_user,_to,msg.as_string())     #(发送方,接收方,信息)
    server.quit()
    print('Get it')
except smtplib.SMTPException as e:
        print('Failed',e)

#----------------------上面图片等内容作为附件传输-----------------------------#


#----------------------下面图片是作为正文传输---------------------------------#

msg = MIMEMultipart()								#创建多文本格式的传输类型
msg.attach(MIMEText('<html><body><img src="cid:0"/></body></html>',
						'html',
						'utf-8'))         #发送的文本内容
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open(os.getcwd()+'\liuyan.jpg','rb') as f:
	# 设置附件的MIME和文件名，这里是png类型:
	mime = MIMEBase('image','png',filename='liuyan.jpg')
	# 设置必要的头信息
	mime.add_header('Content-Disposition','attachment',filename='liuyan.jpg')
	mime.add_header('Content-ID','<0>')
	mime.add_header('X-Attachment-Id','0')
	#把附件内容读进来
	mime.set_payload(f.read())
	#将信息用Base64编码
	encoders.encode_base64(mime)
	msg.attach(mime)

msg['Subject'] = '12-方玉锋-py201706017'    #主题信息
msg['From'] = _user              			#己方地址
msg['To'] = _to                  			#对方地址

try:        
    server = SMTP_SSL('smtp.qq.com',port=465)   #QQsmtp服务器,端口号固定465,SMTP_SSL加密的SMTP传输方法
    server.login(_user,_pwd)                       #登陆
    server.sendmail(_user,_to,msg.as_string())     #(发送方,接收方,信息)
    server.quit()
    print('Get it')
except smtplib.SMTPException as e:
        print('Failed',e)