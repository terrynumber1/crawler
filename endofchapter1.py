from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None

	try:

		bsObject = BeautifulSoup(html.read(), 'html.parser')
		title = bsObject.body.h1
	except AttributeError as e:
		return None

	return title

title = getTitle('http://www.littlethaiatl.com')
print(title)
