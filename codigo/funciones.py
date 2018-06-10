from pyDatalog.pyDatalog import assert_fact, load, create_terms, ask
create_terms('padre, X,Y,Z,N,N1,F,  factorial, first_remainder, odd,even, _split')

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
		""")
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

main()
