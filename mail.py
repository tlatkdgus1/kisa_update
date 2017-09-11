# -*- coding:utf-8 -*-

import smtplib
from email.mime.text  import MIMEText

from core import *
import time

data = get_data()

if data['status'] == "new":
	text = "[+]New notice!!\n\n"
	text += data['text']+"\n"
	text += data['url']
	print text

	smtp = smtplib.SMTP('smtp.live.com', 587)
	smtp.ehlo()  # say Hello
	smtp.starttls()  # TLS 사용시 필요
	smtp.login('tlatkdgus1@gmail.com', 'secret')

	msg = MIMEText(text.encode('utf-8').strip())
	now = time.localtime()
	s = "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
	msg['Subject'] = 'Kisa 취약점 업데이트 '+str(s)
	msg['To'] = 'ipod1597@naver.com'
	smtp.sendmail('tlatkdgus1@gmail.com', 'ipod1597@naver.com', msg.as_string())


	smtp.quit()
