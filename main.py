#Copyright (c) 2022, Efe Akaröz
#All rights reserved.


import requests
from bs4 import BeautifulSoup
import random
from cryptography.fernet import Fernet

while True:
	randomWiki = requests.get("https://en.wikipedia.org/wiki/Special:Random")
	soup = BeautifulSoup(randomWiki.content,features="lxml")
	text = soup.findAll("html")[0].get_text()
	text.replace("\n","")
	words = text.split(" ")
	for w in words:
		googleSearch = requests.get("https://google.com/search?q="+w.replace(".",""))
		googleSoup = BeautifulSoup(googleSearch.content,"html.parser")
		titles = googleSoup.find_all("h3")
		for t in titles:
			try:
				if t.parent.get('href') != None:
					open("results.txt","a").write(f"{t.get_text()}?==+!{t.parent.get('href').replace('/url?q=','')}\n")
				else:
					pass

			except Exception as e:
				print(e)





