import logging
from pyDatalog import pyEngine
from pyDatalog.pyDatalog import assert_fact, load, create_terms, ask



create_terms('padre, hijo, padre2,X,Y,Z,N,N1,F, relacion4, factorial, first_remainder, odd,even, _split, algo, algo2, relacion, etymologically_related, etymological_origin_of')

pyEngine.Trace = True
#pyEngine.Logging = True
#logging.basicConfig(level=logging.INFO)

datos =[["senabe", "sannup"], ["waniigan","wangan"], ["waniigan","wannigan"]]



# -- Funciones  palabra/idioma
def estaRelacionadaIdioma(palabra, idioma):
	# Sí o no
	pass

def palabrasOriginadas(palabra, idioma):
	# devolver lista de palabras
	#recursiva.
	#1º Buscar todas las hijas de esa palabra, según idioma.
	#Las hijas pasan a ser padres y pasa a buscar a sus hijas (siempre usando el filtro del idioma)
	#load("""
	#	(factorial[N] == F) <= (N < 2) & (F==1)
	#	(factorial[N] == F) <= (N > 1) & (N1 == N-1) & (F == N*factorial[N1])
	#""")
	#print(ask('factorial[3]==N')) # prints a set with one element: (3,6)
	pass

def listarIdiomasRelacionados(palabra):
	pass

# -- Comparación idiomas

def contarPalabrasComunes(idiomaA, idiomaB):
	# Contar todas las palabras comunes entre dos idiomas
	pass

def listarPalabrasComunes (idiomaA, idiomaB):
	# Listar todas las palabras comunes entre dos idiomas
	pass

def idiomaMasAporto (idiomaA, idiomaB):
	# Idioma que más aportó a otro
	pass

def listaIdiomasAportaron (idioma):
	# LIstar todos los idiomas que aportaron a otro.
	#Similar al anterior pero debe incluir porcentaje para todos los idiomas
	pass



def crearRelacion(linea):
	# swe: bio-	rel:etymological_origin_of	swe: biologi
	tmp = linea.split("\t")  # ["swe: bio-","rel:etymological_origin_of","swe: biologi"]
	izq = tmp[0]  # swe: bio-
	rel = tmp[1].split(":")[1]  # rel:etymological_origin_of
	der = tmp[2].split("\n")[0]  # swe: biologi
	assert_fact(rel, izq, der)

def loadDBRels():
	with open("etymwn.tsv") as f:
		i = 0
		for l in f:
			#if(l.find("rel:has_derived_form") != -1) or (l.find("rel:etymological_origin_of") != -1):
			if(l.find("rel:etymology") == -1):
				continue
			crearRelacion(l)
			i += 1
			if i%100000==0:
				print(i)
			if i>300000:
				break
		print("dbSize:",i)

#loadDBRels()

def cargarDatos():
	borrar=[]
	derived=""
	etymologically=""
	etymologically_related="" 
	etymological_origin_of=""
	etymology=""
	has_derived_form=""
	is_derived_from=""
	variant=""
	with open("etymwn.tsv") as f:
		i = 0
		for l in f:
			#if(l.find("rel:has_derived_form") != -1) or (l.find("rel:etymological_origin_of") != -1):
			tmp = l.split("\t")  # ["swe: bio-","rel:etymological_origin_of","swe: biologi"]
			
			if (tmp[1].split(":")[1]!= 'etymology' or tmp[1].split(":")[1]!= 'is_derived_from'):
				izqIdioma = tmp[0].split(":")[0] 

				izqPalabra = tmp[0].split(":")[1]
				izqPalabra = izqPalabra[1:]
				relacion = tmp[1].split(":")[1]  # rel:etymological_origin_of
				derIdioma = tmp[2].split(":")[0] # swe: biologi
				derPalabra = tmp[2].split(":")[1]
				derPalabra = derPalabra.split("\n")[0] 
				derPalabra = derPalabra[1:]
				izqPalabra = izqPalabra.replace("'", "")
				derPalabra = derPalabra.replace("'", "")
				#borrar=[izqIdioma, izqPalabra, relacion, derIdioma, derPalabra]
				#hecho = 'assert_fact(padre,'+izqIdioma+','+izqPalabra+','+derIdioma+','+derPalabra+')      '
				hechoPH = "+padre('"+izqIdioma+"','"+izqPalabra+"','"+derIdioma+"','"+derPalabra+"')\n"
				hechoHP = "+padre('"+derIdioma+"','"+derPalabra+"','"+izqIdioma+"','"+izqPalabra+"')\n"
			#	hecho = '+padre('+izqIdioma+','+izqPalabra+','+derIdioma+','+derPalabra+')\n'
				if (relacion=='derived'):
					derived+=hechoPH
				elif (relacion=='etymologically'):
					etymologically+=hechoPH
				elif (relacion=='etymologically_related'):
					etymologically_related+=hechoHP
				elif (relacion=='etymological_origin_of'):
					etymological_origin_of+=hechoPH
					etymology+=hechoHP
				elif (relacion=='has_derived_form'):
					has_derived_form+=hechoPH
					is_derived_from+=hechoHP
				elif (relacion=='variant'):
					variant+=hechoHP
		return 	[derived ,etymologically, etymologically_related, etymological_origin_of, etymology, has_derived_form, is_derived_from, variant]
			#assert_fact(rel, izq, der)

		#relacion(idiomaHijo, hijo, idiomaPadre, padre)

def cargarHechos(bd, vRelaciones):
	hechos=""
	for i in vRelaciones:
		hechos+=bd[i]

	#load(hechos)
	#print("cargar: derived")
	#load(bd[0])
	#print("cargar: etymologically")
	#load(bd[1])
	#print("cargar: etymologically_related")
	#load(bd[2])
	#print("cargar: etymological_origin_of")
	#load(bd[3])
	#print("cargar: etymology")
	#load(bd[4])
	#print("cargar: has_derived_form")
	#load(bd[5])
	#print("cargar: is_derived_from")
	#load(bd[6])
#	print("cargar: variant")
#	load(bd[7])
	print ("**** fin cargar hechos ")


def alimentarBD():

	load("""

		hijo2(P,H,R) <= padre(X,I,X2,H) & (I==P)

		hermano(X, Y, H) <= padre(Z, X) & padre (Z,Y) & (X!=Y)
		hijo(X, Y, H) <= padre(Z,Y) & (X==Z)
		tio(T, S, H) <= padre(P, S) & hermano(P, T, A) & (P!=T) 
		primo(X,Y,R) <= padre(Q,X) & padre(Z,Y) & (Q!=Y) & hermano(Q,Z,R)

		primoGrado(X,Y,H) <= padre(P,X) & padre(A,Y) & hermano(A,P,H) 
		primoGrado(X,Y,R) <= padre(P,X) & padre(A,Y)  & hermano(P, A, Q) &primoGrado(A,P,H)
		""")
#------------- Funciones de relaciones palabra con palabra --
def _sonHermanos(_A, _B):
	if (ask('hermano('+_A+','+_B+', Z)') != None):
		return True
	else:
		return False

def _esHijo(_hijo, _padre):
	if (ask('hijo('+_padre+','+_hijo+', Z)') != None):
		return True
	else:
		return False

def _esTio(_tio, _sobrino):
	if (ask('tio('+_tio+','+_sobrino+', A)') != None):
		return True
	else:
		return False

def main():

	print("********* CARGAR BD ************")
	bd = cargarDatos()
	cargarHechos(bd, [2])
	alimentarBD()
	


	print("************* PRUEBAS  **************")

	#print(ask('hijo2(beampte,amptelijk,R)')) 
main()

#definicion lógica externa
algo(X,Y) <= (Y=="Beep")
print(algo("doot",X))