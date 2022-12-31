# -*- coding: utf-8 -*-
import smtplib
from email.header import Header
from email.mime.text import MIMEText

from config.env_default import SERVER_MAIL, SERVER_MAIL_HOST, SERVER_MAIL_PORT, SERVER_MAIL_PASS
from config.log_conf import logger


# remember 1. 邮件依赖不稳定服务,, 2. 同时大量异常导致邮件多发--导致异常
# 策略: 长链接, 连接池, 生产消费者
def send_email(mail_content, mail_to, subject="master,your mail", mime_text_type='plain'):
    message = MIMEText(mail_content, mime_text_type, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header("明宇致和", 'utf-8')
    message['To'] = Header("朋友", 'utf-8')

    with smtplib.SMTP_SSL(SERVER_MAIL_HOST, SERVER_MAIL_PORT) as smtp_obj:
        # smtp_obj.set_debuglevel(1)
        smtp_obj.login(SERVER_MAIL, SERVER_MAIL_PASS)
        smtp_obj.sendmail(SERVER_MAIL, mail_to, message.as_string())
        logger.info("邮件发送成功")


if __name__ == '__main__':
    send_email("hello world", '1134614268@qq.com')
