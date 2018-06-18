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
create_terms('contarPalabrasComunes, C1, _getHijos')
create_terms("lPalabrasIdiomaOriginadas, getHijosIdioma,Palabra ,Idioma,Hijos, getHijosI, hijosIdioma, getPrimas, X, Y ")
create_terms('_getPadreMostrar,getPalabrasXidioma, palabrasComunes, I1, I2, IA, IB, IP1, IP2, IPP1, IPP2, IT, IS, sonElMismo, O, numeroPalabrasComunes, _hijosDeUnIdioma, __hijosDeUnIdioma')
create_terms('IP1, IP2, _getHijo, IH1, IH2, contribucionXidiomaMin,idiomaPadre, rContPalabras,cPalabras,contPalabras,prueba9,prueba10, prueba7,prueba8, contaPalabras,nPalabrasXidioma2,numTotalPalabras, contadorPalabras,getIdiomaPadre3,nPalabrasXidioma,contribucionXidioma, N2, numPalabras,prueba4, prueba44,prueba3,prueba33,porcentajes2, getIdiomaPadre2,S,N,Z,sumarPalabrasXidioma,totalPalabras,nTotalPalabras,porcentajes,numTotalPalabras,numPalabrasIdioma, prueba2, Y,contarPadres, prueba, IH, Res, Total, consultaPrincipal, getListaIdiomas, getContarPalabrasXidioma, getContarPalabrasXidioma, palabrasDeIdioma')

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

sonElMismo(IH1, IH2, A, B, R) <= (IH1 == IH2) & (A == B)

#------ Es hijo
esHijo(H, P) <= esHijo(IP, P, IH, H)
esHijo(H, P, R) <= esHijo(IP, P, IH, H) & ~sonElMismo(IP, IH, P, H, X)

_getHijo(IP, P, IH, H) <= esHijo(IP, P, IH, H)


sonHermanos(A, B, R) <= _getHijo(IP1, P1, IH1, A) & _getHijo (IP2, P2, IH2, B) & (sonElMismo(P1, P2, IP1, IP2, R3))  & ~(sonElMismo(IH1, IH2, A, B, R2) )
sonHermanos(A, B) <= sonHermanos(A, B, R)
#------ Determinar si dos palabras son prim@s y también se obtiene el grado
sonPrimos(P1, P2, G, True) <= sonPrimos(P1, P2, G )
sonPrimos(P1, P2, 0, False) <= ~sonPrimos(P1, P2, G)
sonPrimos(P1, P2, G) <= esHijo(P1, PP1) & esHijo(P2, PP2) & sonHermanos(PP1, PP2) & (G==1)
sonPrimos(P1, P2, G) <= esHijo(P1, PP1) & esHijo(P2, PP2) & ~sonHermanos(PP1, PP2) & sonPrimos(PP1, PP2, G1) & (G==G1+1)
sonPrimas(P1, P2) <= sonPrimos(P1, P2, G)

#------- Determina si dos palabras son primas, y el grado
gradoPrimos(P1, P2, G) <= sonPrimos(P1, P2, G)

#------- Determinar si una palabra es tía de otra
esTio(T, S, R) <= esHijo(S, P) & sonHermanos(T, P) & (P!=T)
getPadre(H, I)<=esHijo(IP, P, IH, H)

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
_estaRelacionada(P, IH, R) <= _antepasados(P, I,R) & (I==IH)
_estaRelacionada(P, IH, True) <= _estaRelacionada(P, IH, R)
_estaRelacionada(P, IH, False) <= ~_estaRelacionada(P, IH, R)

#-----------  Listar todas las palabras comunes entre dos idiomas
create_terms('getPalabrasXidioma, palabrasComunes, I1, I2')
getPalabrasXidioma(I, R) <= esHijo(IP, P, I, R)
getPalabrasXidioma(I, R) <= esHijo(I, R, IH, H)
palabrasComunes(I1, I2, R1) <= getPalabrasXidioma(I1, R1) & getPalabrasXidioma(I2, R2) & (R1==R2)

#----------- Número de palabras comunes entre dos idiomas
(numeroPalabrasComunes[I1, I2]==len_(R1)) <= palabrasComunes(I1, I2, R1)
contarPalabrasComunes(I1, I2, R1) <= (R1==[numeroPalabrasComunes[I1, I2]])

#------------------------------------- Idiomas que contribuyeron con otros -------------------
create_terms('mayorContribucion,__mayorContribucion, conPalabras,__contadorPalabras')
rContPalabras(IH, R) <= (R==contPalabras[IH])
(contPalabras[IH]==sum_(T, for_each=IP)) <= (T==nPalabrasXidioma2[IH, IP])
(nPalabrasXidioma2[IH, IP]==running_sum_(T, group_by=IP, order_by=P))  <= getIdiomaPadre2(IH, IP, P, T)
getIdiomaPadre2(IH, IP, P, T) <= esHijo(IP, P, IH, H) & (IP!=IH) &(T==1)
(nPalabrasXidioma[IH, IP]==running_sum_(N2, group_by=IP, order_by=P))  <= getIdiomaPadre2(IH, IP, P, T) & (rContPalabras(IH, N) ) & (N2==100/N)
contribucionXidioma(IH, IP, T) <=  (T==nPalabrasXidioma[IH, IP])
(mayorContribucion[IH]==max_(IP, order_by=T))<= (contribucionXidioma(IH, IP, T))
__mayorContribucion(IH, T) <=  (T==mayorContribucion[IH])
#---------------------------------------------------------------



def readFileWord(respuesta):
	tmp = respuesta.split('w')
	linea = int(tmp[1])
	izq = True if tmp[2] == '1' else False
	global DATABASE
	with open(DATABASE,encoding="utf-8") as f:
		for i, line in enumerate(f):
			if i == linea:
				if izq:
					return line.split('\t')[0]
				else:
					return line.split('\t')[2].split('\n')[0]

def __sonHermanos(_nombreA, _nombreB):
	# Determinar si dos palabras son heman@s
	if (ask('sonHermanos('+_nombreA+','+ _nombreB+ ', R)')):
		return "Son hermanas"
	else:
		return "No son hermanas"

def __sonPrimas(_nombreA, _nombreB):
	# Determinar si dos palabras son prim@s
	if(ask('sonPrimas('+_nombreA+','+ _nombreB+')')):
		return "Son primas"
	else:
		return "No son primas"

def __gradoPrimas(_nombreA, _nombreB):
	# Determina si son primas y en qué grado
	consulta = ask('gradoPrimos('+_nombreA+','+ _nombreB+ ', R)')
	if (consulta):
		return "Son primas", consulta.answers[0][0]
	else:
		return "No son primas", 0

def __esHija(_hijo, _padre):
	# Determinar si una palabra es hij@ de otra
	if (ask('esHijo('+_hijo+','+ _padre+ ', R)')):
		return "Sí es hija"
	else:
		return "No es hija"

def __esTia(_tio, _sobrino):
	# Determinar si una palabra es tí@
	if (ask('esTio('+_tio+','+ _sobrino+ ', R)')):
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
	#Obtener el conjunto de todas las palabras en un idioma originadas por una palabra específica
	consulta = ask('hijosIdioma('+_palabra+','+ _idioma+ ', R)')
	if (consulta):
		words = []
		for r in consulta.answers:
			words.append(r[0])
			words.append(readFileWord(r[0]))
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
			words.append(readFileWord(r[0]))
		return words
	else:
		return "No hubo coincidencia."


def __numeroPalabrasComunesIdiomas(_idiomaA, _idiomaB):
	# Contar todas las palabras comunes entre dos idiomas
	consulta = ask('contarPalabrasComunes('+_idiomaA+', '+_idiomaB+', R1)')
	if (consulta):
		return consulta.answers[0][0][0]
	else:
		return 0


def __idiomaMasAporto(_idioma):
	# Idioma que más aportó a otro (e.g. latín a español). Medir basado en porcentaje
	consulta = ask('__mayorContribucion('+_idioma+', R1)')
	if (consulta):
		return consulta.answers[0][0]
	else:
		return "Ninguno"

def __listarIdiomasAportaronOtro(_idioma):
	# LIstar todos los idiomas que aportaron a otro. Similar al anterior pero debe incluir porcentaje para todos los idiomas
	consulta = ask('contribucionXidioma('+_idioma+', R1, R2)')
	if (consulta):
		return consulta.answers
	else:
		return "Ninguno"




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
	with open(DATABASE, encoding="utf-8") as f:
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
				words[wordLft] = 'w'+str(i)+'w1'

			try:
				u = words[wordRgt]
				saved += 1
			except KeyError:
				words[wordRgt] = 'w'+str(i)+'w2'

			#if wordLft == 'beest' or wordRgt == 'beest' or wordLft == 'apartheid' or wordRgt == 'apartheid':
			#	print("beep:", (str(langLftIdx), hash(words[wordLft]), str(langRgtIdx), hash(words[wordRgt])), rel)
			if(rel == 'rel:derived'):
				+ derived(langLft, words[wordLft], langRgt, words[wordRgt])
			elif(rel == 'rel:etymologically'):
				+ etymologically(langLft, words[wordLft], langRgt, words[wordRgt])
			elif(rel == 'rel:etymologically_related'):
				+ etymologically_related(langLft, words[wordLft], langRgt, words[wordRgt])
			elif(rel == 'rel:etymology'):
				+ etymology(langLft, words[wordLft], langRgt, words[wordRgt])
			elif(rel == 'rel:etymological_origin_of'):
				+ etymology(langRgt, words[wordRgt], langLft, words[wordLft])
			elif(rel == 'rel:has_derived_form'):
				+ has_derived_form(langLft, words[wordLft], langRgt, words[wordRgt])
			elif(rel == 'rel:is_derived_from'):
				+ has_derived_form(langRgt, words[wordRgt], langLft, words[wordLft])
			elif(rel.find('rel:variant') > -1):
				+ variant(langLft, words[wordLft], langRgt, words[wordRgt])

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
	if (etymological_origin_of):
		esHijo(IP, P, IH, H) <= etymology(IH, H, IP, P)
	else:
		pyEngine.retract(esHijo(IP, P, IH, H) <= etymology(IP, P, IH, H))
	if (_has_derived_form):
		esHijo(IP, P, IH, H) <= has_derived_form(IP, P, IH, H)
	else:
		pyEngine.retract(esHijo(IP, P, IH, H) <= has_derived_form(IP, P, IH, H))
	if (is_derived_from):
		esHijo(IP, P, IH, H) <= has_derived_form(IH, H, IP, P)
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
		idiomaHijo = 'nld'
		padre = words['bees']
		hija = words['beest']
		#print(padre, hija, 'bees', 'beest')
		print("Prueba función es hija: ", __esHija(padre,  hija))
		print("Prueba función es hija: ", __esHija(hija, padre))

		apartheid = words['apartheid']
		aviation = words['aviation']
		aviarius = words['aviarius']
		aviarium = words['aviarium']
		avis = words['avis']
		#print("Prueba función son hermanas: ", __sonHermanos(apartheid, apartheid))  # true
		#print("Prueba función son hermanas: ", __sonHermanos(apartheid,  apartheid))  # false
		aviations = words['aviations']
		aviationIncident = words['aviation incident']
		print("Prueba función son hermanas: ", __sonHermanos(aviations,  aviationIncident))  # false
		print("Prueba función son hermanas: ", __sonHermanos( words['anxsumnes'],  words['fear']))  # true
		print("Prueba función son hermanas: ", __sonHermanos( words['benn'],  words['hrop']))  # false
		print("Prueba función son hermanas: ", __sonHermanos( words['angsum'],  words['swinc']))  # true

		# TEST: palabrasDeIdioma(I, H) <= esHijo(I, H, IP, P)
		# TEST: palabrasDeIdioma(I, P) <= esHijo(IH, H, I, P)
		# TEST: resultados = []
		# TEST: consulta = ask('palabrasDeIdioma(ita,R)')
		# TEST: for r in consulta.answers:
		# TEST: 	resultados.append(readFileWord(r[0]))
		# TEST: 	#words.append(readFileWord(r[0]))
		# TEST: print("sencillo:", resultados)

		print("Prueba función son primas: ", __sonPrimas(aviation, aviarium))  # true
		print("Prueba función son primas: ", __sonPrimas( aviation, aviarium))  # false
		print("Prueba función son primas: ", __sonPrimas(aviarium,  aviarius))  # false
		print("Prueba función son primas: ", __sonPrimas( aviarium, apartheid)) # false
		print("Prueba función son primas: ", __sonPrimas( words['synder'],words['separately'])) # true

		#print("Prueba función grado primas: ", __gradoPrimas( aviation, aviarium))
		#print("Prueba función grado primas: ", __gradoPrimas( aviation, aviarium))
		#print("Prueba función grado primas: ", __gradoPrimas(aviarium, aviarius))
		#print("Prueba función grado primas: ", __gradoPrimas( aviarium, apartheid))

		print("Prueba función son tios: ", __esTia( aviarius, aviation))  # true
		print("Prueba función son tios: ", __esTia(aviation, aviarium))  # true
		print("Prueba función son tios: ", __esTia( aviation,  aviarius))  # false
		print("Prueba función son tios: ", __esTia( words['sunder'],  words['synder']))  # true
		print("Prueba función son tios: ", __esTia( words['syndrian'],  words['synder']))  # false

		#print("Está idioma relacionado palabra: ", __esPalabraRelacionadaIdioma(aviarius, "lat"))
		#print("Está idioma relacionado palabra: ", __esPalabraRelacionadaIdioma(aviarius, "fra"))
		#print("Está idioma relacionado palabra: ", __esPalabraRelacionadaIdioma(hija, "ita"))

		#print("Idiomas relacionados palabra: ", __idiomasRelacionadosPalabra(avis))
		#print("Idiomas relacionados palabra: ", __idiomasRelacionadosPalabra(aviarius))

		#print("Palabras en un idioma originadas por una palabra específica: ", __palabrasEnUnIdiomaOriginadasPorPalabra(avis, "lat"))
		#print("Palabras en un idioma originadas por una palabra específica: ", __palabrasEnUnIdiomaOriginadasPorPalabra(avis, "fra"))

		#print("Listar palabras comunes dos idiomas: ", __listarPalabrasComunesIdiomas("ita", "lat"))
		#print("Listar palabras comunes dos idiomas: ", __listarPalabrasComunesIdiomas("eng", "lat"))
		#print("Listar palabras comunes dos idiomas: ", __listarPalabrasComunesIdiomas("afr", "lat"))

		#print("Contar palabras comunes dos idiomas: ", __numeroPalabrasComunesIdiomas("ita", "fra"))
		#print("Contar palabras comunes dos idiomas: ", __numeroPalabrasComunesIdiomas("eng", "lat"))
		break
		time.sleep(10)

#-lat: avis
#  -lat: aviarius
#    -lat: aviarium
#  -fra: aviation
#    -eng: aviation

#words, languages = loadDBRels()
#cargarRelaciones(True, True, True, True, True, True, True, True)
#print("Prueba función son hermanas: ", __sonHermanos( words['anxsumnes'],  words['fear']))  # true
#main()

#lis = ['ita: buon giorno', 'ita: se non che', 'ita: 3000 siepi', 'ita: musulmana', 'ita: gatto mammone', 'ita: chicchirichí', 'ita: capodoglio', 'ita: socioculturale', 'ita: melamina', 'ita: romanzo-verità', 'cor: gol', 'ita: scioccare', 'ita: casa barca', 'ita: 5000 metri', 'ita: dimenticato da dio', 'ita: suoneria', 'ita: artificio', 'ita: reimbarcarsi', 'ita: remunerare', 'ita: recuperare', 'ita: ohibò', 'ita: ricomprare', 'ita: bentornato', 'ita: apostrofo', 'ita: socioeconomico', 'ita: formaggiera', 'ita: post-produzione', 'ita: quantomeno', 'ita: pro capite', 'ita: gioco', 'ita: rinuncia', 'ita: dispotismo', 'ita: pakistana', 'eng: capoc', 'ita: Consiglio di Sicurezza', 'cat: psicoanalista', 'ita: in giù', 'ita: pressappoco', 'ita: mulinaro', 'ita: jugoslavo', 'ita: ninnananna', 'ita: newyorkese', 'ita: conoscere', 'ita: quantomeccanico', 'ita: Consiglio di Sicurezza delle Nazioni Unite', 'ita: postdatare', 'ita: giocare', 'ita: caffè latte', 'ita: avantieri', 'ita: chilowattora', 'ita: reputare', 'ita: putacaso', 'ita: mucoso', 'ita: schermitore', 'ita: buddistico', 'ita: beneducato', 'ita: sociosanitario', 'ita: reincarnarsi', "ita: d'accordo", 'ita: proferire', "ita: mo'", 'ita: effigie', 'ita: 10000 metri', 'ita: messaggio e-mail', 'ita: italoamericano', 'ita: catalessi', 'ita: cardellino', 'ita: orecchio', 'ita: gattamorta', 'ita: otto volante', 'ita: districarsi', 'ita: dimagrimento', 'ita: reincarnare', 'ita: psicoanalitico', 'ita: constatare', 'ita: zolfatara', 'ita: mela cotogna', 'ita: zolfara', 'ita: caftano', 'ita: su per giù', 'ita: TV-verità', 'ita: diciannove', 'ita: districare', 'ita: di sopra', 'ita: presepe', 'ita: ormone follicolo-stimolante', 'ita: batticuore', 'ita: medievale', 'ita: cyberspazio', 'ita: ricominciare', 'ita: quartultimo', 'ita: cosiddetto', 'ita: resuscitare', 'ita: pallamano', 'ita: magrebino', 'ita: terraferma', 'ita: passe-partout', 'ita: pallacanestro', 'ces: lobbista', 'ita: uh', 'ita: pallavolo', 'ita: Jugoslavia', 'ita: psicoanaliticamente', 'ita: keniano', 'ita: di sotto', 'ita: benvisto', 'ita: resurrezione', 'ita: reputarsi', 'ita: borragine', 'ita: afghano', 'ita: patriottico', 'ita: casereccio', 'ita: carta musica', 'ita: sottocchio', 'ita: a capo', 'ita: sottotono', 'ita: katiuscia', 'ita: gastroesofageo', 'ita: afroamericano', 'ita: viceallenatore', 'ita: reinvestire', 'ita: edificio', 'ita: di andata', 'ita: 1500 metri', 'ita: specie-specificità', 'ita: sopracciliare', 'ita: deflattivo', 'ita: urogenitale', 'ita: rincuorare', 'ita: cripto', 'ita: acqua santa', 'ita: annerirsi', 'ita: compiere', 'ita: buddista', 'ita: allerta', 'ita: abbrustolire', 'ita: stacanovismo', 'ita: latinoamericano', 'ast: comprare', 'ita: pesce gatto', 'ita: barcaiolo', "ita: di buon'ora", 'ita: bennato', 'ita: sparviere', 'ita: risuolare', 'ita: beninteso', 'ita: benintenzionato', 'ita: bendisposto', 'ita: perbene', 'ita: autogol', 'ita: viticoltore', 'ita: eucaristia', 'ita: pianterreno', 'cat: patriota', 'ita: fisionomia', 'ita: bestiola', 'ita: dopo che', 'ita: conditio sine qua non', 'ita: denuncia', 'ita: paraguaiano', 'ita: lazzarone', 'ita: ricompiere', 'ita: pallanuoto', 'ita: disuguale', 'ita: lecca-lecca', 'ita: Thailandia', 'ita: barberia', 'ita: né', 'ita: acquaiolo', 'ita: uruguaiano', 'ita: sovrappiù', 'ita: reimpiegare', 'ita: uguagliare', 'ita: benpensante', 'ita: viticoltura', 'ita: restringersi', 'ita: codesto', 'ita: buddismo', 'ita: eclissi solare', 'ita: benvenuto', 'ita: ammodo', 'ita: fai da te', 'ita: annerire', 'ita: denunciare', 'ita: keniota', 'ita: acquacoltore', 'ita: eclissi lunare', 'ita: casomai', 'ita: dispotico', 'ita: rincuorarsi', 'ita: rinunciare', 'ita: musulmano', 'ita: risuonare', 'ita: terzultimo', "ita: lista d'attesa", 'ita: benfatto', 'ita: zombi', 'ita: sisma', 'ita: acquacoltura', 'ita: fior di latte', 'ita: eclissi', 'ita: due pezzi', 'ita: tariffa', 'ita: giraffa', 'ita: borgomastro', 'ita: carciofo', 'ita: giubba', 'eng: Sofia', 'ita: meschino', 'fra: chitarra', 'fin: föhn', 'ita: mamelucco', 'ita: marzacotto', 'ita: feluca', 'ita: tazza', 'ita: ussaro', 'lat: tara', 'ita: fango', 'ita: rais', 'ita: berta', 'ita: gabella', 'ita: scacco', 'ita: zecca', 'ita: albicocca', 'ita: avaria', 'ita: melanzana', 'afr: apartheid', 'ita: scacco matto', 'ita: risma', 'ita: limone', 'ita: alcool', 'ita: mocaiaro', 'ita: birra', 'ita: carato', 'ita: magazzino', 'ita: concerto', 'dan: piccolo', 'ita: smalto', 'ita: fagotto', 'deu: Annina', 'ita: castagna', 'ita: brutus', 'ita: sonetto', 'ita: damasco', 'ita: Caesaraugusta', 'ita: fascismo', 'ita: pagliaccio', 'cat: pizza', 'ita: cassa', 'ita: caligotte', 'ita: napolitano', 'cat: caricatura', 'ita: brigata', 'ita: concertina', 'ita: battuta', 'ita: frittella', 'ita: contrabbando', 'dan: tempo', 'cat: ocarina', 'ita: palanca', 'ita: basso', 'ita: fascista', 'ita: clavicembalo', 'ita: grotta', 'enm: do', 'dan: giro', 'ita: cavolfiore', 'ita: Inghilterra', 'dan: lasagne', 'ita: broccolo', 'dan: finale', 'ita: sicuro', 'dan: Rita', 'ita: custode', 'ita: caravana', 'ita: pomodoro', 'ita: diva', 'cat: piano', 'ita: ciglione', 'ita: sdrùcciolo', 'ita: marzapane', 'ita: bastione', 'ita: alto', 'ces: firma', 'ita: fortepiano', 'ita: espresso', 'ita: viola da bracchio', 'ita: bastia', 'ita: balcone', 'dan: mafioso', 'ita: violino', 'ita: plastilina', 'ita: disegnare', 'ita: freccia', 'crh: lava', 'ita: zucchino', 'ita: altana', 'pro: cavalier', 'ita: ciarlatano', 'ita: manco', 'ita: agresto', 'cat: extra-', 'ita: carnevale', 'ita: granata', 'ita: fioretto', 'ita: trampolino', 'ita: capriccio', 'cat: violinista', 'ita: ghetto', 'ang: net', 'dan: malaria', 'ita: isolare', 'crh: regata', 'cat: intra-', 'dan: grave', 'ita: dilettante', 'ita: mostaccio', 'ita: caraffa', 'ita: capo', 'ita: sonata', 'ita: fregata', 'ita: amaretto', 'ita: miniatura', 'ita: salsiccia', 'ita: balletto', 'dan: furore', 'ita: aria', 'ita: gondola', 'cat: zero', 'dan: ambra', 'ita: razza', 'ita: ambiente', 'ita: buongiorno', 'ita: sennonché', 'ita: 3.000 siepi', 'ita: mussulmana', 'ita: gattomammone', 'ita: chicchirichì', 'ita: capidoglio', 'ita: socio-culturale', 'ita: melammina', 'ita: romanzo verità', 'eng: goal', 'ita: choccare', 'ita: casa-barca', 'ita: 5.000 metri', 'ita: dimenticato da Dio', 'ita: soneria', 'ita: artifizio', 'ita: rimbarcarsi', 'ita: rimunerare', 'ita: ricuperare', 'ita: oibò', 'ita: ricomperare', 'ita: ben tornato', 'ita: apostrofe', 'ita: socio-economico', 'ita: formaggera', 'ita: post produzione', 'ita: quanto meno', 'ita: pro-capite', 'ita: giuoco', 'ita: rinunzia', 'ita: despotismo', 'ita: pachistana', 'ita: capok', 'ita: Consiglio di sicurezza', 'ita: psicanalista', 'ita: ingiù', 'ita: pressapoco', 'ita: molinaro', 'ita: iugoslavo', 'ita: shoccare', 'ita: ninna nanna', 'ita: newyorchese', 'lat: cognoscere', 'ita: quanto-meccanico', 'ita: Consiglio di sicurezza delle Nazioni Unite', 'ita: posdatare', 'ita: giuocare', 'ita: caffellatte', "ita: avant'ieri", 'ita: chilovattora', 'ita: riputare', 'ita: puta caso', 'ita: muccoso', 'ita: schermidore', 'ita: buddhistico', 'ita: bene educato', 'ita: socio-sanitario', 'ita: rincarnarsi', 'ita: daccordo', 'ita: profferire', 'ita: mo', 'ita: effige', 'ita: 10.000 metri', 'ita: messaggio email', 'ita: italo-americano', 'ita: catalessia', 'ita: cardinalino', 'ita: orecchia', 'ita: gatta morta', 'ita: ottovolante', 'ita: distrigarsi', 'ita: dimagramento', 'ita: rincarnare', 'ita: psicanalitico', 'ita: costatare', 'cat: solfatara', 'ita: melacotogna', 'ita: solfara', 'ita: kaftano', 'ita: suppergiù', 'ita: TV verità', 'ita: dici nove', 'ita: distrigare', 'ita: disopra', 'ita: presepio', 'ita: ormone follicolo stimolante', 'ita: batticore', 'ita: medioevale', 'ita: ciberspazio', 'ita: rincominciare', "ita: quart'ultimo", 'ita: così detto', 'ita: risuscitare', 'ita: palla a mano', 'ita: maghrebino', 'ita: terra ferma', 'ita: passepartout', 'ita: palla a canestro', 'ita: lobbysta', 'ita: uhu', 'ita: palla a volo', 'ita: postproduzione', 'ita: Iugoslavia', 'ita: psicanaliticamente', 'ita: kenyano', 'ita: disotto', 'ita: ben visto', 'ita: risurrezione', 'ita: riputarsi', 'ita: borraggine', 'ita: afgano', 'ita: patriotico', 'ita: casareccio', 'ita: cartamusica', "ita: sott'occhio", 'ita: accapo', 'ita: sotto tono', 'ita: katiusha', 'ita: gastro-esofageo', 'ita: afro-americano', 'ita: vice allenatore', 'ita: rinvestire', 'ita: edifizio', "ita: d'andata", 'ita: 1.500 metri', 'ita: vice-allenatore', 'ita: specie specificità', 'ita: sopraccigliare', 'ita: deflativo', 'ita: uro-genitale', 'ita: rincorare', 'ita: krypto', 'ita: acquasanta', 'ita: annerarsi', 'ita: compire', 'ces: buddhista', "ita: all'erta", 'ita: abbrustolare', 'ita: stakanovismo', 'ita: latino-americano', 'ita: comperare', 'ita: pescegatto', 'ita: barcarolo', 'ita: di buonora', 'ita: ben nato', 'ita: sparviero', 'ita: risolare', 'ita: ben inteso', 'ita: ben intenzionato', 'ita: ben disposto', 'ita: per bene', 'ita: autogoal', 'ita: viticultore', 'ita: eucarestia', 'ita: pian terreno', 'ita: patriotta', 'ita: fisonomia', 'ita: bestiuola', 'ita: dopoché', 'ita: condicio sine qua non', 'ita: denunzia', 'ita: paraguayano', 'ita: lazzerone', 'ita: ricompire', 'ita: barcaiuolo', 'ita: palla a nuoto', 'ita: diseguale', 'ita: leccalecca', 'ita: Tailandia', 'ita: barbieria', 'ita: nè', 'ita: acquaiuolo', 'ita: uruguayano', 'ita: soprappiù', 'ita: rimpiegare', 'ita: eguagliare', 'ita: ben pensante', 'ita: viticultura', 'ita: ristringersi', 'ita: cotesto', 'ita: buddhismo', 'ita: kripto', 'ita: eclisse solare', 'ita: ben venuto', 'ita: a modo', 'ita: fai-da-te', 'ita: annerare', 'ita: denunziare', 'ita: kenyota', 'ita: acquicoltore', 'ita: eclisse lunare', 'ita: caso mai', 'ita: lecca lecca', 'ita: despotico', 'ita: rincorarsi', 'ita: rinunziare', 'ita: mussulmano', 'ita: risonare', 'ita: sopraciliare', "ita: terz'ultimo", 'ita: lista di attesa', 'ita: ben fatto', 'ita: zombie', 'ita: sismo', 'ita: acquicoltura', 'ita: fiordilatte', 'ita: eclisse', 'ita: duepezzi']
#nope = 0
#for i in lis:
#	if i[0:5] != 'ita: ':
#		nope += 1
#		print(i)
#print(len(lis), nope)
