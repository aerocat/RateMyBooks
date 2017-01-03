# Written by aerocat on Sept. 20, 2016

import urllib
import os
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup as Soup


books = []
# ask user for filename that stores the list (.txt)
filename = raw_input("Enter filename of the list of books: ")
with open(filename,'r') as myfile:
	for line in myfile.readlines():
		if line[:7] != 'http://' and line[:4] != 'www.':
			books.append(line)

## for testing, print the list of books
# for book in books:
#	print book
# print "Found {} books".format(len(books))

APIkey = '' # INSERT A VALID API KEY HERE; obtain from: https://www.goodreads.com/api
URL = 'https://www.goodreads.com/search.xml?key=' + APIkey

d = {}
counter = 0
nbooks = len(books)

for book in books:
# 	add .read() if you want the response to be a string instead of an object
	response = urllib.urlopen(URL+'&q=%s'%urllib.quote(book)).read()
	time.sleep(1) #API limitation (only 1 request per second)

#	print "Your book in the list was: " + book
#	print "Here's what I found: "
	soup = Soup(response, "lxml")
	for work in soup.findAll('work')[:1]:     #for the purpose of this, only first match is chosen
		avg = work.find('average_rating').text
		author = work.find('name').text
		year = work.find('original_publication_year').text
		title = work.find('title').text
		entry = title + ", " + author + ' ('+ year +')'
		d[entry] = avg
	## 	for testing purposes only
#		for k, v in d.items():
#			print k, v
	counter += 1
	print "{} books processed out of {}. (1 book/sec)".format(counter, nbooks)

with open('output.txt', 'w') as f:
	for w in sorted(d, key=d.get, reverse=True):
 # 		print w, d[w]
 		final = d[w] + '\t' + w + '\n'
 		f.write(final)

with open('output.txt', 'r') as f:
	print "Here is the resulting ranking based on your book list!\n"
	print f.read()
