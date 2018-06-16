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
create_terms('getPalabrasXidioma, palabrasComunes, I1, I2, IA, IB, IP1, IP2, IPP1, IPP2, IT, IS, sonElMismo, O, numeroPalabrasComunes, _hijosDeUnIdioma, __hijosDeUnIdioma')

#pyEngine.Logging = True
#logging.basicConfig(level=logging.INFO)

DATABASE = "../etymwn/summaryDB.tsv"

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
hijosIdioma(P, IH, R) <= getHijosI(P, H, IH) & hijosIdioma(H, IH, R)
#------- Palabras comunes dos idiomas
#----Determinar si una palabra está relacionada con un idioma
_estaRelacionada(P, IH, R) <= _antepasados(P, IH, R) #& (I==IH)
_estaRelacionada(P, IH, True) <= _estaRelacionada(P, IH, R)
_estaRelacionada(P, IH, False) <= ~_estaRelacionada(P, IH, R)
#-----------  Listar todas las palabras comunes entre dos idiomas
create_terms('getPalabrasXidioma, palabrasComunes, I1, I2')
getPalabrasXidioma(I, R) <= esHijo(IP, P, I, R)
getPalabrasXidioma(I, R) <= esHijo(I, R, IH, H)
palabrasComunes(I1, I2, R1) <= getPalabrasXidioma(I1, R1) & getPalabrasXidioma(I2, R1) #& (R1==R2)
#-----------Número de palabras comunes entre dos idiomas
#contarPalabrasComunes(I1, I2, R1) <= getPalabrasXidioma(I1, R1) & getPalabrasXidioma(I2, R1) # & (R1==R2)
#----------- Número de palabras comunes entre dos idiomas
(numeroPalabrasComunes[I1, I2]==len_(R1)) <= palabrasComunes(I1, I2, R1)
contarPalabrasComunes(I1, I2, R1) <= (R1==[numeroPalabrasComunes[I1, I2]])


_hijosDeUnIdioma(IP,IH, H) <= esHijo(IP,P,IH,H)

def readFileWord(respuesta):
	tmp = respuesta.split('zzz')
	linea = int(tmp[1])
	izq = True if tmp[2] == '1' else False
	global DATABASE
	with open(DATABASE) as f:
		for i, line in enumerate(f):
			if i == linea:
				if izq:
					print(i, linea, tmp[2], '+++++++++++++++++++++++++++++++++++++++++')
					return line.split('\t')[0]
				else:
					print(i, linea, tmp[2], '-----------------------------------------')
					return line.split('\t')[2].split('\n')[0]


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
		words = []
		for r in consulta.answers:
			words.append(r[0])
			#words.append(readFileWord(r[0]))
		return words
	else:
		return "No se obtuvo coincidencias"


def __idiomasRelacionadosPalabra(_palabra):
	# Listar los idiomas relacionados con una palabra
	consulta = ask('_soloIdiomas('+_palabra+', R)')
	if (consulta):
		words = []
		for r in consulta.answers:
			words.append(r[0])
		return words
	else:
		return "No hay idiomas relacionados"

def __listarPalabrasComunesIdiomas(_idiomaA, _idiomaB):
	# Listar todas las palabras comunes entre dos idiomas
	consulta = ask('palabrasComunes('+_idiomaA+', '+_idiomaB+', R1)')
	if (consulta):
		words = []
		for r in consulta.answers:
			words.append(r[0])
			#words.append(readFileWord(r[0]))
		return words
	else:
		return "No hubo coincidencia."

def __numeroPalabrasComunesIdiomas(_idiomaA, _idiomaB):
	# Contar todas las palabras comunes entre dos idiomas
	consulta = ask('contarPalabrasComunes('+_idiomaA+', '+_idiomaB+', R1)')
	if (consulta):
		return _len(consulta.answers)
	else:
		return 0

def __hijosDeUnIdioma(_idioma):
	# Listar todas las palabras comunes entre dos idiomas
	consulta = ask('getPalabrasXidioma('+_idioma+', A)')
	if (consulta):
		words = []
		for r in consulta.answers:
			print(r[0])
			words.append(r[0])
			#words.append(readFileWord(r[0]))
			return words
		else:
			return "No hubo coincidencia."

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
	global DATABASE
	with open(DATABASE) as f:
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

			#try:
			#	u = langs[langLft]
			#except KeyError:
			#	langs[langLft] = langLft

			#try:
			#	u = langs[langRgt]
			#except KeyError:
			#	langs[langRgt] = langRgt

			#try:
			#	u = words[wordLft]
			#	saved += 1
			#except KeyError:
			#	words[wordLft] = 'zzz'+str(i)+'zzz1'

			#try:
			#	u = words[wordRgt]
			#	saved += 1
			#except KeyError:
			#	words[wordRgt] = 'zzz'+str(i)+'zzz2'

			#if wordLft == 'beest' or wordRgt == 'beest' or wordLft == 'apartheid' or wordRgt == 'apartheid':
			#	print("beep:", (str(langLftIdx), hash(words[wordLft]), str(langRgtIdx), hash(words[wordRgt])), rel)
			if(rel == 'rel:derived'):
				+ derived(langLft, wordLft, langRgt, wordRgt)
			elif(rel == 'rel:etymologically'):
				+ etymologically(langLft, wordLft, langRgt, wordRgt)
			elif(rel == 'rel:etymologically_related'):
				+ etymologically_related(langLft, wordLft, langRgt, wordRgt)
			elif(rel == 'rel:etymology'):
				+ etymology(langLft, wordLft, langRgt, wordRgt)
			elif(rel == 'rel:etymological_origin_of'):
				+ etymology(langRgt, wordRgt, langLft, wordLft)
			elif(rel == 'rel:has_derived_form'):
				+ has_derived_form(langLft, wordLft, langRgt, wordRgt)
			elif(rel == 'rel:is_derived_from'):
				+ has_derived_form(langRgt, wordRgt, langLft, wordLft)
			elif(rel.find('rel:variant') > -1):
				+ variant(langLft, wordLft, langRgt, wordRgt)

			i += 1
			if i%100000==0:
				print("beep:", langLft, wordLft, langRgt, wordRgt, rel, len(words), len(langs))
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
	#if (etymological_origin_of):
	#	esHijo(IP, P, IH, H) <= etymology(IH, H, IP, P)
	#else:
	#	pyEngine.retract(esHijo(IP, P, IH, H) <= etymology(IP, P, IH, H))
	if (_has_derived_form):
		esHijo(IP, P, IH, H) <= has_derived_form(IP, P, IH, H)
	else:
		pyEngine.retract(esHijo(IP, P, IH, H) <= has_derived_form(IP, P, IH, H))
	#if (is_derived_from):
	#	esHijo(IP, P, IH, H) <= has_derived_form(IH, H, IP, P)
	#else:
	#	pyEngine.retract(esHijo(IP, P, IH, H) <= has_derived_form(IP, P, IH, H))
	if (_variant):
		esHijo(IP, P, IH, H) <= variant(IP, P, IH, H)
	else:
		pyEngine.retract(esHijo(IP, P, IH, H) <= variant(IP, P, IH, H))


def main():
	words, languages = loadDBRels()
	cargarRelaciones(True, True, True, True, True, True, True, True)
	while True:
		idiomaPadre = 'afr'
		padre = 'bees'
		idiomaHijo = 'nld'
		hija = 'beest'
		print(padre, hija, 'bees', 'beest')
		print("Prueba función es hija: ", __esHija(idiomaPadre, padre, idiomaHijo, hija))
		print("Prueba función es hija: ", __esHija(idiomaHijo, hija, idiomaPadre, padre))

		apartheid = 'apartheid'
		aviation = 'aviation'
		aviarius = 'aviarius'
		aviarium = 'aviarium'
		avis = 'avis'
		print("Prueba función son hermanas: ", __sonHermanos('fra', apartheid, 'ita', apartheid))  # true
		print("Prueba función son hermanas: ", __sonHermanos('fra', apartheid, 'afr', apartheid))  # false
		print("Prueba función son hermanas: ", __sonHermanos('afr', apartheid, 'afr', apartheid))  # false
		print("Prueba función son hermanas: ", __sonHermanos('fra', aviation, 'lat', aviarius))  # true

		print("Hijos idioma: ", __hijosDeUnIdioma('sco'))  # true

		print("Prueba función son primas: ", __sonPrimas('eng', aviation, 'lat', aviarium))  # true
		print("Prueba función son primas: ", __sonPrimas('fra', aviation, 'lat', aviarium))  # false
		print("Prueba función son primas: ", __sonPrimas('lat', aviarium, 'lat', aviarius))  # false
		print("Prueba función son primas: ", __sonPrimas('lat', aviarium, 'afr', apartheid)) # false

		print("Prueba función grado primas: ", __gradoPrimas('eng', aviation, 'lat', aviarium))
		#print("Prueba función grado primas: ", __gradoPrimas('fra', aviation, 'lat', aviarium))
		#print("Prueba función grado primas: ", __gradoPrimas('lat', aviarium, 'lat', aviarius))
		#print("Prueba función grado primas: ", __gradoPrimas('lat', aviarium, 'afr', apartheid))

		print("Prueba función son tios: ", __esTia('lat', aviarius, 'eng', aviation))  # true
		print("Prueba función son tios: ", __esTia('fra', aviation, 'lat', aviarium))  # true
		print("Prueba función son tios: ", __esTia('eng', aviation, 'lat', aviarius))  # false

		print("Está idioma relacionado palabra: ", __esPalabraRelacionadaIdioma(aviarius, "lat"))
		print("Está idioma relacionado palabra: ", __esPalabraRelacionadaIdioma(aviarius, "fra"))
		print("Está idioma relacionado palabra: ", __esPalabraRelacionadaIdioma(hija, "ita"))

		print("Idiomas relacionados palabra: ", __idiomasRelacionadosPalabra(avis))
		print("Idiomas relacionados palabra: ", __idiomasRelacionadosPalabra(aviarius))

		print("Palabras en un idioma originadas por una palabra específica: ", __palabrasEnUnIdiomaOriginadasPorPalabra(avis, "lat"))
		print("Palabras en un idioma originadas por una palabra específica: ", __palabrasEnUnIdiomaOriginadasPorPalabra(avis, "fra"))

		print("Listar palabras comunes dos idiomas: ", __listarPalabrasComunesIdiomas("ita", "lat"))
		print("Listar palabras comunes dos idiomas: ", __listarPalabrasComunesIdiomas("eng", "lat"))
		print("Listar palabras comunes dos idiomas: ", __listarPalabrasComunesIdiomas("afr", "lat"))

		print("Contar palabras comunes dos idiomas: ", __numeroPalabrasComunesIdiomas("ita", "fra"))
		print("Contar palabras comunes dos idiomas: ", __numeroPalabrasComunesIdiomas("eng", "lat"))
		break
		time.sleep(10)

#-lat: avis
#  -lat: aviarius
#    -lat: aviarium
#  -fra: aviation
#    -eng: aviation


main()
