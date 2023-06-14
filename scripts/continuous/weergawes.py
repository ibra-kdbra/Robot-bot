#!/usr/bin/env python

from packaging import version
from bs4 import BeautifulSoup
from io import StringIO
import requests
import pywikibot
import datetime

# if version.parse(v1) > version.parse(ffStableVersion)

ffStableVersion = '0'
ffStableReleaseDate = ''

ffBetaVersion = '0'
ffBetaReleaseDate = ''

# Firefox stable
def getFFStableInfo():
	global ffStableVersion
	global ffStableReleaseDate
	url = 'https://www.mozilla.org/en-US/firefox/notes/'
	r = requests.get(url, verify=True)
	html = r.content

	page = BeautifulSoup(html, 'lxml')
	rdiv = page.find('div', {'class':'version'})
	children = rdiv.findChildren()
	for child in children:
		if child.name == 'h2':
			ffStableVersion = child.text
		elif child.name == 'p':
			ffStableReleaseDate = datetime.datetime.strptime(child.text, '%B %d, %Y').strftime('%Y|%m|%d')

# end of getFFStableVersion

# Firefox beta
def getFFBetaInfo():
	global ffBetaVersion
	global ffBetaReleaseDate

	url = 'https://www.mozilla.org/en-US/firefox/61.0beta/releasenotes/'
	r = requests.get(url, verify=True)
	html = r.content

	page = BeautifulSoup(html, 'lxml')
	rdiv = page.find('div', {'class':'version'})
	children = rdiv.findChildren()
	for child in children:
		if child.name == 'h2':
			ffBetaVersion = child.text
		elif child.name == 'p':
			ffBetaReleaseDate = datetime.datetime.strptime(child.text, '%B %d, %Y').strftime('%Y|%m|%d')
#end of ff beta

# Firefox wiki
# get wiki page (Mozilla Firefox)

#get 4 lines:
#| laaste weergawe              = 60.0.01<ref name="firefox-release-notes"/>
#| laaste vrystellingsdatum     = {{Begin datum en ouderdom|2018|05|16|df=yes}}
#| laaste betaweergawe          = 61.0beta<ref name="firefox-beta-release-notes"/>
#| laaste betavrystellingsdatum = {{Begin datum en ouderdom|2018|05|09|df=yes}}

#compare versions and dates

#if different, then update
getFFStableInfo()
print('lastest ff version is: ' + ffStableVersion)
print('lastest ff release date is: ' + ffStableReleaseDate)
getFFBetaInfo()
print('lastest ff-beta version is: ' + ffBetaVersion)
print('lastest ff-beta release date is: ' + ffBetaReleaseDate)
