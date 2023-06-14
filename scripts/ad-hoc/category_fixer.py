#!/usr/bin/env python
import pywikibot

site = pywikibot.Site("af", "wikipedia")

bad_cat = '[[Kategorie:Rekenaar]]'
good_cat = '[[Kategorie:Rekenaars]]'

page_list = [
    "Commodore 64",
    "Commodore PET",
    "CUDA",
    "Databasis",
    "DDR SDRAM",
    "Diensgeoriënteerde argitektuur",
    "Dinamiese ewetoeganklike geheue",
    "Document Object Model",
    "Dvorak-sleutelbord",
    "Eksagreep",
    "ENIAC",
    "Epson HX-20",
    "Ewetoeganklike geheue",
    "FpGUI",
    "Free Pascal",
    "Gedraaide draadpaar",
    "Gigagreep",
    "GNU Algemene Publieke Lisensie",
    "GNU-lisensie vir vrye dokumentasie",
    "GNU/Linux",
    "Greep",
    "IBAN",
    "ICDL",
    "Intel",
    "Intel 8259",
    "Jugene",
    "Kabelmodem",
    "Kilogreep",
    "Kliënt (rekenaar)",
    "Kliënt-bediener argitektuur",
    "Klokversnelling",
    "Kodek",
    "Kombinasielogika",
    "Konstruktiewe ruimtemeetkunde",
    "Kontrolesom",
    "Laserdrukker",
    "Macintosh",
    "Megagreep",
    "Melissa rekenaarwurm",
    "Mikroverwerker",
    "Miljoen instruksies per sekonde",
    "Modem",
    "Muis (rekenaar)",
    "Multifunksiedrukker",
    "Onderbrekingsversoek",
    "Oopbroninhoud",
    "Oracle Corporation",
    "Osborne 1",
    "Osborne-effek",
    "OSI-model",
    "Palmrekenaar",
    "Parallelle poort",
    "Pariteitsbis",
    "Pentium 4",
    "Persoonlike rekenaar",
    "Petagreep",
    "POV-Ray",
    "Protokol (rekenaars)",
    "QWERTY-sleutelbord",
    "RAID",
    "Rekenaar",
    "Rekenaarbediener",
    "Rekenaarbus",
    "Rekenaardrukker",
    "Rekenaargesteunde ontwerp",
    "Rekenaarhardeware",
    "Rekenaarpoort",
    "Rekenaarprogram",
    "Rekenaarsekuriteit",
    "Rekenaarterminaal",
    "Rekenaarvirus",
    "Portaal:Rekenaarwetenskap",
    "Rekeningkundige pakket",
    "Remote Installation Services",
    "Sagteware",
    "Sekwensiële logika",
    "Sentrale verwerkingseenheid",
    "Serie-poort",
    "Sharp PC-1211",
    "Sharp PC-1500",
    "Skakel",
    "Skandeerder",
    "Slapskyf",
    "Sleutelbord",
    "Sony PsP",
    "Speltoetser",
    "Tabletrekenaar",
    "Teragreep",
    "Toevoer/afvoer",
    "TrackIR",
    "Trojaanse perd (rekenaars)",
    "Virtuele masjien",
    "Wi-Fi Protected Access",
    "Woordlengte",
    "Wys en klik"]

for page in page_list:
    page = pywikibot.Page(site, page)
    page_title = page.title()
    text = page.text

    if not page.exists():
        print('Bladsy :' + page_title + ' bestaan nie.')
        continue
    else:
        # loop over every line in page text
        for line in text.splitlines():
            # print(line)
            if bad_cat in line:
                text = text.replace(bad_cat, good_cat)

            page.text = text

        page.save(bad_cat + ' -> ' + good_cat, minor=True)
