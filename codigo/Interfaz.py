import tkinter
import logging
from pyDatalog import pyEngine, Logic
from tkinter import *
import tkinter.ttk as TTK
import tkinter.scrolledtext as tkst

import backend3 as bk

#pyEngine.Logging = True
#logging.basicConfig(level=logging.INFO)

pyEngine.Logging = True

try:
    from cStringIO import StringIO      # Python 2
except ImportError:
    from io import StringIO

log_stream = StringIO()    
logging.basicConfig(stream=log_stream,level=logging.INFO)
# logging.info('hello world')
# logging.warning('be careful!')
# logging.debug("you won't see this")
# logging.error('you will see this')
# logging.critical('critical is logged too!')
# print(log_stream.getvalue())



def hello():
    print("Hola mundo")


def printTextos(listaResultado, textPath, varPrint):
    print(varPrint.get())
    if(varPrint.get()==1):
        for i in listaResultado:
            textPath.insert(INSERT,i[33:] + '\n')
    else:
        for i in listaResultado:
            if("esHijo" in i):
                textPath.insert(INSERT,i[33:] + '\n')


def printTextosIdioma(listaResultado, textPath, varPrint):
    print(varPrint.get())
    if(varPrint.get()==1):
        for i in listaResultado:
            textPath.insert(INSERT,i[33:] + '\n')
    else:
        for i in listaResultado:
            if("esHijo" in i):
                #textPath.insert(INSERT,i[33:] + '\n')
                toPrint = i[33:]
                result = []
                for k in toPrint.split("'"):
                    print("k es" + k)
                    if k[0] == 'w' and k[-2] == 'w':
                        print("k en 0 es: " + k[0])
                        print("k en -2 es: " + k[-2])
                        result.append(bk.readFileWord(k))
                        #print("result es: " + result)
                    else:
                        result.append(k)
                toPrint = ''.join(toPrint)
                textPath.insert(INSERT,toPrint + '\n')
    

def var_states(derived,ety,related,origin,etymology,form,rel_from,ortho):
    print(derived.get())
    print(ety.get())
    print(related.get())
    print(origin.get())
    print(etymology.get())
    print(form.get())
    print(rel_from.get())
    print(ortho.get())
    bk.cargarRelaciones(derived.get(),ety.get(),related.get(),origin.get(),etymology.get(),form.get(),rel_from.get(),ortho.get())


def run_query(tipoQuery,entry1,entry2,opcion,textPath,textResult,varPrint):
    textPath.delete('1.0', END)
    textResult.delete('1.0', END)
    print("Dato de text1 es: %s" % entry1.get())
    print("Dato de text2 es: %s" % entry2.get())
    print("El query es %s" % opcion.get())

    letraOpcion = opcion.get()
    string1 = entry1.get()
    string2 = entry2.get()

    if (tipoQuery=="palabra_palabra"):
        print("es del tipo palabra_palabra")
        if(letraOpcion[0]=="A"):
            resultado = bk.__sonHermanos(string1,string2)
            #imprime resultado
            textResult.insert(INSERT,resultado)
            #split al log_stream
            listaResultado = log_stream.getvalue().splitlines()
            #verifica si debe imprimir todo o resumido
            printTextosIdioma(listaResultado,textPath,varPrint)

        elif(letraOpcion[0]=="B"):
            resultado = bk.__sonPrimas(string1,string2)
            #imprime resultado
            textResult.insert(INSERT,resultado)
            #split al log_stream
            listaResultado = log_stream.getvalue().splitlines()
            #verifica si debe imprimir todo o resumido
            printTextos(listaResultado,textPath,varPrint)
            
        elif(letraOpcion[0]=="C"):
            resultado = bk.__esHija(string1,string2)
            #imprime resultado
            textResult.insert(INSERT,resultado)
            #split al log_stream
            listaResultado = log_stream.getvalue().splitlines()
            #verifica si debe imprimir todo o resumido
            printTextos(listaResultado,textPath,varPrint)
        elif(letraOpcion[0]=="D"):
            resultado = bk.__esTia(string1,string2)
            #imprime resultado
            textResult.insert(INSERT,resultado)
            #split al log_stream
            listaResultado = log_stream.getvalue().splitlines()
            #verifica si debe imprimir todo o resumido
            printTextos(listaResultado,textPath,varPrint)
            
        elif(letraOpcion[0]=="E"):
            resultado = bk.__gradoPrimas(string1,string2)
            #imprime resultado
            textResult.insert(INSERT,resultado)
            #split al log_stream
            listaResultado = log_stream.getvalue().splitlines()
            #verifica si debe imprimir todo o resumido
            printTextos(listaResultado,textPath,varPrint)

    if(tipoQuery=="palabra_idioma"):
        print("es del tipo palabra_idioma")
        if(letraOpcion[0]=="A"):
            resultado = bk.__esPalabraRelacionadaIdioma(string1,string2)
            #imprime resultado
            textResult.insert(INSERT,resultado)
            #split al log_stream
            listaResultado = log_stream.getvalue().splitlines()
            #verifica si debe imprimir todo o resumido
            printTextos(listaResultado,textPath,varPrint)
        elif(letraOpcion[0]=="B"):
            resultado = bk.__palabrasEnUnIdiomaOriginadasPorPalabra(string1,string2)
            #imprime resultado
            textResult.insert(INSERT,resultado)
            #split al log_stream
            listaResultado = log_stream.getvalue().splitlines()
            #verifica si debe imprimir todo o resumido
            printTextos(listaResultado,textPath,varPrint)
        elif(letraOpcion[0]=="C"):
            resultado = bk.__idiomasRelacionadosPalabra(string1)
            #imprime resultado
            textResult.insert(INSERT,resultado)
            #split al log_stream
            listaResultado = log_stream.getvalue().splitlines()
            #verifica si debe imprimir todo o resumido
            printTextos(listaResultado,textPath,varPrint)
        
    if(tipoQuery=="idioma_idioma"):
        print("es del tipo idioma_idioma")
        if(letraOpcion[0]=="A"):
            resultado = bk.__numeroPalabrasComunesIdiomas(string1,string2)
            #imprime resultado
            textResult.insert(INSERT,resultado)
            #split al log_stream
            listaResultado = log_stream.getvalue().splitlines()
            #verifica si debe imprimir todo o resumido
            printTextosIdioma(listaResultado,textPath,varPrint)
        elif(letraOpcion[0]=="B"):
            resultado = bk.__listarPalabrasComunesIdiomas(string1,string2)
            #imprime resultado
            for j in resultado:
                textResult.insert(INSERT,j+'\n')
            #split al log_stream
            listaResultado = log_stream.getvalue().splitlines()
            #verifica si debe imprimir todo o resumido
            printTextosIdioma(listaResultado,textPath,varPrint)
        elif(letraOpcion[0]=="C"):
            resultado = bk.__idiomaMasAporto(string1)
            #imprime resultado
            textResult.insert(INSERT,resultado)
            #split al log_stream
            listaResultado = log_stream.getvalue().splitlines()
            #verifica si debe imprimir todo o resumido
            printTextosIdioma(listaResultado,textPath,varPrint)
        elif(letraOpcion[0]=="D"):
            resultado = bk.__listarIdiomasAportaronOtro(string1)
            #imprime resultado
            textResult.insert(INSERT,resultado)
            #split al log_stream
            listaResultado = log_stream.getvalue().splitlines()
            #verifica si debe imprimir todo o resumido
            printTextosIdioma(listaResultado,textPath,varPrint)

def salir():
    root.destroy()


def carga_opciones(root):
    frameCuadro=Frame(root,width=200,height=200 ,bg="cornsilk2")
    frameCuadro.place(x=0,y=0)

    labelRelaciones = Label(frameCuadro, text="1. Relaciones a considerar",width=28,height=2)
    labelRelaciones.place(x=0,y=0)
    
    var_derived = BooleanVar()
    var_ety = BooleanVar()
    var_related = BooleanVar()
    var_origin = BooleanVar()
    var_etymology = BooleanVar()
    var_form = BooleanVar()
    var_from = BooleanVar()
    var_ortho = BooleanVar()
    
    checkBox_derived = Checkbutton(frameCuadro, text="rel:derived", variable=var_derived, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_from,var_ortho))
    checkBox_derived.place(x=30,y=30)
    
    checkBox_ety = Checkbutton(frameCuadro, text="rel:etymologically", variable=var_ety, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_from,var_ortho))
    checkBox_ety.place(x=30,y=50)
    
    checkBox_related = Checkbutton(frameCuadro, text="rel:etymologically_related", variable=var_related, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_from,var_ortho))
    checkBox_related.place(x=30,y=70)
    
    checkBox_origin = Checkbutton(frameCuadro, text="rel:etymological_origin_of", variable=var_origin, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_from,var_ortho))
    checkBox_origin.place(x=30,y=90)
    
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:etymology", variable=var_etymology, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_from,var_ortho))
    checkBox_etymology.place(x=30,y=110)
    
    checkBox_form = Checkbutton(frameCuadro, text="rel:has_derived_form", variable=var_form, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_from,var_ortho))
    checkBox_form.place(x=30,y=130)

    checkBox_from = Checkbutton(frameCuadro, text="rel:has_derived_from", variable=var_from, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_from,var_ortho))
    checkBox_from.place(x=30,y=150)
    
    checkBox_ortho = Checkbutton(frameCuadro, text="rel:variant:orthography", variable=var_ortho, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_from,var_ortho))
    checkBox_ortho.place(x=30,y=170)



def palabra_palabra(root):
    print("Palabra-Palabra")
    #window=tkinter.Tk()
    #window.title("Palabra-Palabra")
    #window.geometry("700x600+100+50")
    #Frames
    frameWigets = Frame(root,width=200,height=400 ,bg="cornsilk2")
    frameWigets.place(x=0,y=200)

    frameTexto = Frame(root,width=980,height=600 ,bg="gray91")
    frameTexto.place(x=200,y=0)
    #Checkbox

    carga_opciones(root)
    
    #Palabra 1
    labelPalabra1 = Label(frameWigets, text="2. Palabra 1",width=28,height=2)
    labelPalabra1.place(x=0,y=10)

    varEntry1 = StringVar()
    entryPalabra1 = Entry(frameWigets,width=20, textvariable=varEntry1)
    entryPalabra1.place(x=30,y=50)

    #Palabra 2
    labelPalabra2 = Label(frameWigets, text="3. Palabra 2", width=28,height=2)
    labelPalabra2.place(x=0,y=80)

    varEntry2 = StringVar()
    entryPalabra2 = Entry(frameWigets,width=20, textvariable=varEntry2)
    entryPalabra2.place(x=30,y=120)

    #menu
    labelPalabra1 = Label(frameWigets, text="4. Determinar si las palabras son:",width=30,height=2)
    labelPalabra1.place(x=0,y=180)


    varCombo = StringVar()
    menuOpciones = TTK.Combobox(frameWigets,values=("A: Hermanas", "B: Primas", "C: Hija 1 de 2","D: Tia 1 de 2","E: Primas con grado"), width=30, textvariable=varCombo)
    menuOpciones.place(x=0,y=240)


    #print Options
    varPrint = IntVar()
    R1 = Radiobutton(frameTexto, text="Todos los detalles de ruta", variable=varPrint, value=1)
    R1.place(x=15,y=0)

    R2 = Radiobutton(frameTexto, text="Ruta resumida", variable=varPrint, value=2)
    R2.select()
    R2.place(x=15,y=30)

    #TextField_path
    textPath=tkst.ScrolledText(frameTexto,width=120,height=21)
    textPath.place(x=0,y=60)

    #TextField_result
    textResult=tkst.ScrolledText(frameTexto,width=120,height=10)
    textResult.place(x=0,y=420)
    
    botonEjecutar=Button(frameWigets,width=28,height=2, text="Ejecutar",bg="dodger blue", command= lambda: run_query("palabra_palabra",varEntry1,varEntry2,varCombo,textPath,textResult,varPrint))
    botonEjecutar.place(x=0,y=300)
    
    root.mainloop()


def palabra_idioma(root):
    print("Palabra-Idioma")
    
    frameWigets = Frame(root,width=200,height=400 ,bg="cornsilk2")
    frameWigets.place(x=0,y=200)

    frameTexto = Frame(root,width=980,height=600 ,bg="gray91")
    frameTexto.place(x=200,y=0)

    carga_opciones(root)
    
    #Palabra 1
    labelPalabra1 = Label(frameWigets, text="2. Palabra",width=28,height=2)
    labelPalabra1.place(x=0,y=10)

    varEntry1 = StringVar()
    entryPalabra1 = Entry(frameWigets,width=20, textvariable=varEntry1 )
    entryPalabra1.place(x=30,y=50)

    #Palabra 2
    idioma = Label(frameWigets, text="3. Idioma(s)", width=28,height=2)
    idioma.place(x=0,y=110)

    varEntry2 = StringVar()
    entryPalabra2 = Entry(frameWigets,width=20,  textvariable=varEntry2 )
    entryPalabra2.place(x=30,y=150)

    #menu
    labelPalabra1 = Label(frameWigets, text="4. Operaciones entre palabra e idioma(s):",width=30,height=2)
    labelPalabra1.place(x=0,y=200)

    varCombo = StringVar()
    menuOpciones = TTK.Combobox(frameWigets,values=("A: 1 Relacionada con 2", "B: Conjunto de todas las palabras en un idioma originadas por la palabra", "C: Listar idiomas relacionados con la palabra"), width=30, textvariable=varCombo)
    menuOpciones.place(x=0,y=240)

    #print Options
    varPrint = IntVar()
    R1 = Radiobutton(frameTexto, text="Todos los detalles de ruta", variable=varPrint, value=1)
    R1.place(x=15,y=0)

    R2 = Radiobutton(frameTexto, text="Ruta resumida", variable=varPrint, value=2)
    R2.select()
    R2.place(x=15,y=30)

    #TextField_path
    textPath=tkst.ScrolledText(frameTexto,width=120,height=21)
    textPath.place(x=0,y=60)

    #TextField_result
    textResult=tkst.ScrolledText(frameTexto,width=120,height=10)
    textResult.place(x=0,y=420)

    botonEjecutar=Button(frameWigets,width=28,height=2, text="Ejecutar",bg="dodger blue", command= lambda: run_query("palabra_idioma",varEntry1,varEntry2,varCombo,textPath,textResult,varPrint))
    botonEjecutar.place(x=0,y=300)
    
    root.mainloop()

def idioma_idioma(root):
    print("Idioma-Idioma")

    frameWigets = Frame(root,width=200,height=400 ,bg="cornsilk2")
    frameWigets.place(x=0,y=200)

    frameTexto = Frame(root,width=980,height=600 ,bg="gray91")
    frameTexto.place(x=200,y=0)

    carga_opciones(root)
    
    #Palabra 1
    labelPalabra1 = Label(frameWigets, text="2. Idioma 1",width=28,height=2)
    labelPalabra1.place(x=0,y=10)

    varEntry1 = StringVar()
    entryPalabra1 = Entry(frameWigets,width=20, textvariable=varEntry1 )
    entryPalabra1.place(x=30,y=50)

    #Palabra 2
    labelPalabra2 = Label(frameWigets, text="3. Idioma 2", width=28,height=2)
    labelPalabra2.place(x=0,y=110)
    
    varEntry2 = StringVar()
    entryPalabra2 = Entry(frameWigets,width=20, textvariable=varEntry2)
    entryPalabra2.place(x=30,y=150)

    #menu
    labelPalabra1 = Label(frameWigets, text="4. Determinar si las palabras son:",width=30,height=2)
    labelPalabra1.place(x=0,y=200)

    varCombo = StringVar()
    menuOpciones = TTK.Combobox(frameWigets,values=("A: Contar palabras comunes", "B: Listar palabras comunes", "C: Idioma que mas aporto a otro (%)","D: Listar todos los idiomas que aportaron a otro"), width=30, textvariable=varCombo)
    menuOpciones.place(x=0,y=240)

    #print Options
    varPrint = IntVar()
    R1 = Radiobutton(frameTexto, text="Todos los detalles de ruta", variable=varPrint, value=1)
    R1.place(x=15,y=0)

    R2 = Radiobutton(frameTexto, text="Ruta resumida", variable=varPrint, value=2)
    R2.select()
    R2.place(x=15,y=30)

    #TextField_path
    textPath=tkst.ScrolledText(frameTexto,width=120,height=21)
    textPath.place(x=0,y=60)

    #TextField_result
    textResult=tkst.ScrolledText(frameTexto,width=120,height=10)
    textResult.place(x=0,y=420)

    botonEjecutar=Button(frameWigets,width=28,height=2, text="Ejecutar",bg="dodger blue", command= lambda: run_query("idioma_idioma",varEntry1,varEntry2,varCombo,textPath,textResult,varPrint))
    botonEjecutar.place(x=0,y=300)
     
    root.mainloop()
    


root = tkinter.Tk()
root.title("Descubre el origen de las palabras...")
root.geometry("1200x600+100+50")
 
menubar = Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Palabra-Palabra", command= lambda: palabra_palabra(root))
filemenu.add_separator()
filemenu.add_command(label="Palabra-Idioma", command=lambda: palabra_idioma(root))
filemenu.add_separator()
filemenu.add_command(label="Idioma-Idioma", command=lambda: idioma_idioma(root))

menubar.add_cascade(label="Operaciones", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Ayuda", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Acerca de", menu=helpmenu)

salirmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Salir", command=salir)


var=BooleanVar()
#checkBox_etymology = Checkbutton(root, text="rel:derived", variable=var, command= lambda: var_states(var))
#checkBox_etymology.place(x=50,y=30)
# display the menu
root.config(menu=menubar)
root.mainloop()


