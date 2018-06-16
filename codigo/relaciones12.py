
from pyDatalog import pyDatalog
from pyDatalog.pyDatalog import assert_fact, load, create_terms, ask

pyDatalog.create_terms("esHijo, getPadre, etymology,etymological_origin_of,has_derived_form,is_derived_from, H, P, IH,IP,R, H1")
create_terms('I,getHijos2, descendientes,gradoPrimos, sonPrimas, lIdiomasRpalabra, D1,D2,D3,D4, D5, D6, ID, LI, LA, PAL,PAD, _PADRES, _IDIOMAS, derived, etymologically, etymologically_related, etymology, has_derived_form, variant, esHijo, sonHermanos,antepasados, esTio, sonPrimos, A, B, P1,P2, T, S, PP1, PP2, G1,G')
create_terms('getHijos2,resultado,_estaRelacionada, _soloIdiomas,getIdiomas, H1, getHijos2,R_IP, R_P,R_IH, R_H, R2, descendientes,getPadres2, ascendencia,_antepasados,A,B,C,D,E,F,GR1,R1, R2,R3')
create_terms('getHijos2,resultado,_estaRelacionada, _soloIdiomas,getIdiomas, H1, getHijos2,R_IP, R_P,R_IH, R_H, R2, descendientes,getPadres2, ascendencia,_antepasados,A,B,C,D,E,F,GR1,R1, R2,R3')
pyDatalog.create_terms("lPalabrasIdiomaOriginadas, getHijosIdioma,Palabra ,Idioma,Hijos, getHijosI, hijosIdioma ")
create_terms('contarPalabrasComunes,getIdiomaPadre, C1, numeroPalabrasComunes, __contadorPalabras')

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


+ variant("fra", "we", "esp", "asda")
+ variant("lat", "werx", "esp", "asda")
+ variant("fra", "sdfwe", "esp", "sdfh")
+ variant("fra", "fds", "esp", "vxcv")
+ variant("fra", "fsd", "esp", "xcvwe")
+ variant("lat", "fw", "esp", "wer")
+ variant("ing", "fsw", "esp", "qwer")
+ variant("fra", "fwewf", "esp", "rty")
+ variant("lat", "erwerqw", "esp", "oiu")
+ variant("fra", "sdf", "esp", "dfsq")
+ variant("ale", "erwerqw", "esp", "oiaaau")
+ variant("ale", "sdf", "esp", "dfqsq")
# hechos:10
# fra: 6
# lat: 3
# ing: 1

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
sonHermanos(A, B, R) <= esHijo(A, P1) & esHijo (B, P2) & (P1 == P2) & (A!=B)
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


create_terms('contribucionXidiomaMin,rContPalabras,cPalabras,contPalabras,prueba9,prueba10, prueba7,prueba8, contaPalabras,nPalabrasXidioma2,numTotalPalabras, contadorPalabras,getIdiomaPadre3,nPalabrasXidioma,contribucionXidioma, N2, numPalabras,prueba4, prueba44,prueba3,prueba33,porcentajes2, getIdiomaPadre2,S,N,Z,sumarPalabrasXidioma,totalPalabras,nTotalPalabras,porcentajes,numTotalPalabras,numPalabrasIdioma, prueba2, Y,contarPadres, prueba, IH, Res, Total, consultaPrincipal, getListaIdiomas,getContarPalabrasXidioma,getContarPalabrasXidioma')

#------------------------------------- Idiomas que contribuyeron con otros -------------------
create_terms('mayorContribucion,__mayorContribucion, conPalabras,__contadorPalabras, _hijosDeUnIdioma')
rContPalabras(IH, R) <= (R==contPalabras[IH])
(contPalabras[IH]==sum_(T, for_each=IP)) <= (T==nPalabrasXidioma2[IH, IP])
(nPalabrasXidioma2[IH, IP]==running_sum_(T, group_by=IP, order_by=P))  <= getIdiomaPadre2(IH, IP, P, T)
getIdiomaPadre2(IH, IP, P, T) <= esHijo(IP, P, IH, H) & (IP!=IH) &(T==1)
(nPalabrasXidioma[IH, IP]==running_sum_(N2, group_by=IP, order_by=P))  <= getIdiomaPadre2(IH, IP, P, T) & (rContPalabras(IH, N) ) & (N2==100/N)
contribucionXidioma(IH, IP, T) <=  (T==nPalabrasXidioma[IH, IP])
(mayorContribucion[IH]==max_(IP, order_by=T))<= (contribucionXidioma(IH, IP, T))
__mayorContribucion(IH, T) <=  (T==mayorContribucion[IH])
#---------------------------------------------------------------
_hijosDeUnIdioma(IP) <= esHijo(IP,P,IH,H)


# ----------
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
	consulta = ask('palabrasComunes('+_idiomaA+', '+_idiomaB+', R1)')
	if (consulta):
		return consulta.answers
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


def main():
	#print("Prueba función son hermanos: ", __sonHermanos("catalina", "margarita"))
	#print("Prueba función son hermanos: ", __sonHermanos("saul", "margarita"))
	#print("Prueba función son PRIMOS: ", __sonPrimas("catalina", "ericka"))
	#print("Prueba función son PRIMOS: ", __sonPrimas("saul", "margarita"))
	#print("Prueba función son PRIMOS: ", __sonPrimas("alejandra", "maria"))
	#print("Prueba función son PRIMOS: ", __gradoPrimas("catalina", "ericka"))
	#print("Prueba función son PRIMOS: ", __gradoPrimas("saul", "margarita"))
	#print("Prueba función son PRIMOS: ", __gradoPrimas("alejandra", "maria"))
	#print("Prueba función son HIJA: ", __esHija("david", "margarita"))
	#print("Prueba función son HIJA: ", __esHija("mariaeee", "catalina"))
	#print("Prueba función es TÍA: ", __esTia("alejandra", "ericka"))
	#print("Prueba función ES TÍA: ", __esTia("mariaeee", "catalina"))
	#print("Está idioma relacionado palabra: ", __esPalabraRelacionadaIdioma("alejandra", "nada"))
	#print("Está idioma relacionado palabra: ", __esPalabraRelacionadaIdioma("alejandra", "asdoij"))
	#print("Idiomas relacionados palabra: ", __idiomasRelacionadosPalabra("alejandradd"))
	#print("Idiomas relacionados palabra: ", __idiomasRelacionadosPalabra("alejandra"))
	#print("Palabras en un idioma originadas por una palabra específica: ", __palabrasEnUnIdiomaOriginadasPorPalabra("alejandra", "aaa"))
	#print("Palabras en un idioma originadas por una palabra específica: ", __palabrasEnUnIdiomaOriginadasPorPalabra("alejandra", "asdrf"))
	#print("Listar palabras comunes dos idiomas: ", __listarPalabrasComunesIdiomas("nada", "aaa"))
	#print("Listar palabras comunes dos idiomas: ", __listarPalabrasComunesIdiomas("alejandra", "asdrf"))
	#print("Contar palabras comunes dos idiomas: ", __numeroPalabrasComunesIdiomas("nada", "aaa"))
	#print("Contar palabras comunes dos idiomas: ", __numeroPalabrasComunesIdiomas("alejandra", "asdrf"))
	#(P[IH]==len_(Y)) <= getIdiomaPadre(IH, IP, P)

	#print(P['esp']==IH)
	#print(ask('porcentajes(esp, IP, P, T )'))
	#print(ask('getIdiomaPadre2(esp, IP, P, T) '))
	#print(ask('contribucionXidioma(esp,  IP, T )'))
	#print(ask('prueba44(esp,  IP,T)'))
	#print(ask('rContPalabras(esp,  IP)'))
	#print(ask('contribucionXidioma(esp,  IP, P)'))
	#print(ask('__mayorContribucion(esp,  P)'))
	#print("Idioma que más aportó: ", __idiomaMasAporto('esp'))
	#print("lista idiomas que más aportaron: ",__listarIdiomasAportaronOtro("esp"))
	print(ask('_hijosDeUnIdioma(esp)'))


	#contadorPalabras

	#print(__listarPalabrasComunesIdiomas("aaa", "nada"))
	#print(__numeroPalabrasComunesIdiomas("aaa", "nada"))

main()
