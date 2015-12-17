# paringJSON.py

# Chapter 4 page 63

import json
from urllib.request import urlopen

def getCountry(ipAddress):

	# print('http://freegeoip.net/json/'+ipAddress)
	response = urlopen('http://freegeoip.net/json/'+ipAddress).read().decode('utf-8')
	print(response)	

	responseJSON = json.loads(response)
	print(responseJSON)

	return responseJSON.get('region_name')
	

		

	

print(getCountry('50.78.253.58'))
