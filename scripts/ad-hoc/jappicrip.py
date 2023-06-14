#!/usr/bin/env python

from bs4 import BeautifulSoup
from io import StringIO
import requests
import pywikibot

###
# Functions
###
def stripParen(token, rd):
	cleanline = ''
	head, sep, tail = rd.partition(token + ':')
	cleanline = sep + tail
	head, sep, tail = cleanline.partition('\n') # get only selected line
	cleanline = head
	if '(' in cleanline:
		head, sep, tail = cleanline.partition('(') # if there is no bracket it returns the rest of the thing
		cleanline = head + '\n'
	else:
		cleanline += '\n'

	s = StringIO(rd)
	for line in s:
		if token in line:
			rd = rd.replace(line, cleanline)
	s.close()

	return rd
##############################################################################

#loop over page range
for i in range(112, 114):
	pagenum = i
	print('doing page ' + str(i))
	meer_inligting = ''
	inligting = '== Inligting Oor Roete =='
	route_data = ''

#get en page
	site = pywikibot.Site('en', 'wikipedia')
	page = pywikibot.Page(site, 'Japan_National_Route_' + str(pagenum))

#get route data
	page.text = page.text.replace('== Route Data ==', inligting) # just in case
	page.text = page.text.replace('==Route data==', inligting) # just in case
	page.text = page.text.replace('==Route Data==', inligting) # just in case
	page.text = page.text.replace('==route Data==', inligting) # just in case
	page.text = page.text.replace('== Route data ==', inligting) # just in case
	page.text = page.text.replace('== route data ==', inligting) # just in case
	page.text = page.text.replace('== route Data ==', inligting) # just in case

	head, sep, tail = page.text.partition(inligting)
	route_data = sep + tail

	head, sep, tail = route_data.partition('\n\n==')
	route_data = head

#translate route data
	route_data = route_data.replace('Length', 'Lengte')
	route_data = route_data.replace('{{Convert|', '{{Omreken|')
	route_data = route_data.replace('mi|1|abbr=on}}', '0}}')

	route_data = route_data.replace('*Origin', '*Oorsprong')
	route_data = stripParen('*Oorsprong',route_data)

	route_data = route_data.replace('*Terminus', '*Eindpunt')
	route_data = stripParen('*Eindpunt',route_data)

	route_data = route_data.replace('Major Cities', 'Hoof stede op die roete')
	route_data = route_data.replace('Major cities', 'Hoof stede op die roete')


# get images
	url = 'https://commons.wikimedia.org/wiki/Category:Route_' + str(pagenum) + '_(Japan)'
	r = requests.get(url)
	html = r.content

	page = BeautifulSoup(html, 'lxml')
	imgs = page.find_all("a", class_='image')

	img_gallery = '== Beelde ==\n<gallery>\n'

	for img in imgs:
		#print(img)
		beeld = img.get('href')
		img_gallery += beeld.replace('/wiki/File','Lêer')
		img_gallery += '|\n'

	img_gallery += '</gallery>\n\n'

	meer_inligting += route_data + '\n\n' + img_gallery

#print(meer_inligting)

#get af page
	site = pywikibot.Site('af', 'wikipedia')
	page = pywikibot.Page(site, 'Japan_Nasionale_Roete_' + str(pagenum))

# replace == verwysings == with meer_inligting + == verwysings ==
	page.text = page.text.replace('== Verwysings ==', meer_inligting + '== Verwysings ==')
	#print(page.text)
#write af page
	page.save('Meer inligting')

# end of for loop
print('done')

