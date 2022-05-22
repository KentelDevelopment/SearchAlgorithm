#Copyright (c) 2022, Efe Akaröz
#All rights reserved.


import requests
from bs4 import BeautifulSoup
import random
import os
from cryptography.fernet import Fernet

os.system("clear")

fileSearch = open("results.txt","r").read()

oldValue = len(fileSearch.split("\n"))



while True:

	randomWiki = requests.get("https://en.wikipedia.org/wiki/Special:Random")
	soup = BeautifulSoup(randomWiki.content,features="lxml")
	text = soup.findAll("html")[0].get_text()
	text.replace("\n","")
	words = text.split(" ")
	for w in words:
		os.system("clear")
		fileSearch2 = open("results.txt","r").read()

		newValue = len(fileSearch2.split("\n"))
		print("===================Kentel======================")
		print("Old count(before run):{}".format(oldValue))
		print("Total Data Count(now):{}".format(newValue))
		print("New Data(while running this session):{}".format(newValue-oldValue))
		print("===============================================")
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





