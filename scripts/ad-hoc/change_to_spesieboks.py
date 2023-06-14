#!/usr/bin/env python
import pywikibot


def is_bad_line(current_line):
    bad_strs = ['regnum =', 'unranked_divisio =', 'unranked_classis =', 'unranked_ordo =', 'divisio =', 'classis =',
                'ordo =', 'familia =', 'phylum =', 'image_width =',
                'subfamilia =', 'tribus =', 'subtribus =', 'genus =', 'species =',
                'species_authority =']

    has_bad_str = False

    for bstr in bad_strs:
        if bstr in current_line:
            has_bad_str = True
            break

    return has_bad_str


##########################################

site = pywikibot.Site("af", "wikipedia")

page_list = ["Erica adaequata", "Erica adnata","Erica adunca"]

change_text0 = '{{Taksoboks'
change_text0b = '{{Taxobox'

change_text1 = 'binomial = '
change_text2 = 'binomial_authority ='

change_text3 = '|name ='
change_text4 = '|image ='
change_text5 = '|image_caption ='
change_text6 = '|status ='
change_text7 = '|status_system ='

for page in page_list:
    page = pywikibot.Page(site, page)
    page_title = page.title()
    text = page.text

    if not page.exists():
        print('Bladsy :' + page_title + ' bestaan nie.')
    else:
        # loop over every line in page text
        for line in text.splitlines():

            if change_text0 in line:
                text = text.replace(change_text0, '{{Spesieboks')

            if change_text0b in line:
                text = text.replace(change_text0b, '{{Spesieboks')

            # remove unnecessary lines
            if is_bad_line(line):
                text = text.replace(line, '')  # blank line

            # heck, that was a struggle
            if change_text1 in line:
                clean_line = line.replace("'", "")
                text = text.replace(line, clean_line)
                text = text.replace(clean_line, clean_line.replace(change_text1, 'taxon = '))

            # optimise this crap below
            if change_text2 in line:
                text = text.replace(change_text2, 'authority =')

            if change_text3 in line:
                text = text.replace(change_text3, '| name =')

            if change_text4 in line:
                text = text.replace(change_text4, '| image =')

            if change_text5 in line:
                text = text.replace(change_text5, '| image_caption =')

            if change_text6 in line:
                text = text.replace(change_text6, '| status =')

            if change_text7 in line:
                text = text.replace(change_text7, '| status_system =')

        # remove blank lines
        while '\n\n|' in text:
            text = text.replace('\n\n|', '\n|')

        page.text = text  # indent?

        page.save('Verander na Spesieboks', minor=False)
