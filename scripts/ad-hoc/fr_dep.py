#!/usr/bin/env python
import pywikibot
import json

def getJson(clmDict, claimId):
	val = "no_key"
	if claimId in clmDict:
		for clm in clmDict[claimId]:
			val = clm.toJSON()['mainsnak']['datavalue']['value']
	return val

### end of functions ###

site = pywikibot.Site("en", "wikipedia")

dep_list = [ "Ain", "Aisne", "Allier", "Alpes-de-Haute-Provence", "Hautes-Alpes", "Alpes-Maritimes", "Ardèche", "Ardennes", "Ariège", "Aube", "Aude", "Aveyron", "Bouches-du-Rhône", "Calvados", "Cantal", "Charente", "Charente-Maritime", "Cher", "Corrèze", "Corse-du-Sud", "Haute-Corse", "Côte-d'Or", "Côtes-d'Armor", "Creuse", "Dordogne", "Doubs", "Drôme", "Eure", "Eure-et-Loir", "Finistère", "Gard", "Haute-Garonne", "Gers", "Gironde", "Hérault", "Ille-et-Vilaine", "Indre", "Indre-et-Loire", "Isère", "Jura", "Landes", "Loir-et-Cher", "Loire", "Haute-Loire", "Loire-Atlantique", "Loiret", "Lot", "Lot-et-Garonne", "Lozère", "Maine-et-Loire", "Manche", "Marne", "Haute-Marne", "Mayenne", "Meurthe-et-Moselle", "Meuse", "Morbihan", "Moselle", "Nièvre", "Nord", "Oise", "Orne", "Pas-de-Calais", "Puy-de-Dôme", "Pyrénées-Atlantiques", "Hautes-Pyrénées", "Pyrénées-Orientales", "Bas-Rhin", "Haut-Rhin", "Rhône_(department)", "Haute-Saône", "Saône-et-Loire", "Sarthe", "Savoie", "Haute-Savoie", "Parys", "Seine-Maritime", "Seine-et-Marne", "Yvelines", "Deux-Sèvres", "Somme", "Tarn", "Tarn-et-Garonne", "Var", "Vaucluse", "Vendée", "Vienne", "Haute-Vienne", "Vosges", "Yonne", "Territoire de Belfort", "Essonne", "Hauts-de-Seine", "Seine-Saint-Denis", "Val-de-Marne", "Val-d'Oise"]

for dep in dep_list:
	page = pywikibot.Page(site, dep)
	item = pywikibot.ItemPage.fromPage(page)
	item_dict = item.get()
	clm_dict = item_dict["claims"]

	try:
		titel = item_dict["labels"]["af"]
	except KeyError:
		titel = item_dict["labels"]["en"]
			
	nommer = getJson(clm_dict, 'P2586')
	logo = getJson(clm_dict, 'P94')
	gewes = "default"
	hoofstad = '____'
	inwoners = '___'
	arrondissemente ='_'
	hoof = getJson(clm_dict, 'P6')
	ligging = getJson(clm_dict, 'P242')
	inception = "default"

	with open("dep_list.txt", "a") as myfile:
	    myfile.write("{{-start-}}\n" +
"{{Franse département\n" +
" logo=[[Beeld:"+ logo+"|100px]]\n"
"| département=" + titel + " ("+ nommer +")\n" +
"| gewes=\n" +
"| Prefektuur=\n" +
"| bevolking=\n" +
"| DatBev=\n" +
"| arr=\n" +
"| president=\n" +
"| ligging=[[Beeld:" + ligging + "|300px]]\n" +
"}}\n" +

"'''" + titel + "''' is sedert ____ 'n [[département]] in ____, [[Frankryk]], met ongeveer ____ inwoners. Die hoofstad (prefektuur) is ____.\n\n"
"{{Départements van Frankryk}}\n\n"
"{{Saadjie}}\n"
"{{-stop-}}\n\n")  

