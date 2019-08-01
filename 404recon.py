#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
href = []
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def linkExtractor():
	link = input("Enter Link:")
	try:
		r = requests.get("http://"+link,headers=headers)
		r.raise_for_status()
	except requests.exceptions.HTTPError:
		print('Error Http')
		pass
	except requests.exceptions.ConnectionError:
		print('Check Your Connection, Or Site Not Responding')
		pass
	else:
		html = r.text
		soup = BeautifulSoup(html,'html.parser')
		for l in soup.find_all('a'):
			href.append(l.get('href'))

def Check404():
	print("Total "+ str(len(href)) + " link Found")
	for line in href:
		try:
			f = requests.get(line,headers=headers)
		except requests.URLRequired:
			continue
		except requests.exceptions.MissingSchema:
			continue
		except requests.exceptions.InvalidSchema:
			continue
		except requests.exceptions.SSLError:
			continue
		else:
			print("[ "+str(f.status_code)+" ]  " + line)
			
def mainf():
	linkExtractor()
	Check404() 
mainf()
