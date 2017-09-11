import mail
import schedule
import time

def check_send():
	mail.send_mail()


schedule.every(1).minutes.do(check_send)
schedule.every().hour.do(check_send)

while True:
	schedule.run_pending()
	time.sleep(1)
