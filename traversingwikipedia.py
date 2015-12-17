# wikiscrap.py

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

# html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
# soup1 = BeautifulSoup(html, 'html.parser')

# for link in soup1.findAll('a'):
# 	if 'href' in link.attrs:
# 		print(link.attrs['href'])

# for link in soup1.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
# 	if 'href' in link.attrs:
# 		print(link.attrs['href'])

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
	html = urlopen('http://en.wikipedia.org'+articleUrl)
	soup1 = BeautifulSoup(html, 'html.parser')	
	return soup1.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')	
# print(links)
# print(len(links))

# newArticle = links[1].attrs['href']
# print(newArticle)

while len(links) > 0:
	newArticle = links[random.randint(0, len(links)-1)].attrs['href']
	print(newArticle)
	links = getLinks(newArticle)

# links = getLinks(newArticle)
# print(len(links))
# newArticle = links[1].attrs['href']
# print(newArticle)