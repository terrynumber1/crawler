from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
	global pages	

	html = urlopen("http://en.wikipedia.org"+pageUrl)
	bsObj = BeautifulSoup(html, 'html.parser')

	print(pages)
	for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				#We have encountered a new page
				newPage = link.attrs['href']
				print(newPage)

				pages.add(newPage)
				print(pages)
				getLinks(newPage)

# Program starts here!!!				
getLinks("")