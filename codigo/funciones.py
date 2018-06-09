from pyDatalog import pyDatalog
pyDatalog.create_terms('padre, X,Y,Z,N,N1,F,  factorial, first_remainder, odd,even, _split')

datos =[["senabe", "sannup"], ["waniigan","wangan"], ["waniigan","wannigan"]]

#---- Parentesco
def sonPrimas(a, b):
	# Devuelve el grado
	pass


def esHermano(_hermanoA, _hermanoB):
	if (pyDatalog.ask('padre(X,'+_hermanoA+')')==pyDatalog.ask('padre(X,'+_hermanoB+')')):
		print(_hermanoA +" es herman@ de  "+ _hermanoB)
	else:
		print(_hermanoA +" NO es herman@ de  "+ _hermanoB)


def esHijo(_padre, _hijo):
	consulta = pyDatalog.ask('padre(X,'+_hijo+')')
	if (consulta.answers[0][0]==_padre):
		print(_hijo +" es hij@ de  "+ _padre)
	else:
		print(_hijo +" NO es hij@ de  "+ _padre)

def esTio(_tio, _sobrino):
	padreSobrino = pyDatalog.ask('padre(X,'+_sobrino+')').answers[0][0]
	if (pyDatalog.ask('padre(X,'+_tio+')')==pyDatalog.ask('padre(X,'+padreSobrino+')')):
		print(_tio +" es tí@ de  "+ _sobrino)
	else:
		print(_tio +" NO es tí@ de  "+ _sobrino)

def esPrimo(_primoA, _primoB):
	padrePrimoA = pyDatalog.ask('padre(X,'+_primoA+')').answers[0][0]
	padrePrimoB = pyDatalog.ask('padre(X,'+_primoB+')').answers[0][0]
	if (pyDatalog.ask('padre(X,'+padrePrimoA+')')==pyDatalog.ask('padre(X,'+padrePrimoB+')')):
		print(_primoA +" es prim@ de  "+ _primoB)
	else:
		print(_primoA +" NO es prim@ de  "+ _primoB)


def esHijo2(_padre, _hijo):
	consulta = pyDatalog.ask('padre(X,'+_hijo+')')
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
	#pyDatalog.load("""
	#	(factorial[N] == F) <= (N < 2) & (F==1)
	#	(factorial[N] == F) <= (N > 1) & (N1 == N-1) & (F == N*factorial[N1])
	#""")
	#print(pyDatalog.ask('factorial[3]==N')) # prints a set with one element: (3,6)
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
	pyDatalog.assert_fact('padre', 'A','B') 
	pyDatalog.assert_fact('padre', 'A','F') 
	pyDatalog.assert_fact('padre', 'A','X') 
	pyDatalog.assert_fact('padre', 'A','Z') 
	pyDatalog.assert_fact('padre', 'B','D') 
	pyDatalog.assert_fact('padre', 'B','C') 
	pyDatalog.assert_fact('padre', 'F','G') 
	pyDatalog.assert_fact('padre', 'C','P') 	
	pyDatalog.assert_fact('padre', 'O','D')	


def main():
	alimentarBD()
	esHijo("B","D")
	esHijo2("B","D")
	esHermano("B", "C")
	esTio("F","C")
	esPrimo("G","D")


main()
