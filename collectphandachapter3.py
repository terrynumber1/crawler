# collectphandachapter3.py


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# new empty set
pages = set()

def getLinks(pageUrl):
	global pages

	html = urlopen('http://en.wikipedia.org'+pageUrl)
	soup1 = BeautifulSoup(html, 'html.parser')

	try:
		print(soup1.h1.get_text())
		print(soup1.find(id='mw-content-text').findAll('p')[0])
		print(soup1.find(id='ca-edit').find('span').find('a').attrs['href'])
	except AttributeError:
		print('This page is missing something!')

	for link in soup1.findAll('a', href=re.compile('^(/wiki/)')):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				# We encountered a new page
				newPage = link.attrs['href']
				print('----------------\n' + newPage)

				pages.add(newPage)
				getLinks(newPage)

getLinks('')
