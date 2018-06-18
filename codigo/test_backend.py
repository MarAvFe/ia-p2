from backend3 import *
from pyDatalog import pyEngine, Logic
from pyDatalog.pyDatalog import assert_fact, load, create_terms, ask
create_terms("esHijo, etymology,IH,H,IP,P")

#- juan
#  - mario
#    - carlos
#	 - oscar
#  - alberto
#    - maria
#	 - susana
#  - darío

esHijo(IP, P, IH, H) <= etymology(IH, H, IP, P)
+ etymology('esp', 'juan', 'esp', 'mario')
+ etymology('esp', 'juan', 'esp', 'alberto')
+ etymology('esp', 'juan', 'esp', 'dario')
+ etymology('esp', 'mario', 'esp', 'carlos')
+ etymology('esp', 'mario', 'esp', 'oscar')
+ etymology('esp', 'alberto', 'esp', 'maria')
+ etymology('esp', 'alberto', 'esp', 'susana')
+ etymology('ita', 'alberta', 'esp', 'alberto')
+ etymology('ita', 'alberta', 'esp', 'alberta')



def test___sonHermanos():
	assert __sonHermanos('alberto', 'mario') == "Son hermanas"
	assert __sonHermanos('alberto', 'susana') == "No son hermanas"
	pass

def test___sonPrimas():
	assert __sonPrimas('maria', 'oscar') == "Son primas"
	assert __sonPrimas('maria', 'susana') == "Son primas"
	pass

def test___gradoPrimas():
	assert __gradoPrimas('maria', 'oscar') == 1
	pass

def test___esHija():
	assert __esHija('mario', 'juan') == True
	pass

def test___esTia():
	assert __esTia('alberto', 'oscar') == "Sí es tía"
	assert __esTia('alberto', 'darío') == "No es tía"
	pass

def test___esPalabraRelacionadaIdioma():
	assert __esPalabraRelacionadaIdioma('maria', 'esp') == "Sí está relacionada"
	assert __esPalabraRelacionadaIdioma('maria', 'ita') == "Sí está relacionada"
	pass

def test___palabrasEnUnIdiomaOriginadasPorPalabra():
	assert type(__palabrasEnUnIdiomaOriginadasPorPalabra('juan', 'esp')) == list
	pass

def test___idiomasRelacionadosPalabra():
	assert __idiomasRelacionadosPalabra("maria") == ['esp']
	pass

def test___listarPalabrasComunesIdiomas():
	assert __listarPalabrasComunesIdiomas('ita', 'esp') == ['alberto']
	pass

def test___numeroPalabrasComunesIdiomas():
	assert __numeroPalabrasComunesIdiomas('ita', 'esp') == 1
	pass

#def test___idiomaMasAporto():
#	assert __idiomaMasAporto(param1, param2) == True
#	pass
#
#def test___listarIdiomasAportaronOtro():
#	assert __listarIdiomasAportaronOtro(param1, param2) == True
#	pass
#
#def test___hijosDeUnIdioma():
#	assert __hijosDeUnIdioma(param1, param2) == True
#	pass
