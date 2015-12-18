# revisionpagecrawling.py

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org'+articleUrl)
    soup1 = BeautifulSoup(html,'html.parser')
    returnvalue = soup1.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    # print(returnvalue)
    return returnvalue

def getHistoryIPs(pageUrl):
    # Format of revision history pages is:
    # https://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history

    pageUrl = pageUrl.replace('/wiki/', '')
    print(':::::::')
    print('pageUrl: ' + pageUrl)

    historyUrl = 'http://en.wikipedia.org/w/index.php?title='+pageUrl+'&action=history'

    print('history url is: ' + historyUrl)
    html = urlopen(historyUrl)
    soup1 = BeautifulSoup(html, 'html.parser')

    # finds only the links with class "mw-anonuserlink" which has IP addresses
    # instead of usernames
    ipAddresses = soup1.findAll('a', {'class':'mw-anonuserlink'})
    addressList = set()

    for ipAddress in ipAddresses:
        print('ipAddress.get_text: ' + ipAddress.get_text())
        addressList.add(ipAddress.get_text())
    return addressList

links = getLinks('/wiki/Python_(programming_language)')

while(len(links) > 0):
    for link in links:
        print('----------------')
        historyIPs = getHistoryIPs(link.attrs['href'])

        for historyIP in historyIPs:
            print(historyIP)

    newLink = links[random.randint(0, len(links)-1)].attrs['href']
    links = getLinks(newLink)

