#!/usr/bin/python
import random
import tkinter as tk

def loadDB(langs, db):
    if langs == []:
        return db
    with open("../etymwn/etymwn.tsv") as f:
        i = 0
        for l in f:
            for lang in langs:
                if(l.find(lang+":") != -1):
                    db.append(Relacion(l))
            i += 1
        print("dbSize:",len(db))
    return list(set(db))

def getRelatedLangs(word):
    langs = []
    with open("../etymwn/etymwn.tsv") as f:
        i = 0
        for l in f:
            if(l.find(" "+word+"\t") != -1):
                s = l.split("\t")
                l1 = s[0].split(":")[0]
                l2 = s[2].split(":")[0]
                if (not l1 in langs):
                    print(l)
                    langs.append(l1)
                if (not l2 in langs):
                    print(l)
                    langs.append(l2)
    print("langs:", langs)
    return langs

class Palabra():
    def __init__(self, palabra):
        tmp = palabra.split(": ")
        self.idioma = tmp[0]
        self.palabra = tmp[1].split("\n")[0]

class Relacion():
    """Clase para descomponer los datos de las relaciones"""
    def __init__(self, rel):
        tmp = rel.split("\t")
        self.izq = Palabra(tmp[0])
        self.rel = tmp[1].split(":")[1]
        self.der = Palabra(tmp[2])

    def __str__(self):
        res = ""
        res += self.izq.palabra
        res += "(" + self.izq.idioma + ") ---"
        res += self.rel + "--->"
        res += self.der.palabra
        res += "(" + self.der.idioma + ")"
        return res

db = loadDB(["eng"], [])
loadedLanguages = ["eng"]

top = tk.Tk()

#w = Button ( top )
lbl = tk.Label(top, text="Enter a query below", font=("Arial Bold", 12))
lbl.grid(column=0, row=0)

ent = tk.Entry(top)
ent.grid(column=0, row=1)

def clicked():
    global db, loadedLanguages
    query = ent.get()
    if len(query) < 2:
        return
    toAdd = []
    for j in getRelatedLangs(query):
        print("j:", j)
        if j not in loadedLanguages:
            toAdd.append(j)
    db = loadDB(toAdd, db)
    loadedLanguages += toAdd
    lbl.configure(text=db[int(random.uniform(0,len(db)))])

btn = tk.Button(top, text="Search", command=clicked)
btn.grid(column=0, row=2)

top.geometry('650x200')
top.mainloop()





aaq: Pawanobskewi       rel:etymological_origin_of      eng: Penobscot
aaq: senabe     rel:etymological_origin_of      eng: sannup 
abe: waniigan   rel:etymological_origin_of      eng: wangan
abe: waniigan   rel:etymological_origin_of      eng: wannigan
abs: beta       rel:etymological_origin_of      zsm: beta
adt: yuru       rel:etymological_origin_of      eng: euro
afr: -heid      rel:etymological_origin_of      afr: moontlikheid
afr: -ig        rel:etymological_origin_of      afr: denkbeeldig
afr: -ig        rel:etymological_origin_of      afr: tydig
afr: -ing       rel:etymological_origin_of      afr: verbuiging
afr: -lik       rel:etymological_origin_of      afr: persoonlik
afr: -lik       rel:etymological_origin_of      afr: tydelik
afr: -lik       rel:etymological_origin_of      afr: wetenskaplik
afr: -lik       rel:etymological_origin_of      afr: wetlik
afr: -lik       rel:has_derived_form    afr: wetenskaplik
