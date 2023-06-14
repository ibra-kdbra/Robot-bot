#!/usr/bin/env python
import pywikibot

site = pywikibot.Site("af", "wikipedia")


prov_lys = ["Asia (Romeinse provinsie)","Assyria (Romeinse provinsie)","Bithinië","Cilicia","Commagene","Corsica et Sardinia","Cyrenaica","Dacië","Galasië","Gallia Lugdunensis","Hispania Baetica","Hispania Tarraconensis","Italia (Romeinse provinsie)","Iudaea (Romeinse provinsie)","Licaonië","Licië","Macedonië (Romeinse provinsie)","Mauretania Caesariensis","Mauretania Tingitana","Moesië","Noricum","Pannonië","Pamfilië","Pisidië","Raetia","Sicilia (Romeinse provinsie)","Sophene","Syria (Romeinse provinsie)"]

for prov in prov_lys:
	page = pywikibot.Page(site, prov)
	page.text = '[[Lêer:RomanEmpire_117.svg|duimnael|regs]]\n\n'
	page.text += "'''" + prov.replace(' (Romeinse provinsie)','') + "''' was 'n Romeinse provinsie.<ref name=\"thoughtco\" /><ref name=\"unrv\" />\n\n"
	page.text += '== Verwysings ==\n{{Verwysings|verwysings=\n'
	page.text += '<ref name="thoughtco">{{en}}[https://www.thoughtco.com/provinces-of-the-roman-empire-120862 provinces of the roman empire]</ref>\n'
	page.text += '<ref name="unrv">{{en}}[https://www.unrv.com/provinces/province-chronology.php province-chronology]</ref>\n'
	page.text += '}}\n{{Saadjie}}\n{{Romeinse provinsies 120}}\n\n[[Kategorie:Romeinse provinsies]]'
	#print(page.text)
	page.save('Nuwe bladsy geskep - ' + prov)
