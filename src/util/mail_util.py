# -*- coding: utf-8 -*-
import smtplib
import traceback
from email.header import Header
from email.mime.text import MIMEText

from config.conf import SERVER_MAIL, SERVER_MAIL_HOST, SERVER_MAIL_PASS, SERVER_MAIL_PORT
from util.log_util import logger as log


def send_email(mail_content, mail_to, subject="master,your mail"):
    message = MIMEText(mail_content, 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header("明宇致和", 'utf-8')
    message['To'] = Header("朋友", 'utf-8')

    #     # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    #     with open('''D:\\py\\www\\img\\android-icon.png''', 'rb') as f:
    #         # 设置附件的MIME和文件名，这里是png类型:
    #         mime = MIMEBase('image', 'png', filename='android-icon.png')
    #         # 加上必要的头信息:
    #         mime.add_header('Content-Disposition', 'attachment', filename='android-icon.png')
    #         mime.add_header('Content-ID', '<0>')
    #         mime.add_header('X-Attachment-Id', '0')
    #         # 把附件的内容读进来:
    #
    #         mime.set_payload(f.read())
    #         # 用Base64编码:
    #         encoders.encode_base64(mime)
    #         # 添加到MIMEMultipart:
    #         message.attach(mime)

    try:
        smtp_obj = smtplib.SMTP_SSL(SERVER_MAIL_HOST, SERVER_MAIL_PORT)
        # smtp_obj.set_debuglevel(1)
        smtp_obj.login(SERVER_MAIL, SERVER_MAIL_PASS)
        smtp_obj.sendmail(SERVER_MAIL, mail_to, message.as_string())
        log.info("邮件发送成功")
    except smtplib.SMTPException:
        traceback.print_exc()
        # 日志记录异常信息
        message = traceback.format_exc()
        # 邮件服务 发送异常通知邮件  邮件模板
        log.error("Error: 无法发送邮件.[原因]" + message)
    finally:
        smtp_obj.quit()


if __name__ == '__main__':
    send_email("hello world", '1134614268@qq.com')
