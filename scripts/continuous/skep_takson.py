#!/usr/bin/env python
import pywikibot


def get_wikidata_item(page_title):
	item_number = 'Q0000'
	return item_number


# This example gets all the Wikidata-data from the Item connected with the English Wikipedia page for Douglas Adams:
# site = pywikibot.Site("en", "wikipedia")
# page = pywikibot.Page(site, "Douglas Adams")
# item = pywikibot.ItemPage.fromPage(page)
#
# check these wikis in order : ceb, vi, af, en
# if none log that no wikidata item can be found
#
# if found return item_number

# create new function for setting siteLink (once you have the item_number)


print("Begin")

site = pywikibot.Site("af", "wikipedia")

page_list = [
	"Lithops aucampiae",
	"Lithops bella",
	"Lithops burchellii"]

for page in page_list:
	page = pywikibot.Page(site, page)
	page_title = page.title()

	if page.exists():
		print('\n' + page_title + ' bestaan reeds. Slaan oor na die volgende bladsy.\n')
		continue

	parent_taxon = ''
	parent_taxon_type = ''
	taxon_type = 'species'
	descriptor = 'vetplant'

	page.text = ''

	if taxon_type == 'species':
		page.text += '{{Spesieboks\n'
	else:
		page.text += '{{Outomatiese taksoboks\n'

	page.text += '| name = <!-- Afrikaanse naam -->\n'
	page.text += '| status = \n'
	page.text += '| status_system = iucn3.1\n'
	page.text += '| status_ref = \n'
	page.text += '| image = \n'
	page.text += '| taxon = ' + page_title + '\n'
	page.text += '| authority = \n'
	page.text += '}}'
	page.text += "'''''" + page_title + "''''' is 'n [[" + descriptor + "]] wat deel is van die " + parent_taxon + " [[" + parent_taxon_type + "]].\n"

	page.text += '<!--\n'
	page.text += '== Verspreiding ==\n'
	page.text += '== Beskrywing ==\n'
	page.text += '== Bronne ==\n'
	page.text += '== Verwysings ==\n'
	page.text += '-->\n'

	page.text += '{{Saadjie}}\n{{Taksonbalk}}\n'

	page.text += '[[Kategorie:' + parent_taxon + ']]'

	print(page.text)
# page.save('Nuwe bladsy geskep - ' + page, minor=False)

# TODO : check if wikidata item exists
# TODO : link to wikidata item : https://www.wikidata.org/wiki/Wikidata:Pywikibot_-_Python_3_Tutorial/Setting_sitelinks

# TODO : source : create stub article from title / create info from wikidata / webscrape iucn page and generate content
