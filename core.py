#-*- coding: utf-8 -*-

import urllib
import BeautifulSoup
import re

notice_table = None

def set_noticeTable(notice):
	global notice_table
	notice_table = notice

def get_recent():
	index = 0
	for i in notice_table:
		data = i.findAll('td', attrs={'class':'gray'})
		while True:
			if str(data[index]).find("[공지]") is not -1:
				index = index+3
			else:
				return data[index]
				break;


def get_num():
	data = str(get_recent())
        regex = re.compile('[0-9]+')
        match = regex.search(data)
        match = match.group()
	
	return match

def check_new():
	match = get_num()

        f = open('number', 'r')
        recent = f.read()
        f.close()

        if int(str(match)) > int(str(recent)):
                f = open('number', 'w')
                f.write(match)
                f.close()
                return True
        else:
                return False

def get_data():
	data = urllib.urlopen('https://www.krcert.or.kr/data/secNoticeList.do')
	soup = BeautifulSoup.BeautifulSoup(data)
	set_noticeTable(soup.findAll('table'))
	
	if check_new() == True:
		for i in notice_table:
			tr_1 = i.findAll('tr')
			for j in tr_1:
				if str(j).find(str(get_num())) is not -1:
					dict = {
						'status' : "new",
						'url' : "https://www.krcert.or.kr"+j.find('a')['href'],
						'text' : j.find('a').contents[0]
					}
					return dict
	else:
		dict = {
			'status' : "old"
		}
		return dict
