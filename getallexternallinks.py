# getallexternallinks.py

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

# Collects a LIST of all external URLs found on the site
allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
	html = urlopen(siteUrl)
	soup1 = BeautifulSoup(html, 'html.parser')

	inter