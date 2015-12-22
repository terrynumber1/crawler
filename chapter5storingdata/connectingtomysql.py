# page 84
# code on page 84 needed to be tweak
# do not include unix_socket= on line 13 of this file

from urllib.request import urlopen
from bs4 import BeautifulSoup

import re
import datetime
import random
import pymysql

conn = pymysql.connect(host='localhost', user='user1', passwd='password1', db='scraping', charset='utf8')

cur = conn.cursor()
cur.execute("USE scraping")

random.seed(datetime.datetime.now())

def store(title, content):
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\", \"%s\")", (title, content))
    cur.connection.commit()

def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org'+articleUrl)
    soup1 = BeautifulSoup(html, 'html.parser')
    # title = soup1.find('h1').find('span').get_text()
    title = soup1.find('h1').get_text()
    content = soup1.find('div', {'id':'mw-content-text'}).find('p').get_text()

    print('title: ' + title)
    print('content: ' + content)

    print('Storing data into db:scraping')
    store(title, content)

    return soup1.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$') )


# print(getLinks('/wiki/Kevin_Bacon'))
# links = getLinks('/wiki/Kevin_Bacon')
try:
    # while len(links) > 0:
        # newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        # print(newArticle)

        # links = getLinks(newArticle)        
finally:
    cur.close()
    conn.close()
