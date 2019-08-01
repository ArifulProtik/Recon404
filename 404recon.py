#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import os,time
from bs4 import BeautifulSoup
href = []
unique = []
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'

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
			if len(l.get("href").strip()) > 1 and l.get("href")[0] != '#' and 'javascript:' not in l.get("href").strip() and 'mailto:' not in l.get("href").strip() and 'tel:' not in l.get("href").strip():
				if 'http' in l.get("href").strip() or 'https' in l.get("href").strip():
					href.append(l.get("href").strip())
					
def uniquelink(href):
	for x in href:
		if x not in unique:
			unique.append(x)

def Check404():
	print("Total "+ str(len(unique)) + " link Found")
	for line in unique:
		try:
			f = requests.get(line,headers=headers)
		except requests.exceptions.SSLError:
			continue
		else:
			if f.status_code == 200:
				print(bcolors.OKGREEN + "[ "+ str(f.status_code)+ " ]"+line)
			else:
				print(bcolors.WARNING + "[ "+ str(f.status_code)+ " ]" + line)
				
				

def banner():
    if (os.name in ('ce', 'nt', 'dos')):
        os.system('cls')
    elif ('posix' in os.name):
        os.system('clear')
    print(bcolors.HEADER+"Started Recon404 \n \n")			
def mainf():
	banner()
	linkExtractor()
	uniquelink(href)
	Check404() 
mainf()
