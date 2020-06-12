import smtplib
from email.mime.text import MIMEText
import time


def sendMail(user: str, content: str) -> int:
    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # SMTP服务器
    mail_user = "13615133689"  # 用户名
    mail_pass = "SWHOHGYAJOABXSUB"  # 密码(这里的密码不是登录邮箱密码，而是授权码)

    sender = '13615133689@163.com'  # 发件人邮箱
    # receivers = ['897701499@qq.com']  # 接收人邮箱
    receivers = [user]  # 接收人邮箱

    # content = 'Check me !'
    title = '请查收代码【' + time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime()) + '】'  # 邮件主题
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        # print("mail has been send successfully.")
        return 1
    except smtplib.SMTPException as e:
        # print(e)
        return 0
