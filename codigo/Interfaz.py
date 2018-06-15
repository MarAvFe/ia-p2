import tkinter
from tkinter import *
import tkinter.ttk as TTK
import tkinter.scrolledtext as tkst




def hello():
    print("Hola mundo")



def var_states(derived,ety,related,origin,etymology,form,ortho):
    print(derived.get())
    print(ety.get())
    print(related.get())
    print(origin.get())
    print(etymology.get())
    print(form.get())
    print(ortho.get())
    print("Aquí deberia llamar a la funcion de marcello con la variable.get()")
    #if(varDerived.get()==True):
    #    print(True)
    #else:    
    #    print(False)
    #print(varDerived.get())
    #print("el checkbox esta: %d" % (varDerived))

def run_query(entry1, entry2,opcion):
    print("Dato de query 1 es: %s" % entry1.get())
    print("Dato de query 2 es: %s" % entry2.get())
    print("El query es %s" % opcion.get())
    

def salir():
    root.destroy()


def palabra_palabra(root):
    print("Palabra-Palabra")
    #window=tkinter.Tk()
    #window.title("Palabra-Palabra")
    #window.geometry("700x600+100+50")
    #Frames
    frameCuadro=Frame(root,width=200,height=200 ,bg="cornsilk2")
    frameCuadro.place(x=0,y=0)

    frameWigets = Frame(root,width=200,height=400 ,bg="cornsilk2")
    frameWigets.place(x=0,y=200)

    frameTexto = Frame(root,width=500,height=600 ,bg="gray91")
    frameTexto.place(x=200,y=0)
    #Checkbox
    labelRelaciones = Label(root, text="1. Relaciones a considerar",width=28,height=2)
    labelRelaciones.place(x=0,y=0)

    var_derived = BooleanVar()
    var_ety = BooleanVar()
    var_related = BooleanVar()
    var_origin = BooleanVar()
    var_etymology = BooleanVar()
    var_form = BooleanVar()
    var_ortho = BooleanVar()
    
    checkBox_derived = Checkbutton(frameCuadro, text="rel:derived", variable=var_derived, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_derived.place(x=30,y=30)
    
    checkBox_ety = Checkbutton(frameCuadro, text="rel:etymologically", variable=var_ety, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_ety.place(x=30,y=50)
    
    checkBox_related = Checkbutton(frameCuadro, text="rel:etymologically_related", variable=var_related, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_related.place(x=30,y=70)
    
    checkBox_origin = Checkbutton(frameCuadro, text="rel:etymological_origin_of", variable=var_origin, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_origin.place(x=30,y=90)
    
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:etymology", variable=var_etymology, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_etymology.place(x=30,y=110)
    
    checkBox_form = Checkbutton(frameCuadro, text="rel:has_derived_form", variable=var_form, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_form.place(x=30,y=130)
    
    checkBox_ortho = Checkbutton(frameCuadro, text="rel:variant:orthography", variable=var_ortho, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_ortho.place(x=30,y=150)
    
    #Palabra 1
    labelPalabra1 = Label(frameWigets, text="2. Palabra 1",width=28,height=2)
    labelPalabra1.place(x=0,y=10)

    varEntry1 = StringVar()
    entryPalabra1 = Entry(frameWigets,width=20, textvariable=varEntry1)
    entryPalabra1.place(x=30,y=50)

    #Palabra 2
    labelPalabra2 = Label(frameWigets, text="3. Palabra 2", width=28,height=2)
    labelPalabra2.place(x=0,y=110)

    varEntry2 = StringVar()
    entryPalabra2 = Entry(frameWigets,width=20, textvariable=varEntry2)
    entryPalabra2.place(x=30,y=150)

    #menu
    labelPalabra1 = Label(frameWigets, text="4. Determinar si las palabras son:",width=30,height=2)
    labelPalabra1.place(x=0,y=200)

    varCombo = StringVar()
    menuOpciones = TTK.Combobox(frameWigets,values=("Hermanas", "Primas", "Hija una de otra","Tia","Primas con grado"), width=30, textvariable=varCombo)
    menuOpciones.place(x=0,y=240)

    #TextField
    #text=tkst.ScrolledText(frameTexto,width=60,height=37)
    #text.pack()

    tree = TTK.Treeview(frameTexto)

    tree.insert("",END,text="Nelson")
    item = tree.insert("",0,text="Elemento1")
    subItem = tree.insert(item, END, text = "Subelemento1")
    a = "japones"
    tree.insert(subItem,END, text = "elemento 3", iid=a)
    tree.insert(a,END,text ="kulingao")
    tree.pack() 
    
    botonEjecutar=Button(frameWigets,width=28,height=2, text="Ejecutar",bg="dodger blue", command= lambda: run_query(varEntry1,varEntry2,varCombo))
    botonEjecutar.place(x=0,y=300)
    
    root.mainloop()


def palabra_idioma(root):
    print("Palabra-Idioma")
    #window=tkinter.Tk()
    #window.title("Palabra-Palabra")
    #window.geometry("700x600+100+50")
    #Frames
    frameCuadro=Frame(root,width=200,height=200 ,bg="cornsilk2")
    frameCuadro.place(x=0,y=0)

    frameWigets = Frame(root,width=200,height=400 ,bg="cornsilk2")
    frameWigets.place(x=0,y=200)

    frameTexto = Frame(root,width=500,height=600 ,bg="gray91")
    frameTexto.place(x=200,y=0)
    #Checkbox
    labelRelaciones = Label(frameCuadro, text="1. Relaciones a considerar",width=28,height=2)
    labelRelaciones.place(x=0,y=0)
    
    var_derived = BooleanVar()
    var_ety = BooleanVar()
    var_related = BooleanVar()
    var_origin = BooleanVar()
    var_etymology = BooleanVar()
    var_form = BooleanVar()
    var_ortho = BooleanVar()
    
    checkBox_derived = Checkbutton(frameCuadro, text="rel:derived", variable=var_derived, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_derived.place(x=30,y=30)
    
    checkBox_ety = Checkbutton(frameCuadro, text="rel:etymologically", variable=var_ety, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_ety.place(x=30,y=50)
    
    checkBox_related = Checkbutton(frameCuadro, text="rel:etymologically_related", variable=var_related, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_related.place(x=30,y=70)
    
    checkBox_origin = Checkbutton(frameCuadro, text="rel:etymological_origin_of", variable=var_origin, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_origin.place(x=30,y=90)
    
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:etymology", variable=var_etymology, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_etymology.place(x=30,y=110)
    
    checkBox_form = Checkbutton(frameCuadro, text="rel:has_derived_form", variable=var_form, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_form.place(x=30,y=130)
    
    checkBox_ortho = Checkbutton(frameCuadro, text="rel:variant:orthography", variable=var_ortho, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_ortho.place(x=30,y=150)
    
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
    menuOpciones = TTK.Combobox(frameWigets,values=("Palabra relacioanda con idioma?", "Conjunto de todas las palabras originadas en idioma", "Listar idiomas relacionados con la palabra"), width=30, textvariable=varCombo)
    menuOpciones.place(x=0,y=240)

    #TextField
    #text=tkst.ScrolledText(frameTexto,width=60,height=37)
    #text.pack()

    tree = TTK.Treeview(frameTexto)

    tree.insert("",END,text="Nelson")
    item = tree.insert("",0,text="Elemento1")
    subItem = tree.insert(item, END, text = "Subelemento1")

    a = "japones"
    tree.insert(subItem,END, text = "elemento 3", iid=a)
    tree.insert(a,END,text ="kulingao")

    tree.pack() 

    botonEjecutar=Button(frameWigets,width=28,height=2, text="Ejecutar",bg="dodger blue", command= lambda: run_query(varEntry1,varEntry2,varCombo))
    botonEjecutar.place(x=0,y=300)
    
    root.mainloop()

def idioma_idioma(root):
    print("Idioma-Idioma")
    #window=tkinter.Tk()
    #window.title("Idioma-Idioma")
    #window.geometry("700x600+100+50")
    #Frames
    frameCuadro=Frame(root,width=200,height=200 ,bg="cornsilk2")
    frameCuadro.place(x=0,y=0)

    frameWigets = Frame(root,width=200,height=400 ,bg="cornsilk2")
    frameWigets.place(x=0,y=200)

    frameTexto = Frame(root,width=500,height=600 ,bg="gray91")
    frameTexto.place(x=200,y=0)
  
    #Checkbox
    labelRelaciones = Label(frameCuadro, text="1. Relaciones a considerar",width=28,height=2)
    labelRelaciones.place(x=0,y=0)
    
    var_derived = BooleanVar()
    var_ety = BooleanVar()
    var_related = BooleanVar()
    var_origin = BooleanVar()
    var_etymology = BooleanVar()
    var_form = BooleanVar()
    var_ortho = BooleanVar()
    
    checkBox_derived = Checkbutton(frameCuadro, text="rel:derived", variable=var_derived, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_derived.place(x=30,y=30)
    checkBox_ety = Checkbutton(frameCuadro, text="rel:etymologically", variable=var_ety, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_ety.place(x=30,y=50)
    checkBox_related = Checkbutton(frameCuadro, text="rel:etymologically_related", variable=var_related, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_related.place(x=30,y=70)
    checkBox_origin = Checkbutton(frameCuadro, text="rel:etymological_origin_of", variable=var_origin, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_origin.place(x=30,y=90)
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:etymology", variable=var_etymology, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_etymology.place(x=30,y=110)
    checkBox_form = Checkbutton(frameCuadro, text="rel:has_derived_form", variable=var_form, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_form.place(x=30,y=130)
    checkBox_ortho = Checkbutton(frameCuadro, text="rel:variant:orthography", variable=var_ortho, command= lambda: var_states(var_derived,var_ety,var_related,var_origin,var_etymology,var_form,var_ortho))
    checkBox_ortho.place(x=30,y=150)
    
    #Palabra 1
    labelPalabra1 = Label(frameWigets, text="2. Idioma 1",width=28,height=2)
    labelPalabra1.place(x=0,y=10)

    varEntry1 = StringVar()
    entryPalabra1 = Entry(frameWigets,width=20, textVariable=varEntry1 )
    entryPalabra1.place(x=30,y=50)

    #Palabra 2
    labelPalabra2 = Label(frameWigets, text="3. Idioma 2", width=28,height=2)
    labelPalabra2.place(x=0,y=110)
    
    entryPalabra2 = Entry(frameWigets,width=20, textVariable=varEntry1)
    entryPalabra2.place(x=30,y=150)

    #menu
    labelPalabra1 = Label(frameWigets, text="4. Determinar si las palabras son:",width=30,height=2)
    labelPalabra1.place(x=0,y=200)

    varCombo = StringVar()
    menuOpciones = TTK.Combobox(frameWigets,values=("Contar palabras comunes", "Listar palabras comunes", "Idioma que mas aporto a otro (%)","Listar idiomas que aportaron a otro"), width=30, textvariable=varCombo)
    menuOpciones.place(x=0,y=240)

    botonEjecutar=Button(frameWigets,width=28,height=2, text="Ejecutar",bg="dodger blue", command= lambda: run_query(varEntry1,varEntry2,varCombo))
    botonEjecutar.place(x=0,y=300)

    #TextField
    #text=tkst.ScrolledText(frameTexto,width=60,height=37)
    #text.pack()
    
    tree = TTK.Treeview(frameTexto)

    tree.insert("",END,text="Nelson")
    item = tree.insert("",0,text="Elemento1")
    subItem = tree.insert(item, END, text = "Subelemento1")

    a = "japones"
    tree.insert(subItem,END, text = "elemento 3", iid=a)
    tree.insert(a,END,text ="kulingao")

    tree.pack()    
    root.mainloop()
    


root = tkinter.Tk()
root.title("Descubre el origen de las palabras...")
root.geometry("700x600+100+50")
 
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

