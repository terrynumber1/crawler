from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

htmlpage1 = urlopen('http://www.pythonscraping.com')
soup1 = BeautifulSoup(htmlpage1, 'html.parser')

imageLocation1 = soup1.find('a', {'id':'logo'}).find('img')['src']
# imageLocation2 = soup1.find('a', {'id':'logo'}).find('img').attrs['src']
# print(imageLocation1)

urlretrieve(imageLocation1, 'jim.jpg')
