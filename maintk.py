import pandas as pd
import psycopg2 as pg
import openpyxl as ex
import pyautogui as pyg
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import tkinter as Tk


from numpy.random import randint



ulaz=None
zgrada=None
stan=None
spret=None
vlasnik=None
porodnos=None
mernibroj=None
fizickavel=None
iz_list=[]
prazan=None

from tkinter import *

import tkinter

from klase1 import *

root = Tk()  # create CTk window like you do with the Tk window
root.geometry("500x500")
bg = PhotoImage(file = "Beograd.png")

buton1=Button(root,width=50,height=1,
            text='Pretraga vlasnika stana prema adresi, broju ulaza i broju stana',
            command=lambda:buton1_podaci()
            )
buton1.place(relx=0.1,rely=0.1,anchor=tkinter.W)

buton2=Button(root,
              width=50,
              height=1,
              text='Prikazi broja clanova domacinstva',
              command=lambda:buton2_podaci()
              )
buton2.place(relx=0.1,rely=0.3,anchor=tkinter.W)

buton3=Button(root,width=50,height=1,
            text='Prikaz cene stana',
            command=lambda:buton3_podaci()

            )
buton3.place(relx=0.1,rely=0.5,anchor=tkinter.W)

buton4=Button(root,width=50,height=1,
            text='Prikaz vlasnika stanova prema ceni ili povrsini stana',
            command=lambda:buton4_podaci()
            )
buton4.place(relx=0.1,rely=0.7,anchor=tkinter.W)

buton5=Button(root,width=50,height=1,
            text='Pretraga podataka vlasnika stana',
            command=lambda:buton51_podaci())
buton5.place(relx=0.1,rely=0.9,anchor=tkinter.W)

#================================================================================== Button 1


def buton1_podaci():
    rootb11=Toplevel(root)
    rootb11.geometry('800x400')
    aa=A.lista_zgrada
    bb=len(aa)
    cc=bb-1  
    ll=[]
    for i in range(1,cc):
        l=[]
        for j in aa:
            l.append(j[i-1])
        ll.append(l)             
    
    
    b1l1=Label(rootb11,text='IZABERITE ZGRADU NA ADRESI')
    b1l1.pack()
    ddd=A.lista_ulazi[0]


    clicked=StringVar()
    clicked.set('')
    drop=OptionMenu(
                    rootb11,
                    clicked,
                    *ll
                    )
    drop.pack(pady=5)

    b1b1=Button(
                rootb11,text='Potvrdu izbor zgrade',
                command=lambda:izaberizgradu(clicked.get())
                )
    b1b1.pack(pady=5)
    def izaberizgradu(brojz):
        global zgrada
        brojz=brojz.replace('(','')
        brojz=brojz.replace(')','')
        brojz=brojz.replace(',','')
        brojz=brojz.split(' ')
        zgrada=int(brojz[0])
  
        

        b1l2=Label(rootb11,text='IZABERITE BROJ ULAZA')
        b1l2.pack()
        if zgrada==1:
            ddd=A.lista_ulazi1
        else:
            ddd=A.lista_ulazi2
        clickedu=StringVar()
        clickedu.set('')
        drop=OptionMenu(
                        rootb11,
                        clickedu,
                        *ddd
                        )
        drop.pack(pady=5)

        b1b2=Button(
                rootb11,text='Potvrdi izbor ulaza',
                command=lambda:izaberulaz(clickedu.get())
                )
        b1b2.pack(pady=5)
    
    
        def izaberulaz(broj):
            global ulaz
            ulaz=int(broj)
            global zgrada
            print(A.lista_stana(ulaz,zgrada))

            b1l3=Label(rootb11,text='UNESITE BROJ STANA')
            b1l3.pack()

            stanovi=StringVar()
            stanovi.set('')
            drop=OptionMenu(
                    rootb11,
                    stanovi,
                    *A.brojevi_stanova
                    )
            drop.pack(pady=5)

            b1b4=Button(
                rootb11,text='Potvrdi izbor stana',
                command=lambda:izaberistan(stanovi.get())
                )
            b1b4.pack(pady=5)


            def izaberistan(sbroj):
                global stan
                global ulaz
                global zgrada
                stan=int(sbroj)
                prikaz_rezultata()
            

            def prikaz_rezultata():
                izlaz=Toplevel(root)
                izlaz.geometry('800x400')
                global zgrada
                global ulaz
                global stan
                a=A.buton1('idzgrade',zgrada,'brulaza',ulaz,'brstana',stan)
                l1=Label(
                    izlaz,text="Izabrana zgrada je {}".format(zgrada),
                        font=("Arial",12),
                        bg="white",
                        fg='green'
                        )
                l1.pack(pady=10)
                l2=Label(izlaz,text="Izabrani ulaz je {}".format(ulaz),
                    font=("Arial",12),
                    bg="white",
                    fg='green'
                    )
                l2.pack(pady=10)
                l3=Label(izlaz,text="Izabrani stan je {}".format(stan),     
                    font=("Arial",12),
                    bg="white",
                    fg='green'
                    )
                l3.pack(pady=10)
                l4=Label(izlaz,text=' ',
                    font=("Arial",12),
                    bg="white",
                    fg='green'
                    )
                l4.pack(pady=10)
                b1=Button(izlaz,text="Prikazi reezultat",command=lambda:[l4.config(text=a),rootb11.destroy()],
                        width=50,
                        height=1
                        )
                b1.pack(pady=10)
                b2=Button(izlaz,text="EXIT",command=lambda:[pyg.alert('DOVIDJENJA'),izlaz.destroy()],
                    borderwidth=1,
                    font=("Arial",12),
                    bg="white",
                    fg='green'
                    )
                b2.pack(pady=10)
#================================================================================== Button 2
def buton2_podaci():
    rootb12=Toplevel(root)
    rootb12.geometry('800x400')
    aa=A.lista_zgrada
    bb=len(aa)
    cc=bb-1  
    ll=[]
    for i in range(1,cc):
        l=[]
        for j in aa:
            l.append(j[i-1])
        ll.append(l)             
    
    
    b1l1=Label(rootb12,text='IZABERITE ZGRADU NA ADRESI')
    b1l1.pack()
    ddd=A.lista_ulazi[0]


    clicked=StringVar()
    clicked.set('')
    drop=OptionMenu(
                    rootb12,
                    clicked,
                    *ll
                    )
    drop.pack(pady=5)

    b1b1=Button(
                rootb12,text='Potvrdu izbor zgrade',
                command=lambda:izaberizgradu(clicked.get())
                )
    b1b1.pack(pady=5)
    def izaberizgradu(brojz):
        global zgrada
        brojz=brojz.replace('(','')
        brojz=brojz.replace(')','')
        brojz=brojz.replace(',','')
        brojz=brojz.split(' ')
        zgrada=int(brojz[0])

        b1l2=Label(rootb12,text='IZABERITE BROJ ULAZA')
        b1l2.pack()
        if zgrada==1:
            ddd=A.lista_ulazi1
        else:
            ddd=A.lista_ulazi2
        clickedu=StringVar()
        clickedu.set('')
        drop=OptionMenu(
                        rootb12,
                        clickedu,
                        *ddd
                        )
        drop.pack(pady=5)

        b1b2=Button(
                rootb12,text='Potvrdi izbor ulaza',
                command=lambda:izaberulaz(clickedu.get())
                )
        b1b2.pack(pady=5)
    
    
        def izaberulaz(broj):
            global ulaz
            ulaz=int(broj)
            global zgrada
            print(A.lista_stana(ulaz,zgrada))

            b1l3=Label(rootb12,text='UNESITE BROJ STANA')
            b1l3.pack()

            stanovi=StringVar()
            stanovi.set('')
            drop=OptionMenu(
                    rootb12,
                    stanovi,
                    *A.brojevi_stanova
                    )
            drop.pack(pady=5)

            b1b4=Button(
                rootb12,text='Potvrdi izbor stana',
                command=lambda:izaberistan(stanovi.get())
                )
            b1b4.pack(pady=5)


            def izaberistan(sbroj):
                global stan
                global ulaz
                global zgrada
                stan=int(sbroj)
                prikaz_rezultata()
            

            def prikaz_rezultata():
                izlaz2=Toplevel(root)
                izlaz2.geometry('800x400')
                global zgrada
                global ulaz
                global stan
                a=A.buton2('idzgrade',zgrada,'brulaza',ulaz,'brstana',stan)
                print(a)
                l1=Label(
                    izlaz2,text="Izabrana zgrada je {}".format(zgrada),
                        font=("Arial",12),
                        bg="white",
                        fg='green'
                        )
                l1.pack(pady=10)
                l2=Label(izlaz2,text="Izabrani ulaz je {}".format(ulaz),
                    font=("Arial",12),
                    bg="white",
                    fg='green'
                    )
                l2.pack(pady=10)
                l3=Label(izlaz2,text="Izabrani stan je {}".format(stan),     
                    font=("Arial",12),
                    bg="white",
                    fg='green'
                    )
                l3.pack(pady=10)
                l4=Label(izlaz2,text=' ',
                    font=("Arial",12),
                    bg="white",
                    fg='green'
                    )
                l4.pack(pady=10)
                b1=Button(izlaz2,text="Prikazi reezultat",command=lambda:[l4.config(text=a),rootb12.destroy()],
                        width=50,
                        height=1
                        )
                b1.pack(pady=10)
                b2=Button(izlaz2,text="EXIT",command=lambda:izlaz2.destroy(),
                    borderwidth=1,
                    font=("Arial",12),
                    bg="white",
                    fg='green'
                    )
                b2.pack(pady=10)
#================================================================================== Button 3
def buton3_podaci():
    rootb13=Toplevel(root)
    rootb13.geometry('800x400')
    aa=A.lista_zgrada
    bb=len(aa)
    cc=bb-1  
    ll=[]
    for i in range(1,cc):
        l=[]
        for j in aa:
            l.append(j[i-1])
        ll.append(l)             
    
    
    b1l1=Label(rootb13,text='IZABERITE ZGRADU NA ADRESI')
    b1l1.pack()
    ddd=A.lista_ulazi[0]


    clicked=StringVar()
    clicked.set('')
    drop=OptionMenu(
                    rootb13,
                    clicked,
                    *ll
                    )
    drop.pack(pady=5)

    b1b1=Button(
                rootb13,text='Potvrdu izbor zgrade',
                command=lambda:izaberizgradu(clicked.get())
                )
    b1b1.pack(pady=5)
    def izaberizgradu(brojz):
        global zgrada
        brojz=brojz.replace('(','')
        brojz=brojz.replace(')','')
        brojz=brojz.replace(',','')
        brojz=brojz.split(' ')
        zgrada=int(brojz[0])

        b1l2=Label(rootb13,text='IZABERITE BROJ ULAZA')
        b1l2.pack()
        if zgrada==1:
            ddd=A.lista_ulazi1
        else:
            ddd=A.lista_ulazi2
        clickedu=StringVar()
        clickedu.set('')
        drop=OptionMenu(
                        rootb13,
                        clickedu,
                        *ddd
                        )
        drop.pack(pady=5)

        b1b2=Button(
                rootb13,text='Potvrdi izbor ulaza',
                command=lambda:izaberulaz(clickedu.get())
                )
        b1b2.pack(pady=5)
    
    
        def izaberulaz(broj):
            global ulaz
            ulaz=int(broj)
            global zgrada
            print(A.lista_stana(ulaz,zgrada))

            b1l3=Label(rootb13,text='IZABERITE BROJ STANA')
            b1l3.pack()

            stanovi=StringVar()
            stanovi.set('')
            drop=OptionMenu(
                    rootb13,
                    stanovi,
                    *A.brojevi_stanova
                    )
            drop.pack(pady=5)

            b1b4=Button(
                rootb13,text='Potvrdi izbor stana',
                command=lambda:izaberistan(stanovi.get())
                )
            b1b4.pack(pady=5)


            def izaberistan(sbroj):
                global stan
                global ulaz
                global zgrada
                stan=int(sbroj)
                prikaz_rezultata()
            

            def prikaz_rezultata():
                izlaz3=Toplevel(root)
                izlaz3.geometry('800x400')
                global zgrada
                global ulaz
                global stan
                a=A.buton3('idzgrade',zgrada,'brulaza',ulaz,'brstana',stan)
                print(a)
                l1=Label(
                    izlaz3,text="Izabrana je zgrada broj {}".format(zgrada),
                        font=("Arial",12),
                        bg="white",
                        fg='green'
                        )
                l1.pack(pady=10)
                l2=Label(izlaz3,text="Izabrani je ulaz broj {}".format(ulaz),
                    font=("Arial",12),
                    bg="white",
                    fg='green'
                    )
                l2.pack(pady=10)
                l3=Label(izlaz3,text="Izabrani je stan broj {}".format(stan),     
                    font=("Arial",12),
                    bg="white",
                    fg='green'
                    )
                l3.pack(pady=10)
                l4=Label(izlaz3,text=' ',
                    font=("Arial",12),
                    bg="white",
                    fg='green'
                    )
                l4.pack(pady=10)
                b1=Button(izlaz3,text="Prikazi reezultat",command=lambda:[l4.config(text=a),rootb13.destroy()],
                        width=50,
                        height=1
                        )
                b1.pack(pady=10)
                b2=Button(izlaz3,text="EXIT",command=lambda:izlaz3.destroy(),
                    borderwidth=1,
                    font=("Arial",12),
                    bg="white",
                    fg='green'
                    )
                b2.pack(pady=10)

#================================================================================== Button 4
def buton4_podaci():
    rootb14=Toplevel(root)
    rootb14.geometry('800x800')
    aa=A.lista_zgrada
    bb=len(aa)
    cc=bb-1  
    ll=[]
    for i in range(1,cc):
        l=[]
        for j in aa:
            l.append(j[i-1])
        ll.append(l)             
    
    
    b1l1=Label(rootb14,text='IZABERITE ZGRADU NA ADRESI')
    b1l1.pack()
    ddd=A.lista_ulazi[0]


    clicked=StringVar()
    clicked.set('')
    drop=OptionMenu(
                    rootb14,
                    clicked,
                    *ll
                    )
    drop.pack(pady=5)

    b1b1=Button(
                rootb14,text='Potvrdu izbor zgrade',
                command=lambda:izaberizgradu(clicked.get())
                )
    b1b1.pack(pady=5)
    def izaberizgradu(brojz):
        global zgrada
        brojz=brojz.replace('(','')
        brojz=brojz.replace(')','')
        brojz=brojz.replace(',','')
        brojz=brojz.split(' ')
        zgrada=int(brojz[0])
        b1l2=Label(rootb14,text='IZABERITE BROJ ULAZA')
        b1l2.pack()
        if zgrada==1:
            ddd=A.lista_ulazi1
        else:
            ddd=A.lista_ulazi2
        clickedu=StringVar()
        clickedu.set('')
        drop=OptionMenu(
                        rootb14,
                        clickedu,
                        *ddd
                        )
        drop.pack(pady=5)

        b1b2=Button(
                rootb14,text='Potvrdi izbor ulaza',
                command=lambda:izaberulaz(clickedu.get())
                )
        b1b2.pack(pady=5)
        def izaberulaz(broj):
            global ulaz
            ulaz=int(broj)
            global zgrada
            print(A.lista_stana(ulaz,zgrada))
            b1l3=Label(rootb14,text='IZABERITE BROJ STANA')
            b1l3.pack()
            stanovi=StringVar()
            stanovi.set('')
            drop=OptionMenu(
                    rootb14,
                    stanovi,
                    *A.brojevi_stanova
                    )
            drop.pack(pady=5)
            b1b4=Button(
                rootb14,text='Potvrdi izbor stana',
                command=lambda:izaberistan(stanovi.get())
                )
            b1b4.pack(pady=5)
            def izaberistan(sbroj):
                global stan
                global ulaz
                global zgrada
                global ulaz
                global porodnos
                global vlasnik
                stan=int(sbroj)
                b4l3=Label(rootb14,text='IZABERITE KRITERIJUM PRETRAGE')
                b4l3.pack()
                krit=StringVar()
                krit.set('')
                drop=OptionMenu(
                                rootb14,
                                krit,'vece od','jednako','manje od'
                                )
                drop.pack(pady=5)
                b4b4=Button(
                    rootb14,text='Potvrdi izbor porodnosa',
                    command=lambda:izaberikrit(krit.get())
                    )
                b4b4.pack(pady=5)
                def izaberikrit(kbroj):
                    global stan
                    global ulaz
                    global zgrada
                    global ulaz
                    global porodnos
                    global vlasnik
                    porodnos=str(kbroj)
                    b4l7=Label(rootb14,text='IZABERITE USLOV PRETRAGE')
                    b4l7.pack()

                    mer=StringVar()
                    mer.set('')
                    drop=OptionMenu(
                                rootb14,
                                mer,'povrsina','cena'
                                )
                    drop.pack(pady=5)
                    b4b8=Button(
                        rootb14,text='Potvrdi izbor porodnosa',
                        command=lambda:izaberfizickavel(mer.get())
                    )
                    b4b8.pack(pady=5)
                    def izaberfizickavel(merka):
                        global stan
                        global ulaz
                        global zgrada
                        global ulaz
                        global porodnos
                        global vlasnik
                        global mernibroj
                        global fizickavel
                        fizickavel=str(merka)
                        b4l6=Label(rootb14,text='IZABERITE KRITERIJUM PRETRAGE')
                        b4l6.pack()
                        eusl=Entry(rootb14)
                        eusl.pack(pady=5)
                        b4b5=Button(
                                rootb14,text='Potvrdi izbor mernibroja',
                                command=lambda:izaberiumernibroj(eusl.get())
                                )
                        b4b5.pack(pady=5)
                        def izaberiumernibroj(usl):
                            global stan
                            global ulaz
                            global zgrada
                            global ulaz
                            global porodnos
                            global vlasnik
                            global mernibroj
                            global fizickavel
                            global iz_list
                            mernibroj=usl
                            if porodnos=='jednako':
                                por=1
                            if porodnos=='vece od':
                                por=2
                            if porodnos=='manje od':
                                por=3
                            mernibroj=usl
                            rez_df=A.podaci_zgrada_ID(zgrada)
                            if por==1:
                                iz_df=rez_df[rez_df.idzgrade==zgrada]
                                iz_df=iz_df[iz_df.brulaza==ulaz]
                                iz_df=iz_df[iz_df.loc[:,fizickavel] == int(mernibroj)]
                                iz_df=iz_df[iz_df.loc[:,fizickavel] != 0 ]
                            if por==2:
                                iz_df=rez_df[rez_df.idzgrade==zgrada]
                                iz_df=iz_df[iz_df.brulaza==ulaz]
                                iz_df=iz_df[iz_df.loc[:,fizickavel] > int(mernibroj)]
                                iz_df=iz_df[iz_df.loc[:,fizickavel] != 0 ]
                            if por==3:
                                iz_df=rez_df[rez_df.idzgrade==zgrada]
                                iz_df=iz_df[iz_df.brulaza==ulaz]
                                iz_df=iz_df[iz_df.loc[:,fizickavel] < int(mernibroj)]
                                iz_df=iz_df[iz_df.loc[:,fizickavel] != 0 ]
                            aaa=iz_df.loc[:,'idvlasnik']
                            iz_list=aaa.tolist()
                            b4b10=Button(rootb14,text='PRIKAZ LISTE REZULATA',command=lambda:[prikazlisterez(iz_list),rootb14.destroy()])
                            b4b10.pack(pady=10)
                            def prikazlisterez(lll):
                                rootrez=Toplevel(root)
                                rootrez.geometry('400x600')
                                global iz_list
                                print(iz_list)
                                l1=Label(rootrez,
                                         text='REZULTAT PRETRAGE JE'
                                         
                                         )
                                l1.pack()
                                list1 = StringVar(value=iz_list)
                                lst = Listbox(rootrez,listvariable=list1)
                                lst.pack(side=LEFT, fill=BOTH)

                                b1=Button(rootrez,text='Zatvoti prozor',command=lambda:rootrez.destroy())
                                b1.pack()


#================================================================================== Button 5
def buton51_podaci():
    rootb51=Toplevel(root)
    rootb51.geometry('1000x200')
    
    b5l1=Label(rootb51,text='IZABERITE STANARA ZA KOJEG SE TRAZE PODACI')
    b5l1.pack()
    
    clicked=StringVar()
    clicked.set('')
    drop=OptionMenu(
                    rootb51,
                    clicked,
                    *A.svistanari
                    )
    drop.pack(pady=5)

    b5b1=Button(
                rootb51,text='Izaberi stanara',
                command=lambda:izabranistanar(clicked.get())
                )
    b5b1.pack(pady=5)
    
    b5l1=Label(
                rootb51,text='',
                borderwidth=1,
                font=("Arial",12),
                bg="white",
                fg='green'
                )                         
    b5l1.pack(pady=20)

    b5b2=Button(
                rootb51,text='IZADJI',
                command=lambda:rootb51.destroy()
                )
    b5b2.pack(pady=5)

    def izabranistanar(stanar):                        
        aa=A.buton5(stanar)
        b5l1.config(text=aa)
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def dodajstanara():
    rootdodaj=Toplevel(root)
    rootdodaj.geometry('400x400')
    l1=Label(rootdodaj,text='Ime i prezime stanara')
    l1.grid(row=0,column=0,pady=5)
    l2=Label(rootdodaj,text='JMBG (13 brojeva)')
    l2.grid(row=1,column=0,pady=5)
    l3=Label(rootdodaj,text='Broj zgrade')
    l3.grid(row=2,column=0,pady=5)
    l4=Label(rootdodaj,text='Broj ulaza')
    l4.grid(row=3,column=0,pady=5)
    l5=Label(rootdodaj,text='Broj stana')
    l5.grid(row=4,column=0,pady=5)
    l6=Label(rootdodaj,text='Broj odraslih')
    l6.grid(row=5,column=0,pady=5)
    l7=Label(rootdodaj,text='Broj dece')
    l7.grid(row=6,column=0,pady=5)
    
    e1=Entry(rootdodaj)
    e1.grid(row=0,column=20,pady=5,padx=4)
    e2=Entry(rootdodaj)
    e2.grid(row=1,column=20,pady=5,padx=4)
    e3=Entry(rootdodaj)
    e3.grid(row=2,column=20,pady=5,padx=4)
    e4=Entry(rootdodaj)
    e4.grid(row=3,column=20,pady=5,padx=4)
    l8=Label(rootdodaj,text='')
    l8.grid(row=4,column=20,pady=5,padx=4)
    e6=Entry(rootdodaj)
    e6.grid(row=5,column=20,pady=5,padx=4)
    e7=Entry(rootdodaj)
    e7.grid(row=6,column=20,pady=5,padx=4)
    b1=Button(rootdodaj,text='Izbor praznog stana',
              command=lambda:odabirstana(e3.get(),e4.get()))
    b1.grid(row=7,column=0,pady=5)
    def odabirstana(szgrada,sulaz):
        global prazan
        A.prazan_stan(szgrada,sulaz)
        brstan=StringVar()
        brstan.set('')
        drop=OptionMenu(
                    rootdodaj,
                    brstan,
                    *A.prazni_stanovi
                    )
        drop.grid(row=8,column=0,pady=5)
        b2=Button(rootdodaj,text='Potvrdi',
                  command=lambda:
                  [l8.config(text=brstan.get()),
                   debrstan(brstan.get())]
                    )
                
        b2.grid(row=9,column=0,pady=5)
    def debrstan(cifra):
        global prazan
        prazan=cifra
    b3=Button(rootdodaj,text='DODAJ STANARA',
              command=lambda:dodaj_stanara()
              )   
    b3.grid(row=10,column=0,pady=5)
    def dodaj_stanara():
        global prazan
        A.bazastanara_svi_df.loc[len(A.bazastanara_svi_df.index)]=[e1.get(),int(e3.get()),int(e4.get()),prazan,e2.get(),int(e6.get()),int(e7.get())]
        ime=e1.get()
        zgrada=int(e3.get())
        ulaz=int(e4.get())
        stan=prazan
        jmbg=e2.get()
        odrasli=int(e6.get())
        deca=int(e7.get())
        A.dodaj_stanara_SQL(ime,zgrada,ulaz,stan,jmbg,odrasli,deca)
        pyg.alert('STANAR JE USPESNO DODAT!!!!')
        pyg.alert('VELJKO JE SRECAN JER KORISTIMO PYG!!!!')
        rootdodaj.destroy()
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def obrisistanara():
    rootbrisi=Toplevel(root)
    rootbrisi.geometry('800x200')
    l1=Label(rootbrisi,text='')
    l1.pack(pady=5)
    bimeprezime=StringVar()
    bimeprezime.set('')
    drop=OptionMenu(
                    rootbrisi,
                    bimeprezime,*A.svistanari
                    )
    drop.pack(pady=5)
    b2=Button(
            rootbrisi,text='Potvrdi izbor brisanja',command=lambda:izberistanara(bimeprezime.get())
            )
    b2.pack(pady=5)
    def izberistanara(imeprezime):
        stanarbrisi=imeprezime
        print(stanarbrisi)
        aa=A.brisanje_stanara_stanari_ID(stanarbrisi)
        print (aa)
        l1.config(text=aa)
        A.brisi_stanara_SQL(imeprezime)
        pyg.alert('STANAR JE USPESNO OBRISAN I IZVRSEN JE UPDATE SQL BAZE!!!!')
        rootbrisi.destroy()



def prosecna_cena_stana():
    jednosbni=0
    dvosobni=0
    trosobni=0
    cetvorosobni=0
    ostali=0
    aa=A.bazaulaz_svi_df.loc[A.bazaulaz_svi_df.loc[:,'brsoba']==1]
    jednosobni_df=aa.loc[:,'cena']
    p1=jednosobni_df.mean()
    aa=A.bazaulaz_svi_df.loc[A.bazaulaz_svi_df.loc[:,'brsoba']==2]
    dvosobni_df=aa.loc[:,'cena']
    p2=dvosobni_df.mean()
    aa=A.bazaulaz_svi_df.loc[A.bazaulaz_svi_df.loc[:,'brsoba']==3]
    trosobni_df=aa.loc[:,'cena']
    p3=trosobni_df.mean()
    aa=A.bazaulaz_svi_df.loc[A.bazaulaz_svi_df.loc[:,'brsoba']==4]
    cetvorosobni_df=aa.loc[:,'cena']
    p4=cetvorosobni_df.mean()
    aa=A.bazaulaz_svi_df.loc[A.bazaulaz_svi_df.loc[:,'brsoba']>4]
    ostali_df=aa.loc[:,'cena']
    p5=ostali_df.mean()
   
    plt.subplot(2,1,1)
    x=[1,2,3,4,5]
    y=[p1,p2,p3,p4,p5]
    plt.subplot(2,1,1)
    plt.bar(x,y,color='red',width=0.1)
    plt.show()

                    ##pip install matplotlib

def brojdece():
    d_df=A.bazastanara_svi_df.loc[:,'brdeca']
    d=len(d_df)
    aa=A.bazastanara_svi_df.loc[A.bazastanara_svi_df.loc[:,'brdeca']==0]
    d0_df=A.bazastanara_svi_df.loc[:,'brdeca']
    d0=len(d0_df)
    aa=A.bazastanara_svi_df.loc[A.bazastanara_svi_df.loc[:,'brdeca']==1]
    d1_df=aa.loc[:,'brdeca']
    d1=len(d1_df)
    aa=A.bazastanara_svi_df.loc[A.bazastanara_svi_df.loc[:,'brdeca']==2]
    d2_df=aa.loc[:,'brdeca']
    d2=len(d2_df)
    aa=A.bazastanara_svi_df.loc[A.bazastanara_svi_df.loc[:,'brdeca']==3]
    d3_df=aa.loc[:,'brdeca']
    d3=len(d3_df)
    aa=A.bazastanara_svi_df.loc[A.bazastanara_svi_df.loc[:,'brdeca']==4]
    d4_df=aa.loc[:,'brdeca']
    d4=len(d4_df)
    aa=A.bazastanara_svi_df.loc[A.bazastanara_svi_df.loc[:,'brdeca']>4]
    d5_df=aa.loc[:,'brdeca']
    d5=len(d5_df)
    
    p0=d0/d*100
    print(p0)

    p1=d1/d*100
    print(p1)

    p2=d2/d*100
    print(p2)

    p3=d3/d*100
    print(p3)

    p4=d4/d*100
    print(p4)

    p5=d5/d*100
    print(p5)


    l=[p0,p1,p2,p3,p4,p5]
    l1=['Bez dece','Jedno dete','Dva deteta',
        'Tri deteta','Cetiri deteta','Vise od 4 deteta']
    e=[0.2,0.1,0.3,0.5,0.1,0.1]
    plt.figure(figsize=(10,6))
    plt.pie(l,labels=l1,explode=e,autopct='%1.1f%%')
    plt.legend(title="My legend:",loc='upper right')
    plt.show()

def odjavna_poruka():
    sg.theme('DarkAmber') 
    layout = [  [sg.Text('Ko je najbolji nastavnik')],
                [sg.Text('Ime najboljeg nastavnika je'), sg.InputText()],
                [sg.OK()]]

    window = sg.Window('Window Title', layout)
    while True:             
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'OK'):
            break

    window.close()






menubar = Menu()

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="DODAJ STANARA", command=lambda: dodajstanara())
filemenu.add_command(label="IZBRISI STANARA", command=lambda: obrisistanara())
menubar.add_cascade(label="ADMINISTRACIJA", menu=filemenu)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="PROSECNA CENA STANA PREMA BROJU SOBA",command=lambda:prosecna_cena_stana())
filemenu.add_command(label="PROCENAT BROJA DECE PO PO STANU",command=lambda:brojdece())
menubar.add_cascade(label="GRAFICKI PRIKAZ", menu=filemenu)



exit_menu = Menu(menubar, tearoff=0)
exit_menu.add_command(label="UPDATE", command=lambda:[A.export_excel(),pyg.alert('NASTAVNIK JE CAR NAJVECI ! ! ! !')])
exit_menu.add_command(label="Izlaz", command=lambda: [odjavna_poruka(),root.destroy()])
menubar.add_cascade(label="Exit", menu=exit_menu)

root.config(menu=menubar)


root.mainloop()