#!/usr/local/bin/python

from bs4 import BeautifulSoup
import requests
#import dataset
import time
import psycopg2
import psycopg2.extras

print "thanks for using, this may take a second depending on your Internet connection"

#connect to db using psycopg2
dbConnection = psycopg2.connect(user = 'YOURUSER', password = 'YOURPASS', dbname = 'YOURDB', host = 'YOURHOST', port = PORT) #for postgres

#db = dataset.connect('sqlite:////Users/Rob/Documents/code/capstone/v2/site2/cap2.db') #for sqlite

print "got db"

cursor = dbConnection.cursor(cursor_factory=psycopg2.extras.DictCursor)


one = "http://www.cuindependent.com"
two = "http://www.dailycamera.com"
three = "http://www.denverpost.com"

def textDB(text1, link1, name1, url1):
	text=text1
	print text
	slug = text
	for ch in [':',',',';','!','.','$','@','%','&','?','<','>','+','=','-','(',')',"'",]:
		if ch in slug:
			slug=slug.replace(ch, '').encode('ascii', errors='ignore')
	slug=slug.replace(" ", "-").replace("'", "")
	text=text.replace("'", "")
	#print slug
	link = link1
	#print link
	name = name1
	#print name
	url = url1
	#print url

	#for sqlite
	#table=db['headTable']
	#data = dict(head=text,slug=slug,link=link,name=name,site=url,published="1",day=time.strftime("%m/%d/%Y"),)
	#print data
	#table.insert(data)
	#print "success!"

	#for postgres
	insStr = "insert into headTable (head, link, name, slug, site, day, published) values ("
	insStr += "'" + text + "', "
	insStr += "'" + link + "', "
	insStr += "'" + name + "', "
	insStr += "'" + slug + "-" + time.strftime("%m-%d-%Y") + "', "
	insStr += "'" + url + "', "
	insStr += "'" + time.strftime("%m/%d/%Y") + "', "
	insStr += "'True'"
	insStr += ");"
	insStr = str(insStr)
	print "insStr = " + insStr
	cursor.execute(insStr)
	dbConnection.commit()
	print "success!"

def urls(url):
	get = requests.get(url)
	content = get.content
	soup = BeautifulSoup(content)
	if url == one:
		#modify this to scrape your first site
		div=soup.find("div", "post_header")
		text=div.find('a').text
		link=div.find('a').get('href')
		textDB(text, link, "CU Independent", url)
	elif url == two:
		#modify this to scrape your second site
		div=soup.find('a', 'listingItemTitle')
		text=div.text
		link=div.get('href')
		textDB(text, link, "Boulder Daily Camera", url)
	elif url == three:
		#modify this to scrape your third site
		div=soup.find('a', 'listingItemTitle')
		text=div.text
		link=div.get('href')
		textDB(text, link, "The Denver Post", url)
	else:
		print "no data"

urls(one)
urls(two)
urls(three)