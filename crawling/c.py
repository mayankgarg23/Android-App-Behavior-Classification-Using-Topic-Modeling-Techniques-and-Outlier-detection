import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')	

def trade_spider():
	url = 'https://play.google.com/store/apps/details?id=net.one97.paytm'
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text,"html.parser")
	for link in soup.findAll('div' , {'class': 'featured-review' }):
	#href ="https://play.google.com" + link.get('href')
		"""href=url	
		sc2 = requests.get(href)
		pt = sc2.text
		soup1 = BeautifulSoup(pt,"html.parser")"""
		for link2 in link.find('div' , {'class': 'review-text'}):	
			tit = link2.string
			print(tit)


trade_spider()
