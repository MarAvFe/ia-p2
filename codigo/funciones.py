#!/usr/bin/python
import time
import threading
import logging
from pyDatalog import pyEngine, Logic
from pyDatalog.pyDatalog import assert_fact, load, create_terms, ask
create_terms('derived, etymologically, etymologically_related, etymology, has_derived_form, variant, esHijo, sonHermanos, esTio, sonPrimos, A, B, P1,P2, T, S, PP1, PP2, G1,G,esHijo, etymology,etymological_origin_of,is_derived_from, H, P, IH,IP,R')

pyEngine.Logging = True
logging.basicConfig(level=logging.INFO)
datos =[["senabe", "sannup"], ["waniigan","wangan"], ["waniigan","wannigan"]]

class myThread (threading.Thread):
	def __init__(self, threadID, loadStr, logic):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.loadStr = loadStr
		self.logic = logic
	def run(self):
		#threadLock.acquire()
		Logic(self.logic)
		loadBigString(self.loadStr, self.threadID)
		#threadLock.release()

def loadBigString(string,cnt):
	try:
		load(string)
	except Exception:
		import traceback
		print( traceback.format_exc())

db = []
threadLock = threading.Lock()
def loadDBRels():
	words = {}
	langs = {}
	derivedLoadStr = ""
	etymologicallyLoadStr = ""
	etymologically_relatedLoadStr = ""
	etymologyLoadStr = ""
	has_derived_formLoadStr = ""
	variantLoadStr = ""
	loadStrs = ["","","","","",""]
	loadStrsNums = [0,0,0,0,0,0]
	numWords = 0
	threads = []
	saved = 0
	#with open("../etymwn/etymwn.tsv") as f:
	with open("../etymwn/summaryDB.tsv") as f:
		i = 0
		for l in f:
			tmp = l.split("\t")
			rel = tmp[1]
			if(rel == 'rel:etymological_origin_of' or rel == 'rel:is_derived_from'):
				#print(rel)
				continue

			lft = tmp[0]
			rgt = tmp[2]
			tmpLft = lft.split(': ')
			langLft, wordLft = tmpLft[0], tmpLft[1]
			tmpRgt = rgt.split(': ')
			langRgt, wordRgt = tmpRgt[0], tmpRgt[1].split("\n")[0]

			try:
				u = langs[langLft]
			except KeyError:
				langs[langLft] = langLft

			try:
				u = langs[langRgt]
			except KeyError:
				langs[langRgt] = langRgt

			try:
				u = words[wordLft]
				saved += 1
			except KeyError:
				words[wordLft] = (i,1)

			try:
				u = words[wordRgt]
				saved += 1
			except KeyError:
				words[wordRgt] = (i,2)


			for k in range(len(loadStrs)):
				if(loadStrsNums[k] > 15000):
					th = myThread(k, loadStrs[k], Logic(True))
					th.start()
					threads.append(th)
					print(len(loadStrs[k].split("\n")),"remaining of", loadStrs[k].split("(")[0])
					#load(loadStrs[k])
					loadStrs[k] = ""
					loadStrsNums[k] = 0

			if(wordRgt == 'anchor' or wordLft == 'anchor'):
				print(rel, "(", wordLft, ",", wordRgt, ")")
			#print("boop:", len(langs), len(words))
			#print("beep:", languages.index(langLft), words[wordLft], languages.index(langRgt), words[wordRgt], rel)
			langLftIdx = langs[langLft]
			langRgtIdx = langs[langRgt]
			if(rel == 'rel:derived'):
				#loadStrs[0] += "derived("+str(langLftIdx)+", "+str(words[wordLft])+", "+str(langRgtIdx)+", "+str(words[wordRgt])+")\n"
				#loadStrsNums[0] += 1
				+ derived(str(langLftIdx), str(words[wordLft]), str(langRgtIdx), str(words[wordRgt]))
			elif(rel == 'rel:etymologically'):
				#loadStrs[1] += "etymologically("+str(langLftIdx)+", "+str(words[wordLft])+", "+str(langRgtIdx)+", "+str(words[wordRgt])+")\n"
				#loadStrsNums[1] += 1
				+ etymologically(str(langLftIdx), str(words[wordLft]), str(langRgtIdx), str(words[wordRgt]))
			elif(rel == 'rel:etymologically_related'):
				#loadStrs[2] += "etymologically_related("+str(langLftIdx)+", "+str(words[wordLft])+", "+str(langRgtIdx)+", "+str(words[wordRgt])+")\n"
				#loadStrsNums[2] += 1
				+ etymologically_related(str(langLftIdx), str(words[wordLft]), str(langRgtIdx), str(words[wordRgt]))
			elif(rel == 'rel:etymology'):
				#loadStrs[3] += "etymology("+str(langLftIdx)+", "+str(words[wordLft])+", "+str(langRgtIdx)+", "+str(words[wordRgt])+")\n"
				#loadStrsNums[3] += 1
				+ etymology(str(langLftIdx), str(words[wordLft]), str(langRgtIdx), str(words[wordRgt]))
			elif(rel == 'rel:has_derived_form'):
				#loadStrs[4] += "has_derived_form("+str(langLftIdx)+", "+str(words[wordLft])+", "+str(langRgtIdx)+", "+str(words[wordRgt])+")\n"
				#loadStrsNums[4] += 1
				+ has_derived_form(str(langLftIdx), str(words[wordLft]), str(langRgtIdx), str(words[wordRgt]))
			elif(rel.find('rel:variant') > -1):
				#loadStrs[5] += "variant("+str(langLftIdx)+", "+str(words[wordLft])+", "+str(langRgtIdx)+", "+str(words[wordRgt])+")\n"
				#loadStrsNums[5] += 1
				+ variant(str(langLftIdx), str(words[wordLft]), str(langRgtIdx), str(words[wordRgt]))

			i += 1
			if i%100000==0:
				print("beep:", langs[langLft], words[wordLft], langs[langRgt], words[wordRgt], rel, len(words), len(langs))
				print(i)
			#if i>300000:
			#	break
		for k in range(len(loadStrs)):
			load(loadStrs[k])
			print(len(loadStrs[k].split("\n")),"remaining of", loadStrs[k].split("(")[0])
			loadStrs[k] = ""
			loadStrsNums[k] = 0
		print("dbSize:",i, "lenWords:", len(words), "saved:", saved)
		print("Now waiting to join:", time.strftime("%H:%M:%S"))
		print()
		for t in threads:
			t.join()
			print("joined a thread:",time.strftime("%H:%M:%S"))
		print("Joined every thread:", time.strftime("%H:%M:%S"))
		return words, langs

def cargarRelaciones(_derived, _etymologically, _etymologically_related, _etymology, _has_derived_form, _variant, etymological_origin_of, is_derived_from):
	if (_derived):
		esHijo(H, P) <= derived(IP, P, IH, H)
	else:
		pyEngine.retract(esHijo(H, P) <= derived(IP, P, IH, H))
	if (_etymologically):
		esHijo(H, P) <= etymologically(IP, P, IH, H)
	else:
		pyEngine.retract(esHijo(H, P) <= etymologically(IP, P, IH, H))
	if (_etymologically_related):
		esHijo(H, P) <= etymologically_related(IP, P, IH, H)
	else:
		pyEngine.retract(esHijo(H, P) <= etymologically_related(IP, P, IH, H))
	if (_etymology):
		esHijo(H, P) <= etymology(IP, P, IH, H)
	else:
		pyEngine.retract(esHijo(H, P) <= etymology(IP, P, IH, H))
	if (_has_derived_form):
		esHijo(H, P) <= has_derived_form(IP, P, IH, H)
	else:
		pyEngine.retract(esHijo(H, P) <= has_derived_form(IP, P, IH, H))
	if (_variant):
		esHijo(H, P) <= variant(IP, P, IH, H)
	else:
		pyEngine.retract(esHijo(H, P) <= variant(IP, P, IH, H))
	if (etymological_origin_of):
		esHijo(H, P) <= etymology(IH, H, IP, P)	#etymological_origin_of
	else:
		pyEngine.retract(esHijo(H, P) <= etymology(IH, H, IP, P))
	if (is_derived_from):
		esHijo(H, P) <= has_derived_form(IH, H, IP, P) #is_derived_from
	else:
		pyEngine.retract(esHijo(H, P) <= has_derived_form(IH, H, IP, P)) #is_derived_from


def main():

	esHijo(H, P, True) <= esHijo(H, P)
	esHijo(H, P, False) <= ~esHijo(H, P)

	sonHermanos(A, B, True) <= sonHermanos(A, B)
	sonHermanos(A, B, False) <= ~sonHermanos(A, B)
	sonHermanos(A, B) <= esHijo(A, P1) & esHijo (B, P2) & (P1 == P2) & (A!=B)

	esTio(T, S , True) <= esTio(T, S)
	esTio(T, S, False) <= ~esTio(T, S)
	esTio(T, S) <= esHijo(S, P) & sonHermanos(T, P) & (P!=T)

	sonPrimos(P1, P2, G, True) <= sonPrimos(P1, P2, G )
	sonPrimos(P1, P2, 0, False) <= ~sonPrimos(P1, P2, G)
	sonPrimos(P1, P2, G) <= esHijo(P1, PP1) & esHijo(P2, PP2) & sonHermanos(PP1, PP2) & (G==1)
	sonPrimos(P1, P2, G) <= esHijo(P1, PP1) & esHijo(P2, PP2) & ~sonHermanos(PP1, PP2) & sonPrimos(PP1, PP2, G1) & (G==G1+1)

	words, languages = loadDBRels()
	cargarRelaciones(True, True, True, True, True, True, True, True)
	lis = list(words)[2000:2020]
	print(len(lis))
	print("{")
	for j in range(len(lis)):
		print("    '"+str(lis[j])+"': "+str(words[lis[j]])+",")
	print("}")
	c = 0
	while True:
		print(words[lis[2]], words[lis[3]],lis[2], lis[3])
		quest2 = 'esHijo('+str(words[lis[2]])+','+str(words[lis[3]])+',R)'
		print(quest2)
		print(c,":",ask(quest2))
		print(words[lis[3]], words[lis[2]])
		quest = 'esHijo('+str(words[lis[3]])+','+str(words[lis[2]])+',R)'
		print(quest)
		print(c,":",ask(quest))
		c += 1
		time.sleep(10)

main()
