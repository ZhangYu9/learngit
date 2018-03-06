#coding=utf-8
import smtplib
from email.mime.text import MIMEText
msg_from='2509048189@qq.com'                                 
passwd='kfkodlxgvcgneajd'
#jwtwwgjzbaxoebfj
msg_to='2509048189@qq.com'                                 
                            
subject="python邮件测试"                                        
content="这是我使用python smtplib及email模块发送的邮件"
#test
#test2
#test3
msg=MIMEText('填写邮件内容','plain','utf-8')
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, [msg_to,], msg.as_string())
    print "发送成功"
except :
    print "发送失败"
finally:
    s.quit()
