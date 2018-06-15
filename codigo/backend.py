#!/usr/bin/python
import time
import threading
import logging
from pyDatalog import pyEngine, Logic
from pyDatalog.pyDatalog import assert_fact, load, create_terms, ask
create_terms('derived, etymologically, etymologically_related, etymology, has_derived_form, variant, esHijo, sonHermanos, esTio, sonPrimos, A, B, P1,P2, T, S, PP1, PP2, G1,G,esHijo, etymology,etymological_origin_of,is_derived_from, H, P, IH,IP,R')
create_terms("esHijo, getPadre, etymology,etymological_origin_of,has_derived_form,is_derived_from, H, P, IH,IP,R, H1")
create_terms('I,getHijos2, descendientes,gradoPrimos, sonPrimas, lIdiomasRpalabra, D1,D2,D3,D4, D5, D6, ID, LI, LA, PAL,PAD, _PADRES, _IDIOMAS, derived, etymologically, etymologically_related, etymology, has_derived_form, variant, esHijo, sonHermanos,antepasados, esTio, sonPrimos, A, B, P1,P2, T, S, PP1, PP2, G1,G')
create_terms('getHijos2,resultado,_estaRelacionada, _soloIdiomas,getIdiomas, H1, getHijos2,R_IP, R_P,R_IH, R_H, R2, descendientes,getPadres2, ascendencia,_antepasados,A,B,C,D,E,F,GR1,R1, R2,R3')
create_terms('contarPalabrasComunes, C1')
create_terms("lPalabrasIdiomaOriginadas, getHijosIdioma,Palabra ,Idioma,Hijos, getHijosI, hijosIdioma, getPrimas, X, Y ")
create_terms('getPalabrasXidioma, palabrasComunes, I1, I2, IA, IB, IP1, IP2, IPP1, IPP2, IT, IS, sonElMismo, O')

#pyEngine.Logging = True
#logging.basicConfig(level=logging.INFO)

class myThread (threading.Thread):
	def __init__(self, threadID, loadStr, logic):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.loadStr = loadStr
		self.logic = logic
	def run(self):
		Logic(self.logic)
		loadBigString(self.loadStr, self.threadID)

def loadBigString(string,cnt):
	try:
		load(string)
	except Exception:
		import traceback
		print( traceback.format_exc())

#------ Es hijo
esHijo(H, P) <= esHijo(IP, P, IH, H)
esHijo(IH, H, IP, P, R) <= esHijo(IP, P, IH, H)

sonElMismo(IA, A, IB, B, R) <= (IA == IB) & (A == B)

# ----- Determinar si dos palabras son heman@s
sonHermanos(IA, A, IB, B, R) <= esHijo(IA, A, IP, P) & esHijo (IB, B, IP, P) & (A!=B)#& ~sonElMismo(IA, A, IB, B, O)
#sonHermanos(IA, A, IB, B, R) <= esHijo(IA, A, IP, P) & esHijo (IB, B, IP, P) & (A!=B)
sonHermanos(IA, A, IB, B) <= sonHermanos(IA, A, IB, B, R)

#------ Determinar si dos palabras son prim@s y también se obtiene el grado
sonPrimos(IP1, P1, IP2, P2, G, True) <= sonPrimos(IP1, P1, IP2, P2, G)
sonPrimos(IP1, P1, IP2, P2, 0, False) <= ~sonPrimos(IP1, P1, IP2, P2, G)
sonPrimos(IP1, P1, IP2, P2, G) <= esHijo(IP1, P1, IPP1, PP1) & esHijo(IP2, P2, IPP2, PP2) & sonHermanos(IPP1, PP1, IPP2, PP2) & (G==1)
sonPrimos(IP1, P1, IP2, P2, G) <= esHijo(IP1, P1, IPP1, PP1) & esHijo(IP2, P2, IPP2, PP2) & ~sonHermanos(IPP1, PP1, IPP2, PP2) & sonPrimos(IPP1, PP1, IPP2, PP2, G1) & (G==G1+1)
sonPrimas(IP1, P1, IP2, P2) <= sonPrimos(IP1, P1, IP2, P2, G)

getPrimas(IP1, P1, IP2, P2) <= sonPrimos(IP1, P1, IP2, P2, G)

#------- Determina si dos palabras son primas, y el grado
gradoPrimos(IP1, P1, IP2, P2, G) <= sonPrimos(IP1, P1, IP2, P2, G)

#------- Determinar si una palabra es tía de otra
esTio(IT, T, IS, S, R) <= esHijo(IS, S, IP, P) & sonHermanos(IT, T, IP, P) & (P!=T)
esTio(IT, T, IS, S, R) <= esHijo(IS, S, IP, P) & sonHermanos(IT, T, IP, P) & (IP!=IT)
getPadre(IH, H, I)<=esHijo(IP, P, IH, H)


#--- Determinar si una palabra está relacionada con un idioma

getHijos2(P, IH, H) <= esHijo(IP, P, IH, H)
descendientes(P, I, R) <= getHijos2 (P, I, R)
descendientes(P, I, R) <= getHijos2 (P, R_IH, R_H) & descendientes(R_H, I, R)
getPadres2(H, IP, P) <= esHijo(IP, P, IH, H)
ascendencia(H, I, R) <= getPadres2(H, I, R)
ascendencia(H, I, R) <= getPadres2(H, R_IP, R_P) & ascendencia(R_P, I, R)

# Idioma de la misma palabra
getIdiomas(P,IP, IP) <= esHijo(IP, P, IH, H)
getIdiomas(H,IH, IP) <= esHijo(IP, P, IH, H)

_antepasados(H, I, R) <= ascendencia(H, I, R)
_antepasados(P, I, R) <= descendientes(P, I, R)
_antepasados(P, I, R) <= getIdiomas(P,I, R)

#---- Listar los idiomas relacionados con una palabra
_soloIdiomas(P, I)<=_antepasados(P, I, R)


#------- Obtener el conjunto de todas las palabras en un idioma originadas por una palabra
getHijosI(P, H, IH) <= esHijo(IP, P, IH, H)
hijosIdioma(P, IH, H) <= getHijosI(P, H, IH)
hijosIdioma(Palabra, IH, R) <= getHijosI(P, H, IH) & hijosIdioma(H, IH, R)

#------- Palabras comunes dos idiomas
#----Determinar si una palabra está relacionada con un idioma
_estaRelacionada(P, IH, R) <= _antepasados(P, I,R) & (I==IH)
_estaRelacionada(P, IH, True) <= _estaRelacionada(P, IH, R)
_estaRelacionada(P, IH, False) <= ~_estaRelacionada(P, IH, R)

#-----------  Listar todas las palabras comunes entre dos idiomas
create_terms('getPalabrasXidioma, palabrasComunes, I1, I2')
getPalabrasXidioma(I, R) <= esHijo(IP, P, I, R)
getPalabrasXidioma(I, R) <= esHijo(I, R, IH, H)
palabrasComunes(I1, I2, R1) <= getPalabrasXidioma(I1, R1) & getPalabrasXidioma(I2, R2) & (R1==R2)

#-----------Número de palabras comunes entre dos idiomas
contarPalabrasComunes(I1, I2, R1) <= getPalabrasXidioma(I1, R1) & getPalabrasXidioma(I2, R2) & (R1==R2)


def __sonHermanos(_idiomaA, _nombreA, _idiomaB, _nombreB):
	# Determinar si dos palabras son heman@s
	if (ask('sonHermanos('+_idiomaA+','+_nombreA+','+_idiomaB+','+ _nombreB+ ', R)')):
		return "Son hermanas"
	else:
		return "No son hermanas"

def __sonPrimas(_idiomaA, _nombreA, _idiomaB, _nombreB):
	# Determinar si dos palabras son prim@s
	if(ask('sonPrimas('+_idiomaA+','+_nombreA+','+_idiomaB+','+ _nombreB+ ')')):
		return "Son primas"
	else:
		return "No son primas"

def __gradoPrimas(_idiomaA, _nombreA, _idiomaB, _nombreB):
	# Determina si son primas y en qué grado
	consulta = ask('gradoPrimos('+_idiomaA+','+_nombreA+','+_idiomaB+','+ _nombreB+ ', R)')
	if (consulta):
		return "Son primas", consulta.answers[0][0]
	else:
		return "No son primas", 0

def __esHija(_idiomaHijo, _hijo, _idiomaPadre, _padre):
	# Determinar si una palabra es hij@ de otra
	if (ask('esHijo('+_idiomaHijo+','+ _hijo+ ','+ _idiomaPadre+ ','+ _padre+ ', R)')):
		return "Sí es hija"
	else:
		return "No es hija"

def __esTia(_idiomaTio, _tio, _idiomaSobrino, _sobrino):
	# Determinar si una palabra es tí@
	if (ask('esTio('+_idiomaTio+','+_tio+','+_idiomaSobrino+','+ _sobrino+ ', R)')):
		return "Sí es tía"
	else:
		return "No es tía"

def __esPalabraRelacionadaIdioma(_palabra, _idioma):
	#Determinar si una palabra está relacionada con un idioma (Si / No)
	if (ask('_antepasados('+_palabra+','+ _idioma+ ', R)')):
		return "Sí está relacionada"
	else:
		return "No está relacionada"

def __palabrasEnUnIdiomaOriginadasPorPalabra(_palabra, _idioma):
	#Obtener el conjunto de todas las palabras en un idioma originadas por una palabra específica
	consulta = ask('hijosIdioma('+_palabra+','+ _idioma+ ', R)')
	if (consulta):
		return consulta.answers
	else:
		return "No se obtuvo coincidencias"


def __idiomasRelacionadosPalabra(_palabra):
	# Listar los idiomas relacionados con una palabra
	consulta = ask('_soloIdiomas('+_palabra+', R)')
	if (consulta):
		return consulta.answers
	else:
		return "No hay idiomas relacionados"

def __listarPalabrasComunesIdiomas(_idiomaA, _idiomaB):
	# Listar todas las palabras comunes entre dos idiomas
	consulta = ask('contarPalabrasComunes('+_idiomaA+', '+_idiomaB+', R1)')
	if (consulta):
		return consulta.answers
	else:
		return "No hubo coincidencia."


def __numeroPalabrasComunesIdiomas(_idiomaA, _idiomaB):
	# Contar todas las palabras comunes entre dos idiomas
	consulta = ask('contarPalabrasComunes('+_idiomaA+', '+_idiomaB+', R1)')
	if (consulta):
		return _len(consulta.answers)
	else:
		return 0

db = []
threadLock = threading.Lock()
def loadDBRels():
	words = {}
	langs = {}
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
				pass#continue

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

			#print("boop:", len(langs), len(words))
			langLftIdx = langs[langLft]
			langRgtIdx = langs[langRgt]
			#if wordLft == 'beest' or wordRgt == 'beest' or wordLft == 'apartheid' or wordRgt == 'apartheid':
			#	print("beep:", (str(langLftIdx), hash(words[wordLft]), str(langRgtIdx), hash(words[wordRgt])), rel)
			if(rel == 'rel:derived'):
				+ derived(str(langLftIdx), hash(words[wordLft]), str(langRgtIdx), hash(words[wordRgt]))
			elif(rel == 'rel:etymologically'):
				+ etymologically(str(langLftIdx), hash(words[wordLft]), str(langRgtIdx), hash(words[wordRgt]))
			elif(rel == 'rel:etymologically_related'):
				+ etymologically_related(str(langLftIdx), hash(words[wordLft]), str(langRgtIdx), hash(words[wordRgt]))
			elif(rel == 'rel:etymology'):
				+ etymology(str(langLftIdx), hash(words[wordLft]), str(langRgtIdx), hash(words[wordRgt]))
			elif(rel == 'rel:etymological_origin_of'):
				+ etymology(str(langRgtIdx), hash(words[wordRgt]), str(langLftIdx), hash(words[wordLft]))
			elif(rel == 'rel:has_derived_form'):
				+ has_derived_form(str(langLftIdx), hash(words[wordLft]), str(langRgtIdx), hash(words[wordRgt]))
			elif(rel == 'rel:is_derived_from'):
				+ has_derived_form(str(langRgtIdx), hash(words[wordRgt]), str(langLftIdx), hash(words[wordLft]))
			elif(rel.find('rel:variant') > -1):
				+ variant(str(langLftIdx), hash(words[wordLft]), str(langRgtIdx), hash(words[wordRgt]))

			i += 1
			if i%100000==0:
				print("beep:", langs[langLft], words[wordLft], langs[langRgt], words[wordRgt], rel, len(words), len(langs))
				print(i)

		print("dbSize:",i, "lenWords:", len(words), "saved:", saved)
		return words, langs


def cargarRelaciones(_derived, _etymologically, _etymologically_related, _etymology, _has_derived_form, _variant, etymological_origin_of, is_derived_from):
	if (_derived):
		esHijo(IP, P, IH, H) <= derived(IP, P, IH, H)
	else:
		pyEngine.retract(esHijo(IP, P, IH, H) <= derived(IP, P, IH, H))
	if (_etymologically):
		esHijo(IP, P, IH, H) <= etymologically(IP, P, IH, H)
	else:
		pyEngine.retract(esHijo(IP, P, IH, H) <= etymologically(IP, P, IH, H))
	if (_etymologically_related):
		esHijo(IP, P, IH, H) <= etymologically_related(IP, P, IH, H)
	else:
		pyEngine.retract(esHijo(IP, P, IH, H) <= etymologically_related(IP, P, IH, H))
	if (_etymology):
		esHijo(IP, P, IH, H) <= etymology(IP, P, IH, H)
	else:
		pyEngine.retract(esHijo(IP, P, IH, H) <= etymology(IP, P, IH, H))
	if (_has_derived_form):
		esHijo(IP, P, IH, H) <= has_derived_form(IP, P, IH, H)
	else:
		pyEngine.retract(esHijo(IP, P, IH, H) <= has_derived_form(IP, P, IH, H))
	if (_variant):
		esHijo(IP, P, IH, H) <= variant(IP, P, IH, H)
	else:
		pyEngine.retract(esHijo(IP, P, IH, H) <= variant(IP, P, IH, H))


def main():
	words, languages = loadDBRels()
	cargarRelaciones(True, True, True, True, True, True, True, True)
	while True:
		idiomaPadre = 'afr'
		padre = str(hash(words['bees']))
		idiomaHijo = 'nld'
		hija = str(hash(words['beest']))
		print(padre, hija, 'bees', 'beest')
		print("Prueba función es hija: ", __esHija(idiomaPadre, padre, idiomaHijo, hija))
		print("Prueba función es hija: ", __esHija(idiomaHijo, hija, idiomaPadre, padre))

		apartheid = str(hash(words['apartheid']))
		aviation = str(hash(words['aviation']))
		aviarius = str(hash(words['aviarius']))
		aviarium = str(hash(words['aviarium']))
		print("Prueba función son hermanas: ", __sonHermanos('fra', apartheid, 'ita', apartheid)) #true
		print("Prueba función son hermanas: ", __sonHermanos('fra', apartheid, 'afr', apartheid)) #false
		print("Prueba función son hermanas: ", __sonHermanos('afr', apartheid, 'afr', apartheid)) #false
		print("Prueba función son hermanas: ", __sonHermanos('fra', aviation, 'lat', aviarius)) #true

		print("Prueba función son primas: ", __sonPrimas('eng', aviation, 'lat', aviarium)) #true
		print("Prueba función son primas: ", __sonPrimas('fra', aviation, 'lat', aviarium)) #false
		print("Prueba función son primas: ", __sonPrimas('lat', aviarium, 'lat', aviarius)) #false
		print("Prueba función son primas: ", __sonPrimas('lat', aviarium, 'afr', apartheid)) #false

		print("Prueba función son tios: ", __esTia('lat', aviarius, 'eng', aviation))# true
		print("Prueba función son tios: ", __esTia('fra', aviation, 'lat', aviarium))# true
		print("Prueba función son tios: ", __esTia('eng', aviation, 'lat', aviarius))# false

		time.sleep(10)

#-lat: avis
#  -lat: aviarius
#    -lat: aviarium
#  -fra: aviation
#    -eng: aviation


main()
