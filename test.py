import urllib
import BeautifulSoup

data = urllib.urlopen('https://www.krcert.or.kr/data/secNoticeView.do?bulletin_writing_sequence=26668')
soup = BeautifulSoup.BeautifulSoup(data)
data = soup.findAll('td', attrs={'class':'cont'})

for i in data:
	data1 = i.findAll('table')
	print "\n\n"+str(data1)


