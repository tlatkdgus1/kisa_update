# -*- coding:utf-8 -*-

import smtplib
from email.mime.text  import MIMEText

from core import *
import time


def send_mail():
	data = get_data()

	if data['status'] == "new":
		text = "[+]New notice!!\n\n"
		text += data['text']+"\n"
		text += data['url']+"\n\n\n"
		form = get_form(data['url']).decode('utf-8')
		form = form.replace("<br />", "\n")
		form = form.replace("<tr>", "")
		form = form.replace("</tr>", "")
		form = form.replace("<td>", "")
		form = form.replace("</td>", "")
		form = form.replace("&nbsp;o", " ")
		form = form.replace("&nbsp;", "")
		form = form.replace("<table>", "")
		form = form.replace("</table>", "")
		form = form.replace("<p>", "")
		form = form.replace("</p>", "")
		form = form.replace("<u>", "")
		form = form.replace("</u>", "")
		form = form.replace("<a>", "")
		form = form.replace("</a>", "")
		form = form.replace("&lsquo;", "'")
		form = form.replace("&rsquo;", "'")
		form = form.replace("<a href=\"", "")
		form = form.replace("\">", "")
		text += form
		print text
	
		smtp = smtplib.SMTP('smtp.live.com', 587)
		smtp.ehlo()  # say Hello
		smtp.starttls()  # TLS 사용시 필요
		smtp.login('tlatkdgus1@gmail.com', 'secret')
	
		msg = MIMEText(text.encode('utf-8').strip())
		now = time.localtime()
		s = "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
		msg['Subject'] = 'Kisa 취약점 업데이트 '+str(s)
		msg['To'] = 'shsim@monitorapp.com'
		smtp.sendmail('tlatkdgus1@gmail.com', 'shsim@monitorapp.com', msg.as_string())
		msg['To'] = 'smryu@monitorapp.com'
                smtp.sendmail('tlatkdgus1@gmail.com', 'smryu@naver.com', msg.as_string())


		
		#smtp.sendmtp.sendmail('tlatkdgus1@gmail.com', 'shsim@monitorapp.com', msg.as_string())

		
	
	
		smtp.quit()

send_mail()
