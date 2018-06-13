import tkinter
from tkinter import *
import tkinter.ttk as TTK
import tkinter.scrolledtext as tkst



def hello():
    print("Hola mundo")


def salir():
    root.destroy()


def palabra_palabra():
    print("Palabra-Palabra")
    window=tkinter.Tk()
    window.title("Palabra-Palabra")
    window.geometry("700x600+100+50")
    #Frames
    frameCuadro=Frame(window,width=200,height=200 ,bg="cornsilk2")
    frameCuadro.place(x=0,y=0)

    frameWigets = Frame(window,width=200,height=400 ,bg="cornsilk2")
    frameWigets.place(x=0,y=200)

    frameTexto = Frame(window,width=500,height=600 ,bg="gray91")
    frameTexto.place(x=200,y=0)
    #Checkbox
    labelRelaciones = Label(frameCuadro, text="1. Relaciones a considerar",width=28,height=2)
    labelRelaciones.place(x=0,y=0)

    checkBox_etymology = Checkbutton(frameCuadro, text="rel:derived")
    checkBox_etymology.place(x=50,y=30)
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:etymology")
    checkBox_etymology.place(x=50,y=50)
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:etymology_related")
    checkBox_etymology.place(x=50,y=70)
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:etymology_origin_of")
    checkBox_etymology.place(x=50,y=90)
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:etymology")
    checkBox_etymology.place(x=50,y=110)
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:has_derived_from")
    checkBox_etymology.place(x=50,y=130)
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:variant_orthography")
    checkBox_etymology.place(x=50,y=150)

    
    #Palabra 1
    labelPalabra1 = Label(frameWigets, text="2. Palabra 1",width=28,height=2)
    labelPalabra1.place(x=0,y=10)

    entryPalabra1 = Entry(frameWigets,width=20)
    entryPalabra1.place(x=30,y=50)

    #Palabra 2
    labelPalabra2 = Label(frameWigets, text="3. Palabra 2", width=28,height=2)
    labelPalabra2.place(x=0,y=110)
    
    entryPalabra2 = Entry(frameWigets,width=20)
    entryPalabra2.place(x=30,y=150)

    #menu
    labelPalabra1 = Label(frameWigets, text="4. Determinar si las palabras son:",width=30,height=2)
    labelPalabra1.place(x=0,y=200)
    
    menuOpciones = TTK.Combobox(frameWigets,values=("Hermanas", "Primas", "Hija una de otra","Tia","Primas con grado"), width=30)
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
    
    botonEjecutar=Button(frameWigets,width=28,height=2, text="Ejecutar",bg="dodger blue")
    botonEjecutar.place(x=0,y=300)
    
    root.mainloop()


def palabra_idioma():
    print("Palabra-Idioma")
    window=tkinter.Tk()
    window.title("Palabra-Palabra")
    window.geometry("700x600+100+50")
    #Frames
    frameCuadro=Frame(window,width=200,height=200 ,bg="cornsilk2")
    frameCuadro.place(x=0,y=0)

    frameWigets = Frame(window,width=200,height=400 ,bg="cornsilk2")
    frameWigets.place(x=0,y=200)

    frameTexto = Frame(window,width=500,height=600 ,bg="gray91")
    frameTexto.place(x=200,y=0)
    #Checkbox
    labelRelaciones = Label(frameCuadro, text="1. Relaciones a considerar",width=28,height=2)
    labelRelaciones.place(x=0,y=0)
    
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:derived")
    checkBox_etymology.place(x=50,y=30)
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:etymology")
    checkBox_etymology.place(x=50,y=50)
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:etymology_related")
    checkBox_etymology.place(x=50,y=70)
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:etymology_origin_of")
    checkBox_etymology.place(x=50,y=90)
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:etymology")
    checkBox_etymology.place(x=50,y=110)
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:has_derived_from")
    checkBox_etymology.place(x=50,y=130)
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:variant_orthography")
    checkBox_etymology.place(x=50,y=150)
    
    #Palabra 1
    labelPalabra1 = Label(frameWigets, text="2. Palabra",width=28,height=2)
    labelPalabra1.place(x=0,y=10)

    entryPalabra1 = Entry(frameWigets,width=20)
    entryPalabra1.place(x=30,y=50)

    #Palabra 2
    idioma = Label(frameWigets, text="3. Idioma(s)", width=28,height=2)
    idioma.place(x=0,y=110)
    
    entryPalabra2 = Entry(frameWigets,width=20)
    entryPalabra2.place(x=30,y=150)

    #menu
    labelPalabra1 = Label(frameWigets, text="4. Operaciones entre palabra e idioma(s):",width=30,height=2)
    labelPalabra1.place(x=0,y=200)
    
    menuOpciones = TTK.Combobox(frameWigets,values=("Palabra relacioanda con idioma?", "Conjunto de todas las palabras originadas en idioma", "Listar idiomas relacionados con la palabra"), width=30)
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

    botonEjecutar=Button(frameWigets,width=28,height=2, text="Ejecutar",bg="dodger blue")
    botonEjecutar.place(x=0,y=300)
    
    root.mainloop()

def idioma_idioma():
    print("Idioma-Idioma")
    window=tkinter.Tk()
    window.title("Idioma-Idioma")
    window.geometry("700x600+100+50")
    #Frames
    frameCuadro=Frame(window,width=200,height=200 ,bg="cornsilk2")
    frameCuadro.place(x=0,y=0)

    frameWigets = Frame(window,width=200,height=400 ,bg="cornsilk2")
    frameWigets.place(x=0,y=200)

    frameTexto = Frame(window,width=500,height=600 ,bg="gray91")
    frameTexto.place(x=200,y=0)
  
    #Checkbox
    labelRelaciones = Label(frameCuadro, text="1. Relaciones a considerar",width=28,height=2)
    labelRelaciones.place(x=0,y=0)
    
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:derived")
    checkBox_etymology.place(x=50,y=30)
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:etymology")
    checkBox_etymology.place(x=50,y=50)
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:etymology_related")
    checkBox_etymology.place(x=50,y=70)
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:etymology_origin_of")
    checkBox_etymology.place(x=50,y=90)
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:etymology")
    checkBox_etymology.place(x=50,y=110)
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:has_derived_from")
    checkBox_etymology.place(x=50,y=130)
    checkBox_etymology = Checkbutton(frameCuadro, text="rel:variant_orthography")
    checkBox_etymology.place(x=50,y=150)
    
    #Palabra 1
    labelPalabra1 = Label(frameWigets, text="2. Idioma 1",width=28,height=2)
    labelPalabra1.place(x=0,y=10)

    entryPalabra1 = Entry(frameWigets,width=20)
    entryPalabra1.place(x=30,y=50)

    #Palabra 2
    labelPalabra2 = Label(frameWigets, text="3. Idioma 2", width=28,height=2)
    labelPalabra2.place(x=0,y=110)
    
    entryPalabra2 = Entry(frameWigets,width=20)
    entryPalabra2.place(x=30,y=150)

    #menu
    labelPalabra1 = Label(frameWigets, text="4. Determinar si las palabras son:",width=30,height=2)
    labelPalabra1.place(x=0,y=200)
    
    menuOpciones = TTK.Combobox(frameWigets,values=("Contar palabras comunes", "Listar palabras comunes", "Idioma que mas aporto a otro (%)","Listar idiomas que aportaron a otro"), width=30)
    menuOpciones.place(x=0,y=240)

    botonEjecutar=Button(frameWigets,width=28,height=2, text="Ejecutar",bg="dodger blue")
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
filemenu.add_command(label="Palabra-Palabra", command=palabra_palabra)
filemenu.add_separator()
filemenu.add_command(label="Palabra-Idioma", command=palabra_idioma)
filemenu.add_separator()
filemenu.add_command(label="Idioma-Idioma", command=idioma_idioma)

menubar.add_cascade(label="Operaciones", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Ayuda", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Acerca de", menu=helpmenu)

salirmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Salir", command=salir)

# display the menu
root.config(menu=menubar)
root.mainloop()
