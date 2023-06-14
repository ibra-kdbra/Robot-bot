#!/usr/bin/env python
import pywikibot
import requests
import datetime
from requests.exceptions import ConnectionError

save_changes = True
####################
# Wisselkoers data #
####################

try:
    url_usd_zar = 'https://free.currencyconverterapi.com/api/v6/convert?q=USD_ZAR&compact=y'
    url_eur_zar = 'https://free.currencyconverterapi.com/api/v6/convert?q=EUR_ZAR&compact=y'
    url_gbp_zar = 'https://free.currencyconverterapi.com/api/v6/convert?q=GBP_ZAR&compact=y'

    response = requests.get(url_usd_zar)
    usd_zar = response.json()['USD_ZAR']['val']
    usd_zar = round(usd_zar,2)
    usd_zar = str(usd_zar)
    #print(usd_zar)

    response = requests.get(url_eur_zar)
    eur_zar = response.json()['EUR_ZAR']['val']
    eur_zar = round(eur_zar,2)
    eur_zar = str(eur_zar)
    #print(eur_zar)

    response = requests.get(url_gbp_zar)
    gbp_zar = response.json()['GBP_ZAR']['val']
    gbp_zar = round(gbp_zar,2)
    gbp_zar = str(gbp_zar)
    #print(gbp_zar)

    date = datetime.date.today().strftime('%d/%m/%Y')
    #print(date)


    wisselkoers_lyn = '* Wisselkoers (' + date + '): 1 [[Amerikaanse dollar|VS$]] = ' + usd_zar + ' ZAR, 1 [[Euro]] = ' + eur_zar + ' ZAR, 1 [[pond sterling]] = ' + gbp_zar + ' ZAR. <ref name="wisselkoers">https://free.currencyconverterapi.com</ref>'

    #print(wisselkoers_lyn)

except ConnectionError as e:
    print(e)
    print('Conneciton error. Probably hit max retry limit. Try again later.\n')
    print('changes not saved')
    quit()

####################

####################
# Pywikibot        #
####################

site = pywikibot.Site('af','wikipedia')
page = pywikibot.Page(site,'Suid-Afrikaanse rand')
text = page.text

for line in text.splitlines():
    if '* Wisselkoers' in line:
        print('Changing :\n' + line + '\n to\n' + wisselkoers_lyn)
        page.text = text.replace(line,wisselkoers_lyn)

if save_changes:
    page.save('Wisselkoers')
    print('Saved changes')
else:
    print('Not saving changes')
