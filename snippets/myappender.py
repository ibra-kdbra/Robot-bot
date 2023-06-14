#!/usr/bin/env python

for n in range(101,109):
	with open("jp_nat_high.txt", "a") as myfile:
	    myfile.write("{{-start-}}\n" +
"xxxJapan Nasionale Roete " + str(n) + "yyy\n" + 
"'''Nasionale Roete " + str(n) + "''' is 'n nasionale snelweg van [[Japan]]. <ref name=\"ref1\"/>\n\n" + 
"== Verwysings ==\n" + 
"{{Verwysings|verwysings=\n" + 
"<ref name=\"ref1\">{{jp}} [http://www.mlit.go.jp/road/ir/ir-data/tokei-nen/2015/pdf/d_genkyou26.pdf www.mlit.go.jp]</ref>\n" + 
"}}\n\n" + 
"{{Saadjie}}\n\n" + 
"{{-stop-}}\n\n")  


