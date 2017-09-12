# -*- coding:utf-8 -*-

import smtplib
from email.mime.text  import MIMEText

from core import *
import time

def mailSend(msg):
	HOST = 'mail.monitorapp.com'
	me = 'shsim@monitorapp.com'
	you = 'shsim@monitorapp.com'

	contents = msg
	now = time.localtime()
	s = "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
	msg = MIMEText(contents, _charset='euc-kr')
	msg['Subject'] = u'Kisa 취약점 업데이트 '.encode('euc-kr')+str(s)
	msg['From'] = me
	msg['To'] = you

	s = smtplib.SMTP(HOST)
	s.ehlo()  # say Hello
	s.starttls()  # TLS 사용시 필요
#	s.login(me, '1234asdf')
	s.sendmail(me, you, msg.as_string()) # [you] --> error
	s.quit()

def send_mail():
	data = get_data()

	if data['status'] == "new":
		text = "[+]New notice!!\n\n"
		text += data['text']+"\n"
		text += data['url']+"\n\n\n"
		text += get_form(data['url']).decode('utf-8')
		print (text)
	
		mailSend(text)

send_mail()
