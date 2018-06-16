
from pyDatalog import pyDatalog
from pyDatalog.pyDatalog import assert_fact, load, create_terms, ask

pyDatalog.create_terms("esHijo, getPadre, etymology,etymological_origin_of,has_derived_form,is_derived_from, H, P, IH,IP,R, H1")
create_terms('I,getHijos2, descendientes,gradoPrimos, sonPrimas, lIdiomasRpalabra, D1,D2,D3,D4, D5, D6, ID, LI, LA, PAL,PAD, _PADRES, _IDIOMAS, derived, etymologically, etymologically_related, etymology, has_derived_form, variant, esHijo, sonHermanos,antepasados, esTio, sonPrimos, A, B, P1,P2, T, S, PP1, PP2, G1,G')
create_terms('getHijos2,resultado,_estaRelacionada, _soloIdiomas,getIdiomas, H1, getHijos2,R_IP, R_P,R_IH, R_H, R2, descendientes,getPadres2, ascendencia,_antepasados,A,B,C,D,E,F,GR1,R1, R2,R3')
create_terms('getHijos2,resultado,_estaRelacionada, _soloIdiomas,getIdiomas, H1, getHijos2,R_IP, R_P,R_IH, R_H, R2, descendientes,getPadres2, ascendencia,_antepasados,A,B,C,D,E,F,GR1,R1, R2,R3')
pyDatalog.create_terms("lPalabrasIdiomaOriginadas, getHijosIdioma,Palabra ,Idioma,Hijos, getHijosI, hijosIdioma ")
create_terms('contarPalabrasComunes, C1')

+ etymologically("nada", "luis","nada", "catalina")
+ derived("aaa", "alejandra","aaa", "margarita")
+ derived("aaa", "alejandra","aaa", "teresa")
+ derived("aaa", "alejandra","fff", "jose")
+ derived("fff", "jose","www", "julio")
+ derived("aaa", "margarita","aaa", "david")
+ derived("aaXa", "papa de marta","aaa", "marta")
+ derived("aaa", "david","aaXa", "daniel")
+ derived("aaa", "alejandra","aaa", "catalina")
+ derived("b", "marta","idiomaHija", "alejandra")
+ etymologically("nada", "emilia","nada", "adriana")
+ etymologically_related("nada", "alejandra","nada", "catalina")
+ etymologically_related("nada", "helena","nada", "emilia")
+ etymology("nada", "luis", "nada", "diego")
+ etymology("nada", "erick", "nada", "ericka")
+ etymologically_related("nada", "marta", "nada", "erick")
+ has_derived_form("nada", "luis", "nada", "carlos")
+ has_derived_form("nada", "adriana", "nada", "saul")
+ has_derived_form("nada", "enrique", "bbb", "catalina")
+ has_derived_form("nada", "juan", "bbb", "enrique")
+ variant("nada", "alejandra","nada", "catalina")
+ variant("c", "helena","b", "marta")
+ variant("nada", "luis","nada", "catalina")

esHijo(IP, P, IH, H) <= derived(IP, P, IH, H)
esHijo(IP, P, IH, H) <= etymologically(IP, P, IH, H)
esHijo(IP, P, IH, H) <= etymologically_related(IP, P, IH, H)
esHijo(IP, P, IH, H) <= etymology(IP, P, IH, H)
esHijo(IP, P, IH, H) <= has_derived_form(IP, P, IH, H)
esHijo(IP, P, IH, H) <= variant(IP, P, IH, H)
#esHijo(H, P) <= etymology(IH, H, IP, P)	#etymological_origin_of
#esHijo(H, P) <= has_derived_form(IH, H, IP, P) #is_derived_from

#------ Es hijo
esHijo(H, P) <= esHijo(IP, P, IH, H)
esHijo(H, P, R) <= esHijo(A, P, B, H)

# ----- Determinar si dos palabras son heman@s
sonHermanos(A, B, R) <= esHijo(A, P) & esHijo (B, P) & (A!=B)
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

def __idiomaMasAporto(_idioma):
	# Idioma que más aportó a otro (e.g. latín a español). Medir basado en porcentaje
	pass

def __listarIdiomasAportaronOtro():
	# LIstar todos los idiomas que aportaron a otro. Similar al anterior pero debe incluir porcentaje para todos los idiomas
	pass

def main():
	print("Prueba función son hermanos: ", __sonHermanos("catalina", "margarita"))
	print("Prueba función son hermanos: ", __sonHermanos("saul", "margarita"))
	print("Prueba función son PRIMOS: ", __sonPrimas("catalina", "ericka")) #True
	print("Prueba función son PRIMOS: ", __sonPrimas("saul", "margarita")) #True
	print("Prueba función son PRIMOS: ", __sonPrimas("alejandra", "maria")) #False
	print("Prueba función son PRIMOS: ", __gradoPrimas("catalina", "ericka"))
	print("Prueba función son PRIMOS: ", __gradoPrimas("saul", "margarita"))
	print("Prueba función son PRIMOS: ", __gradoPrimas("alejandra", "maria"))
	print("Prueba función son HIJA: ", __esHija("david", "margarita"))
	print("Prueba función son HIJA: ", __esHija("mariaeee", "catalina"))
	print("Prueba función es TÍA: ", __esTia("alejandra", "ericka"))
	print("Prueba función ES TÍA: ", __esTia("mariaeee", "catalina"))
	print("Está idioma relacionado palabra: ", __esPalabraRelacionadaIdioma("alejandra", "nada"))
	print("Está idioma relacionado palabra: ", __esPalabraRelacionadaIdioma("alejandra", "asdoij"))
	print("Idiomas relacionados palabra: ", __idiomasRelacionadosPalabra("alejandradd"))
	print("Idiomas relacionados palabra: ", __idiomasRelacionadosPalabra("alejandra"))
	print("Palabras en un idioma originadas por una palabra específica: ", __palabrasEnUnIdiomaOriginadasPorPalabra("alejandra", "aaa"))
	print("Palabras en un idioma originadas por una palabra específica: ", __palabrasEnUnIdiomaOriginadasPorPalabra("alejandra", "asdrf"))
	print("Listar palabras comunes dos idiomas: ", __listarPalabrasComunesIdiomas("nada", "aaa"))
	print("Listar palabras comunes dos idiomas: ", __listarPalabrasComunesIdiomas("alejandra", "asdrf"))
	print("Contar palabras comunes dos idiomas: ", __numeroPalabrasComunesIdiomas("nada", "aaa"))
	print("Contar palabras comunes dos idiomas: ", __numeroPalabrasComunesIdiomas("alejandra", "asdrf"))
	print("primas de alejandra: ", ask('sonPrimas("alejandra",Y)'))
	print("primas de catalina: ", ask('sonPrimas("catalina",Y)'))

main()
