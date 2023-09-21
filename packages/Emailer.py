import smtplib
from .settings import *
from email.mime.text import MIMEText

class Emailer():
	def __init__(self):
		self.emailer = {
			"account": ACCOUNT,
			"password": PASSWORD,
		}

	def sendMail(self, email, content):
		msg = MIMEText(content)
		msg["Subject"] = "Bo OK! 最新消息"
		msg["From"] = self.emailer["account"]
		msg["To"] = email
		
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		server.starttls()
		server.login(self.emailer["account"], self.emailer["password"])
		server.send_message(msg)
		server.quit()

	def sendWelcomeMessage(self, email):
		self.sendMail(email, "Hello～ 歡迎你加入我們！")
