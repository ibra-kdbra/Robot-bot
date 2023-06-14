#!/usr/bin/env python
import pywikibot
import argparse

############################
# handle command line args #
############################

parser = argparse.ArgumentParser(
	description='Go through random pages, until you find one with missing templates on the discussion page. Then add the missing templates.')
parser.add_argument('--limit', type=int, nargs='?', default=1,
					help='the number of pages you want to appy this script to')

args = parser.parse_args()

############################

counter = 0
limit = args.limit
site = pywikibot.Site("af")
blad = None

while counter < limit:
	print('counter:' + str(counter))
	print('limit:' + str(limit))

	found = False
	while not found:
		# get random page
		for page in site.randompages(1, 0, False, False):
			blad = page

		# toggle talk
		if not blad.isTalkPage():
			blad = blad.toggleTalkPage()

		# check if exists
		bladlen = len(blad.text)
		if bladlen > 0:
			print(blad.title() + " has a non-empty talk page. Size = " + str(bladlen))
			found = True
		else:
			print(blad.title() + " is an empty talk page.")

	# end of whilenot found loop

	Kop = '{{Kop van besprekingsbladsy}}'
	Bladtrekke = '{{Bladtrekke}}'
	containsKop = False
	containsBladtrekke = False
	skip = False
	savemsg = ''

	if Kop in blad.text:
		containsKop = True
	if Bladtrekke in blad.text:
		containsBladtrekke = True
	if containsKop and containsBladtrekke:
		print('already has Kop and Bladtrekke')
		skip = True
	elif containsKop and not containsBladtrekke:
		blad.text = blad.text.replace(Kop, (Kop + '\n' + Bladtrekke + '\n'))
		savemsg = 'Bladtrekke'
	elif not containsKop and containsBladtrekke:
		blad.text = Kop + '\n' + blad.text
		savemsg = 'Kop'
	elif not containsKop and not containsBladtrekke:
		blad.text = Kop + '\n' + Bladtrekke + '\n' + blad.text
		savemsg = 'Bladtrekke en Kop'

	print(savemsg)

	if not skip:
		counter += 1
		try:
			blad.save(savemsg)  # Saves the page
		except pywikibot.EditConflict:
			pywikibot.output('Edit conflict! skip!')
		except pywikibot.ServerError:
			if count <= config.max_retries:
				pywikibot.output('Server Error! Wait..')
				time.sleep(config.retry_wait)
			else:
				raise pywikibot.ServerError('Server Error! Maximum retries exceeded')
		except pywikibot.SpamfilterError as e:
			pywikibot.output('Cannot change {} because of blacklist entry {}'.format(page.title(), e.url))
		except pywikibot.LockedPage:
			pywikibot.output('Skipping {} (locked page)'.format(page.title()))
		except pywikibot.PageNotSaved as error:
			pywikibot.output('Error putting page: {}'.format(error.args))

# end of while counter < limit

print('Klaar.')
