# Proyecto 2: Relaciones de Etimología

*** Curso: *** Inteligencia Artificial

***Tecnológico de Costa Rica***
## Autores

* **Marcello Ávila Feoli** - *Desarrollador*
* **Stefi Falcón Chávez** - *Desarrollador*
* **Nelson Gómez Alvarado** - *Desarrollador*

## Introducción
La lógica representa un papel básico en la informática y en campos como la Inteligencia Artificial, específicamente en la creación de agentes basados en lógica. De aquí se deriva también la lógica de primer orden, que por medio de un conjunto de predicados y cuantificadores se pueden realizar inferencias.

Por otra parte, la etimología es un campo que estudia el origen de las palabras, debido a que muchos idiomas actuales tienen interrelaciones basadas en raíces comunes.
A partir de los conceptos anteriormente mencionados, se presenta el proyecto a realizar, el cual básicamente tiene como intención exponer el procesamiento de datos mediante un motor de derivación lógico.

Para realizar el proyecto, se utilizará un lenguaje de lógica sobre el lenguaje de programación Python, llamado PyDatalog, y una base de datos de relaciones etimológicas proveniente de “Etymological Wordnet”, que recopila relaciones entre palabras de distintos idiomas.

La idea principalmente es que se pueda construir un sistema basado en proposiciones lógicas que nos permita responder preguntas relacionadas al origen común de las palabras, similitud de los lenguajes, etc.  


## Instalación

El lenguaje de derivación utilizado será PyDatalog, el cual consiste en una librería que permite solucionar problemas de lógica utilizando el paradigma de programación lógico.
Dicha librería requiere una instalación, cuyos pasos serán mencionados a continuación.

* El primer requisito es tener instalado Python 3.6. Si el sistema operativo es Windows, se puede descargar el ejecutable por medio de la siguiente dirección:
```
    https://www.python.org/downloads/
```
* Para realizar su instalación en Linux, utilizar el siguiente comando, en la terminal:
```
pip install pyDatalog
```
* Para realizar la instalación de este segundo proyecto programado, del curso Inteligencia Artificial, primero deberá de descargar el archivo tec-0.1.zip; y posteriormente, deberá de ejecutar, en línea de comandos, la instrucción que se especifica a continuación:
```
pip install tec-0.1.zip -t <directorio>
```
* Descargar la base de datos Etymological Wordnet y colocarla en la carpeta raíz:
```
https://cs.rutgers.edu/~gd343/downloads/etymwn-20130208.zip
```

### Manual de usuario
# FALTA: poner capturas de pantalla para cada operación


### Detalles de implementación y diseño

#### Interfaz gráfica
Para la implementación de la interfaz de usuario, se utilizó TkInter que es un estándar para la interfaz gráfica de un usuario para Python.

#### Manejo de los datos
La base de datos a manipular contiene el siguiente formato:

```
idioma: palabra tipoRelación idioma: palabra
```
A continuación se muestra un ejemplo del formato escrito:
```
eng: war rel:has_derived_form eng: war crime
```


Donde, eng representa el idioma inglés; war representa la palabra guerra; rel:has_derived_form, representa el el tipo de relación entre esas dos palabras; y crime, significa la palabra que se encuentra relacionada con la primera mencionada.

Además existen ocho tipos distintos de relaciones para las palabras las cuales son:

1. rel:derived     
2. rel:etymologically
3. rel:etymologically_related
4. rel:etymological_origin_of
5. rel:etymology
6. rel:has_derived_form
7. rel:is_derived_from
8. rel:variant:orthography

Dónde se descubre que las relaciones rel:etymological_origin_of y
rel:etymology, son simétricas. Esto debido a que ambas relaciones tienen la misma cantidad de hechos, en el archivo inspeccionado. Para ser exactos: 473433 hechos.

El mismo caso sucede con las relaciones has_derived_form y is_derived_from.

Así, para realizar la carga de datos y hechos en la base de conocimiento se tomaron las siguientes decisiones:

* FALTA

#### Consultas

Las consultas son realizadas a partir de la función ask de pyDatalog.
```
ask(query)
```


Dónde query es un string que contiene un una consulta lógica, dicha función puede devolver dos tipos de valores: pyDatalog.Answer o None.


#### Análisis del resultados


#### Distribución del trabajo




## Licencia

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Referencias
* Programa Estado de La Nación (2018). Distribución de juntas receptoras de votos. Recuperado de https://www.estadonacion.or.cr/files/biblioteca_virtual/otras_publicaciones/IndicadoresCantonales_Censos2000y011.xlsx

* Tribunal Supremo de Elecciones República de Costa Rica (2018). 2018 Elecciones Nacionales, Resultados Provinciales. Recuperado de http://resultados2018.tse.go.cr/resultados/#/presidenciales

* Tribunal Supremo de Elecciones República de Costa Rica (2018). 2018 Elecciones Nacionales, Actas de escrutinio. Recuperado de http://www.tse.go.cr/elecciones2018/actas_escrutinio.htm

* Tribunal Supremo de Elecciones República de Costa Rica (2018). Distribución de juntas receptoras de votos. Recuperado de http://www.tse.go.cr/pdf/nacional2018/JRV.pdf
