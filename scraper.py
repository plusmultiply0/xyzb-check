import os
import smtplib
import requests
from bs4 import BeautifulSoup

# 获取环境变量
login_url = 'https://xyzb.yuanfudao.com/task/main'
cookie = os.getenv("COOKIE")
keyword = ''
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
email_user = os.getenv("EMAIL_USER")
email_pass = os.getenv("EMAIL_PASS")


# 登录请求
headers = {"Connection": 'keep-alive',
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "Cache-Control": 'no-cache',
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
           "accept": "*/*",
           "connection": "Keep-Alive",
           "Accept-Encoding": "gzip,deflate",
           "Cookie": cookie
           }

# 请求目标页面
response = requests.post(url=login_url, headers=headers)
print(response.text)

# # 检查关键字是否存在
# if keyword.lower() in soup.text.lower():
#     print("Product is available! Sending notification...")

#     # 发送邮件通知
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
#         server.login(email_user, email_pass)
#         subject = "Product Available Notification"
#         body = f"The product with keyword '{keyword}' is now available at {target_url}."
#         msg = f"Subject: {subject}\n\n{body}"
        
#         server.sendmail(email_user, recipient, msg)
# else:
#     print("Product not found.")
