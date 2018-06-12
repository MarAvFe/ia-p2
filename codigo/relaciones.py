
from pyDatalog import pyDatalog
from pyDatalog.pyDatalog import assert_fact, load, create_terms, ask

pyDatalog.create_terms("esHijo, etymology,etymological_origin_of,has_derived_form,is_derived_from, H, P, IH,IP,R")
create_terms('derived, etymologically, etymologically_related, etymology, has_derived_form, variant, esHijo, sonHermanos, esTio, sonPrimos, A, B, P1,P2, T, S, PP1, PP2, G1,G')


+ derived("nada", "alejandra","nada", "catalina")
+ derived("nada", "marta","nada", "alejandra")
+ etymologically("nada", "alejandra","nada", "catalina")
+ etymologically("nada", "emilia","nada", "adriana")
+ etymologically_related("nada", "alejandra","nada", "catalina")
+ etymologically_related("nada", "erminda","nada", "emilia")
+ etymology("nada", "luis", "nada", "diego")
+ etymology("nada", "erick", "nada", "ericka")
+ etymologically_related("nada", "marta", "nada", "erick")
+ has_derived_form("nada", "luis", "nada", "carlos")
+ has_derived_form("nada", "adriana", "nada", "saul")
+ variant("nada", "alejandra","nada", "catalina")
+ variant("nada", "erminda","nada", "marta")
+ variant("nada", "luis","nada", "catalina")

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


def cargarRelaciones(_derived, _etymologically, _etymologically_related, _etymology, _has_derived_form, _variant, etymological_origin_of, is_derived_from):
	if (_derived):
		esHijo(H, P) <= derived(IP, P, IH, H)
	else:
		-esHijo(H, P) <= derived(IP, P, IH, H)
	if (_etymologically):
		esHijo(H, P) <= etymologically(IP, P, IH, H)
	else:
		-esHijo(H, P) <= etymologically(IP, P, IH, H)
	if (_etymologically_related):
		esHijo(H, P) <= etymologically_related(IP, P, IH, H)
	else:
		-esHijo(H, P) <= etymologically_related(IP, P, IH, H)
	if (_etymology):
		esHijo(H, P) <= etymology(IP, P, IH, H)
	else:
		-esHijo(H, P) <= etymology(IP, P, IH, H)
	if (_has_derived_form):
		esHijo(H, P) <= has_derived_form(IP, P, IH, H)
	else:
		-esHijo(H, P) <= has_derived_form(IP, P, IH, H)
	if (_variant):
		esHijo(H, P) <= variant(IP, P, IH, H)
	else:
		-esHijo(H, P) <= variant(IP, P, IH, H)
	if (etymological_origin_of):
		esHijo(H, P) <= etymology(IH, H, IP, P)	#etymological_origin_of
	else:
		-esHijo(H, P) <= etymology(IH, H, IP, P)	#etymological_origin_of
	if (is_derived_from):
		esHijo(H, P) <= has_derived_form(IH, H, IP, P) #is_derived_from
	else:
		-esHijo(H, P) <= has_derived_form(IH, H, IP, P) #is_derived_from






def main():
	cargarRelaciones(True, True, True, True, True, True, True, True)
	print(ask('esHijo(diego, luis, R)').answers[0][0])
	print("Son Hermanos: ",ask('sonHermanos(catalina, luis, R)').answers[0][0])
	print("Son Hermanos: ",ask('sonHermanos(carlos, catalina, R)').answers[0][0])
	print("Es tio ",ask('esTio(erick, catalina, R)').answers[0][0])
	print("Es tio ",ask('esTio(catalina, erick, R)').answers[0][0])
	print("Son primos ",ask('sonPrimos(catalina, ericka,G, R)'))
	print("Son primos ",ask('sonPrimos(catalina, saul,G, R)'))
	print("Son primos ",ask('sonPrimos(carlos, saul,G,  R)'))
main()		


	



