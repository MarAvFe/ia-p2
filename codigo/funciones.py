import logging
from pyDatalog import pyEngine
from pyDatalog.pyDatalog import assert_fact, load, create_terms, ask
create_terms('padre, X,Y,Z,N,N1,F,  factorial, first_remainder, odd,even, _split, algo, algo2')

#pyEngine.Logging = True
#logging.basicConfig(level=logging.INFO)
datos =[["senabe", "sannup"], ["waniigan","wangan"], ["waniigan","wannigan"]]

#---- Parentesco
def sonPrimas(a, b):
	# Devuelve el grado
	pass



def esHermano(_hermanoA, _hermanoB):
	if (ask('padre(X,'+_hermanoA+')')==ask('padre(X,'+_hermanoB+')')):
		print(_hermanoA +" es herman@ de  "+ _hermanoB)
	else:
		print(_hermanoA +" NO es herman@ de  "+ _hermanoB)


def esHermanoNew(_hermanoA, _hermanoB):
	# funciona, pero es por ser puro python.
	a1 = ask("parent("+str(_hermanoA)+",X)")
	a2 = ask("parent("+str(_hermanoB)+",X)")
	flag = False
	for h in a1.answers:
		if h in a2.answers:
			flag = True
	if (flag):
		print(_hermanoA +" es herman@ de  "+ _hermanoB)
	else:
		print(_hermanoA +" NO es herman@ de  "+ _hermanoB)


def esHijo(_padre, _hijo):
	consulta = ask('padre(X,'+_hijo+')')
	if (consulta.answers[0][0]==_padre):
		print(_hijo +" es hij@ de  "+ _padre)
	else:
		print(_hijo +" NO es hij@ de  "+ _padre)

def esTio(_tio, _sobrino):
	padreSobrino = ask('padre(X,'+_sobrino+')').answers[0][0]
	if (ask('padre(X,'+_tio+')')==ask('padre(X,'+padreSobrino+')')):
		print(_tio +" es tí@ de  "+ _sobrino)
	else:
		print(_tio +" NO es tí@ de  "+ _sobrino)

def esPrimo(_primoA, _primoB):
	padrePrimoA = ask('padre(X,'+_primoA+')').answers[0][0]
	padrePrimoB = ask('padre(X,'+_primoB+')').answers[0][0]
	if (ask('padre(X,'+padrePrimoA+')')==ask('padre(X,'+padrePrimoB+')')):
		print(_primoA +" es prim@ de  "+ _primoB)
	else:
		print(_primoA +" NO es prim@ de  "+ _primoB)


def esHijo2(_padre, _hijo):
	consulta = ask('padre(X,'+_hijo+')')
	if (consulta.answers[0][0]==_padre):
		print(_hijo +" es hij@ de  "+ _padre)
	else:
		print(_hijo +" NO es hij@ de  "+ _padre)



# -- Operaciones entre palabra e idioma
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
	# Idioma que más aportó a otro
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
	db = []
	words = {}
	numWords = 0
	with open("../etymwn/etymwn.tsv") as f:
		i = 0
		for l in f:
			tmp = l.split("\t")
			lft = tmp[0]
			rgt = tmp[2]
			lftIdx = numWords
			if lft in words:
				continue
			else:
				words[lft] = (i,1)
			if rgt in words:
				continue
			else:
				words[rgt] = (i,2)
			assert_fact(tmp[1],words[lft],words[rgt])

			#if(l.find("rel:has_derived_form") != -1) or (l.find("rel:etymological_origin_of") != -1):
			#if(l.find("rel:etymology") == -1):
			#	continue
			#db.append(l)  #crearRelacion(l)
			i += 1
			if i%10000==0:
				print(i)
			#if i>300000:
			#	break
		print("dbSize:",i)
		print(words["eng: chickenpox"])
		while True:
			pass

loadDBRels()

def alimentarBD():
	assert_fact('padre', 'A','B')
	assert_fact('padre', 'A','F')
	assert_fact('padre', 'A','X')
	assert_fact('padre', 'A','Z')
	assert_fact('padre', 'B','D')
	assert_fact('padre', 'B','C')
	assert_fact('padre', 'F','G')
	assert_fact('padre', 'C','P')
	assert_fact('padre', 'O','D')

	assert_fact('parent', 'mike','bob')
	assert_fact('parent', 'mike2','bob')
	assert_fact('parent', 'brian','mike')
	assert_fact('parent', 'luke','mike')
	assert_fact('parent', 'john','mike')
	assert_fact('parent', 'tom','brian')
	assert_fact('parent', 'marty','tom')
	assert_fact('parent', 'bill','john')
	assert_fact('parent', 'brian2','mike2')
	assert_fact('parent', 'luke2','mike2')
	assert_fact('parent', 'john2','mike2')
	assert_fact('parent', 'tom2','brian2')
	assert_fact('parent', 'bill2','john2')
	assert_fact('parent', 'mike3','bob3')
	assert_fact('parent', 'roy3','bob3')
	# bob
	#  -mike
	#    -brian
	#      -tom
	#        -marty
	#    -luke
	#    -john
	#      -bill
	#  -mike2
	#    -brian2
	#      -tom2
	#    -luke2
	#    -john2
	#      -bill2
	#
	# bob3
	#   -mike3
	#   -roy3
	load("""
		brother(X,Y) <= parent(X,Z) & parent(Y,Z) & (X!=Y)
		uncle(X,Y) <= parent(Y,Z) & brother(X,Z)
		ancestor(X,Y) <= parent(X,Y)
		ancestor(X,Y) <= parent(X,Z) & ancestor(Z,Y)
		cousin(X,Y) <= parent(X,Z) & parent(Y,W) & brother(Z,W)
		cousin2(X,Y) <= cousin(X,W) & parent(Y,W)
		start(X,Y) <= (Y==X[0:2])
		related(X,Y) <= ancestor(X,P) & ancestor(Y,Q) & (P==Q)

		parentRel(X,Y) <= etymology(X,Y)
		parentRel(X,Y) <= etymology(X,Z) & parentRel(Z,Y)

		""")
		#parentRel(X,Y) <= is_derived_from(X,Y)
		#parentRel(X,Y) <= is_derived_from(X,Z) & parentRel(Z,Y)
	# el start muestra cómo editar la salida o comparación.
	# por ejemplo cuando agreguemos 'eng: doubt', podríamos comparar los idiomas con este método con Y==[:5]

	# el related está más o menos. inestable, tal vez

def main():
	alimentarBD()
	esHijo("B","D")
	esHijo2("B","D")
	esHermano("B", "C")
	esTio("F","C")
	esPrimo("G","D")

	print('parent bill:',ask('parent(bill,X)'))
	print('ancestor bill:',ask('ancestor(bill,X)')) # john, mike, bob
	print('uncle brian:',ask('uncle(brian,X)'))  # bill
	print('brother john:',ask('brother(john,X)'))  # luke, brian
	print('cousin bill:',ask('cousin(bill,X)'))  # tom
	print('cousin luke:',ask('cousin(luke,X)'))  # luke2, brian2, john2
	print('cousin2 luke:',ask('cousin2(luke,X)'))  # bill2, tom2
	print('cousin2 bill:',ask('cousin2(bill,X)'))  # marty
	print('start:',ask('start(bill,X)'))
	print('related:',ask('related(bill,X)'))
	print('related:',ask('related(mike3,X)'))
	esHermanoNew('bill','john')
	esHermanoNew('luke','john')
	print('related:',ask('parentRel(Japan,X)'))

main()

#definicion lógica externa
algo(X,Y) <= (Y=="Beep")
print(algo("doot",X))
