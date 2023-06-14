#!/usr/bin/env python
import pywikibot

site = pywikibot.Site("af", "wikipedia")

bladsy_lys = [
    "Appelkoos (kleur)",
    "Aspersie (kleur)",
    "Aspersiegrys",
    "Asuur (kleur)",
    "Avokado (kleur)",
    "Babablou",
    "Baksteen (kleur)",
    "Beige",
    "Beskuit (kleur)",
    "Bewer (kleur)",
    "Bister",
    "Bittersoet (kleur)",
    "Blou",
    "Blougroen",
    "Blougrys",
    "Boergondies (kleur)",
    "Bole (kleur)",
    "Bondi-blou",
    "Bordeaux (kleur)",
    "Bottelgroen",
    "Brons (kleur)",
    "Bruin",
    "Cambridge-blou",
    "Celeste (kleur)",
    "Chartreuse-geel",
    "Chartreuse-groen",
    "Denim (kleur)",
    "Dennegroen",
    "Dodgers-blou",
    "Donkerblou",
    "Donkergroen",
    "Donkeroranje",
    "Donker mosgroen",
    "Donkerrooi",
    "Donkersjokolade (kleur)",
    "Eierdopwit",
    "Elektriese blou",
    "Framboos (kleur)",
    "Fuchsia (Crayolakleur)",
    "Geel",
    "Geelbruin",
    "Geelgroen",
    "Gommagutta",
    "Goud (kleur)",
    "Goudbruin",
    "Grasgroen",
    "Groen",
    "Grys",
    "Grysgroen",
    "Harlekyngroen",
    "Heldergroen",
    "Helderrooi",
    "Hemelblou",
    "Indiese geel",
    "Indië-groen",
    "Indigo",
    "Internasionale oranje",
    "Islamitiese groen",
    "Jagtersgroen",
    "Kadetblou",
    "Kadetgrys",
    "Kadmiumgeel",
    "Kadmiumgroen",
    "Kadmiumoranje",
    "Kadmiumrooi",
    "Kakie",
    "Kardinaalrooi",
    "Karibiese groen",
    "Karmosyn",
    "Karmyn",
    "Kersierooi",
    "Klawergroen",
    "Kobalt (kleur)",
    "Komboegroen",
    "Koningsblou",
    "Koring (kleur)",
    "Koringblomblou",
    "Laventel (kleur)",
    "Lawa (kleur)",
    "Leeu (kleur)",
    "Lemmetjie (kleur)",
    "Lemmetjie (kleur)",
    "Lemoenskil (kleur)",
    "Lentegroen",
    "Lewer (kleur)",
    "Ligblou ",
    "Ligbruin ",
    "Liggeel ",
    "Liggroen ",
    "Liggrys",
    "Ligpers",
    "Ligrooigrys",
    "Ligte denim (kleur)",
    "Linne (kleur)",
    "Lugmagblou",
    "Magenta (kleur)",
    "Mahonie (kleur)",
    "Mandaryn (kleur)",
    "Mantisgroen",
    "Maroen ",
    "Middernagblou ",
    "Mielie (kleur)",
    "Mintgroen ",
    "Mirre (kleur)",
    "Moerasgroen",
    "Mosgroen",
    "Mosterd (kleur)",
    "Napelsgeel",
    "Navajowit",
    "Neongroen",
    "Oerwoudgroen",
    "Oker",
    "Olyf (kleur)",
    "Ongebleik (kleur)",
    "Oranje (kleur)",
    "Oranjebruin",
    "Ougoud",
    "Pakistangroen",
    "Pampoen (kleur)",
    "Papajaklits (kleur)",
    "Parysgroen",
    "Pastelbruin",
    "Pastelgeel",
    "Peer (kleur)",
    "Pers",
    "Persiese blou",
    "Persiese rooi",
    "Persiese groen",
    "Perske (kleur)",
    "Peru (kleur)",
    "Pienk",
    "Pistagiogroen",
    "Poeierblou",
    "Pomegranaat (kleur)",
    "Poublou",
    "Pruim (kleur)",
    "Pruisiese blou",
    "Purper",
    "Resiesrooi",
    "Roes (kleur)",
    "Rooi",
    "Rooibruin",
    "Room (kleur)",
    "Roos (kleur)",
    "Roosoranje",
    "Russiese groen",
    "Saalbruin",
    "Saffier (kleur)",
    "Saffloer",
    "Saffraan (kleur)",
    "Salm (kleur)",
    "Savoiblou",
    "Seegroen",
    "Seeskilpadgroen",
    "Selektiewe geel",
    "Sepia (kleur)",
    "Seruleumblou",
    "Siaan",
    "Sienna",
    "Silwer (kleur)",
    "Sinabargroen",
    "Sjampanje (kleur)",
    "Sjokolade (kleur)",
    "Skarlaken",
    "Skokpienk",
    "Skoolbusgeel",
    "Skuttersgroen",
    "Skreegroen",
    "Smarag (kleur)",
    "Sneeu (kleur)",
    "Spanspek (kleur)",
    "Spookwit",
    "Staalblou",
    "Staalpienk",
    "Suurlemoen (kleur)",
    "Suurlemoen-lemmetjie (kleur)",
    "Suurlemoenroom (kleur)",
    "Swart",
    "Taankleurig",
    "Tamatie (kleur)",
    "Taupe (kleur)",
    "Teel (kleur)",
    "Terracotta",
    "Tropiese groen",
    "Tropiese reënwoud (kleur)",
    "Turkoois (kleur)",
    "Ultramarien",
    "Vaalbruin",
    "Vaalgroen ",
    "Vanielje (kleur)",
    "Varinggroen",
    "Venesiese rooi",
    "Verbrande oranje",
    "Vermiljoen",
    "Veroneesgroen",
    "Violet",
    "Vlamoranje",
    "Vlas (kleur)",
    "Vlootblou",
    "Wilgergroen",
    "Wit",
    "Woestynsand (kleur)",
    "Worteloranje",
    "Woudgroen",
    "Wynrooi",
    "Zydeco (kleur)"
]

oldcss1 = '{| border="1" cellpadding="2" cellspacing="0" style="margin: 1em 1em 1em 0; background: #f9f9f9; border: 1px #aaa solid; border-collapse: collapse; font-size: 95%; text-align: right"'
oldcss2 = 'style="background-color:#E9E9E9" align=left|'
oldcss3 = 'style="background-color:#E9E9E9" align=right|'
oldcss4 = 'style="background-color:#E9E9E9" '
oldcss5 = 'align=left|'
oldcss6 = 'align=right|'
oldcss7 = '{| border="1"'

for bladsy in bladsy_lys:
    blad = pywikibot.Page(site, bladsy)
    text = blad.text

    for lyn in text.splitlines():
        if oldcss1 in lyn:
            text = text.replace(oldcss1, '{| class="wikitable"')

        if oldcss2 in lyn:
            text = text.replace(oldcss2, '')

        if oldcss3 in lyn:
            text = text.replace(oldcss3, '')

        if oldcss4 in lyn:
            text = text.replace(oldcss4, '')

        if oldcss5 in lyn:
            text = text.replace(oldcss5, '')

        if oldcss6 in lyn:
            text = text.replace(oldcss6, '')

        if oldcss7 in lyn:
            text = text.replace(oldcss7, '{| class="wikitable"')

        if 'Totaal ||' in lyn:
            totaal_lyn = lyn.replace(' Totaal ', 'Totaal')
            totaal_lyn = lyn.replace('||', '!!')
            text = text.replace(lyn, totaal_lyn)

        blad.text = text

    blad.save('Verander na wikitable', minor=False)

print('done')
