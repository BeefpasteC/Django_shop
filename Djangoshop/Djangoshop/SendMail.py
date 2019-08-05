import smtplib #登陆邮件服务器，进行邮件发送
from email.mime.text import MIMEText #负责构建邮件格式

subject = "老边的学习邮件" #标题
content = "孩子不学习，多半是欠的，抄五遍就好了" #内容
sender = "ybw_2569@163.com" # 发件人
recver = """ybw_2569@163.com, 
ybw_2569@163.com""" #收件人

password = "ybw2569" # SMTP授权码

message = MIMEText(content,"plain","utf-8")
message["Subject"] = subject
message["To"] = recver
message["From"] = sender

smtp = smtplib.SMTP_SSL("smtp.163.com",465) # 登录服务器
smtp.login(sender,password) # 登录邮箱
smtp.sendmail(sender,recver.split(",\n"),message.as_string()) # 发送人，接收人【列表】，邮件内容
smtp.close() # 退出服务器
