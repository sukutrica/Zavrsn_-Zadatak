import pandas as pd
import psycopg2 as pg
import pyautogui as pyg
import openpyxl as openpyxl
from numpy.random import randint
from sqlite3 import * 


class Admin_zgrade:
        def __init__ (self):
                self.con=pg.connect(
                        database='ZAVRSNI1',
                        user='postgres', 
                        password='Trade2004', 
                        host='localhost', 
                        port='5432'
                        )
                self.baza_sve_df=None
        def ucitaj_bazu(self):
                self.baza_sve_df=pd.read_sql_query('SELECT S.IDVLASNIK, S.JMBG, U.SPRAT,S.BRSTANA, U.CENA, U.POVRSINA,S.BRODRASLI, S.BRDECA, U.BRULAZA, Z.ADRESA,Z.IDZGRADE, Z.OPSTINA FROM ZGRADA Z, ULAZ U, STANARI S WHERE Z.IDZGRADE=U.IDZGRADE AND U.BRULAZA=S.BRULAZA AND S.BRULAZA=U.BRULAZA AND S.BRSTANA=U.BRSTANA AND S.IDZGRADE=Z.IDZGRADE'
                                                       ,self.con
                                                       )
                self.bazastanara_svi_df=pd.read_sql_query('SELECT * FROM STANARI',self.con)
                self.svistanari=self.bazastanara_svi_df.loc[:,'idvlasnik']
                aa=self.svistanari
                self.svistanari=aa.tolist()
                filename='StanariBaza.xlsx'
                
                self.bazastanara_svi_df.to_excel(filename)
                self.bazazgrada_svi_df=pd.read_sql_query('SELECT * FROM ZGRADA',self.con)
                self.lista_zgrada = []                                                                   #     prebacuje elemente DataFrame u listu
                for i in self.bazazgrada_svi_df:
                        l = self.bazazgrada_svi_df[i].tolist()
                        self.lista_zgrada.append(l)                                                   # jedan nacin vraca liste redova iy DF
                print(self.lista_zgrada)
                filename='ZgradaBaza.xlsx'
                self.bazazgrada_svi_df.to_excel(filename)
                
                self.bazaulaz_svi_df=pd.read_sql_query('SELECT * FROM ULAZ',self.con)
                self.ulazi=pd.read_sql_query('SELECT BRULAZA FROM ULAZ',self.con)
                self.ulazi.drop_duplicates(inplace=True)
                self.lista_ulazi = []                                                                   #     prebacuje elemente DataFrame u listu
                for i in self.ulazi:
                        l = self.ulazi[i].tolist()
                        self.lista_ulazi.append(l)
                self.bazaulaz_1_df=pd.read_sql_query('SELECT BRULAZA FROM ULAZ WHERE IDZGRADE = 1 GROUP BY BRULAZA',self.con)
                self.ulazi1=pd.read_sql_query('SELECT BRULAZA FROM ULAZ WHERE IDZGRADE=1 GROUP BY BRULAZA',self.con)
                self.ulazi1.drop_duplicates(inplace=True)
                self.lista_ulazi1 = []                                                                   #     prebacuje elemente DataFrame u listu
                for i in self.ulazi1:
                        l = self.ulazi1[i].tolist()
                        self.lista_ulazi1.append(l)
                        self.lista_ulazi1=self.lista_ulazi1[0]
                self.bazaulaz_2_df=pd.read_sql_query('SELECT BRULAZA FROM ULAZ WHERE IDZGRADE = 2 GROUP BY BRULAZA',self.con)
                self.ulazi2=pd.read_sql_query('SELECT BRULAZA FROM ULAZ WHERE IDZGRADE = 2 GROUP BY BRULAZA',self.con)
                self.ulazi2.drop_duplicates(inplace=True)
                self.lista_ulazi2 = []                                                                   #     prebacuje elemente DataFrame u listu
                for i in self.ulazi2:
                        l = self.ulazi2[i].tolist()
                        self.lista_ulazi2.append(l)
                        self.lista_ulazi2=self.lista_ulazi2[0]



        def dodaj_stanara_SQL(self,vlasnik,zgrada,ulaz,stan,jmbg,odrasli,deca):
                cursor=self.con.cursor()
                d='''INSERT INTO STANARI (IDVLASNIK,IDZGRADE,BRULAZA,BRSTANA,JMBG,BRODRASLI,BRDECA) VALUES ('{}',{},{},'{}',{},{},{});'''.format(vlasnik,zgrada,ulaz,stan,jmbg,odrasli,deca)
                cursor.execute(d)
                self.con.commit()
                cursor.close()
                A.ucitaj_bazu()
                pyg.alert('SQL TABELA JE UPDATOVANA')






        def brisi_stanara_SQL(self,stanar):
                cursor=self.con.cursor()
                u='''DELETE FROM STANARI WHERE IDVLASNIK='{}';'''.format(stanar)
                cursor.execute(u)
                self.con.commit()
                cursor.close()
                A.ucitaj_bazu()
                pyg.alert('SQL TABELA JE UPDATOVANA')





        def zatvori_konekciju(self):
                self.con.close()

        def lista_stana(self,ulazbr,zgradabr):
                self.lista_stanova_df=pd.read_sql_query('''SELECT * FROM ULAZ WHERE BRULAZA='{}' AND IDZGRADE='{}' '''.format(ulazbr,zgradabr),self.con)
                self.ulaz_lista=[]
                for i in self.lista_stanova_df:
                        l = self.lista_stanova_df[i].tolist()
                        self.ulaz_lista.append(l)
                self.brojevi_stanova=self.ulaz_lista[3]
                return self.brojevi_stanova

        def export_excel (self):
                filename='StanariBaza.xlsx'
                self.bazastanara_svi_df.to_excel(filename)
                filename='StanariBaza.txt'
                self.bazastanara_svi_df.to_csv(filename)                
                filename='ZgradaBaza.xlsx'
                self.bazazgrada_svi_df.to_excel(filename)
                filename='ZgradaBaza.txt'
                self.bazazgrada_svi_df.to_csv(filename)
                filename='UlazBaza.xlsx'
                self.bazaulaz_svi_df.to_excel(filename)
                filename='UlazBaza.txt'
                self.bazaulaz_svi_df.to_csv(filename)


# pravi listu praznih stanova
        def prazan_stan(self,brojzgrade,brojulaza):
                A.export_excel()
                self.stan_baza_ulaz_df=self.bazaulaz_svi_df.loc[
                        self.bazaulaz_svi_df.loc[:,'idzgrade']==int(brojzgrade)
                        ]
                
                self.stan_baza_ulaz_df=self.stan_baza_ulaz_df.loc[
                        self.stan_baza_ulaz_df.loc[:,'brulaza']==int(brojulaza)
                        ]
                self.stan_baza_ulaz_df=self.stan_baza_ulaz_df.loc[
                        :,'brstana'
                        ]
                self.stan_baza_ulaz_list=self.stan_baza_ulaz_df.tolist()
#----------------------------------------------------------------------------
                self.stanari_baza_ulaz_df=self.bazastanara_svi_df.loc[
                        self.bazastanara_svi_df.loc[:,'idzgrade']==int(brojzgrade)
                        ]
                self.stanari_baza_ulaz_df=self.stanari_baza_ulaz_df.loc[
                        self.stanari_baza_ulaz_df.loc[:,'brulaza']==int(brojulaza)
                        ]
                self.stanari_baza_ulaz_df=self.stanari_baza_ulaz_df.loc[
                        :,'brstana'
                        ]
                self.stanari_baza_ulaz_list=self.stanari_baza_ulaz_df.tolist()
                self.prazni_stanovi=[]
                for i in self.stan_baza_ulaz_list:
                        if i in self.stanari_baza_ulaz_list:
                                pass
                        else:
                                self.prazni_stanovi.append(i)
                return(self.prazni_stanovi)
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        def podaci_zgrada_ID(self,idzgradebr):            # podaci o zgradi prema ID
                #print(idzgradebr,'+-+-+')
                self.stanari_zgrade_df=self.baza_sve_df[self.baza_sve_df.idzgrade==idzgradebr]
                return self.stanari_zgrade_df

        def podaci_zgrada_ulaz(self,uslov1,uslov2,brzgrade,brulaz):
                self.zgrada_ulaz_df=self.baza_sve_df[(self.baza_sve_df[uslov1]==brzgrade) & (self.baza_sve_df[uslov2]==brulaz)]
                    #print(self.zgrada_ulaz_df)

        def podatak_zgrade_ulaz(self,brzgrada,brlamela,uslov1,krit1,kontrola):
                # print(krit1,'  krit1')
                # print(kontrola,'  kontrola')
                if kontrola=='jednako':
                        self.podatak_zgrada_df=self.stanari_zgrade_df[self.stanari_zgrade_df.idzgrade==brzgrada]
                        self.podatak_zgrada_df=self.stanari_zgrade_df[self.stanari_zgrade_df.brulaza==brlamela]
                        self.podatak_zgrada_df=self.stanari_zgrade_df[self.stanari_zgrade_df[uslov1]==krit1]
                        self.podatak_zgrada_df=self.podatak_zgrada_df[self.podatak_zgrada_df[uslov1]!=0]
                        ##print(self.podatak_zgrada_df,'1')
                        return
                if kontrola=='vece od':
                        self.podatak_zgrada_df=self.stanari_zgrade_df[self.stanari_zgrade_df.idzgrade==brzgrada]
                        self.podatak_zgrada_df=self.stanari_zgrade_df[self.stanari_zgrade_df.brulaza==brlamela]
                        self.podatak_zgrada_df=self.stanari_zgrade_df[self.stanari_zgrade_df[uslov1]>krit1]
                        self.podatak_zgrada_df=self.podatak_zgrada_df[self.podatak_zgrada_df[uslov1]!=0]
                        ##print(self.podatak_zgrada_df,'2')
                        return
                else:
                        self.podatak_zgrada_df=self.stanari_zgrade_df[self.stanari_zgrade_df.idzgrade==brzgrada]
                        self.podatak_zgrada_df=self.stanari_zgrade_df[self.stanari_zgrade_df.brulaza==brlamela]
                        self.podatak_zgrada_df=self.stanari_zgrade_df[self.stanari_zgrade_df[uslov1]<krit1]
                        self.podatak_zgrada_df=self.podatak_zgrada_df[self.podatak_zgrada_df[uslov1]!=0]
                        ##print(self.podatak_zgrada_df,'3')
                        return
                        
        def buton1(self,kriterijum1,uslov1,kriterijum2,uslov2,kriterijum3,uslov3):                  #       Prikaz stanara prema izboru lamele i stana 
                self.buton1_df = self.baza_sve_df[(self.baza_sve_df[kriterijum1]==uslov1)
                                                    &(self.baza_sve_df[kriterijum2]==uslov2)
                                                    &(self.baza_sve_df[kriterijum3]==uslov3)
                                                    ]
                        #print(self.buton1_df)  
                self.lista = []                                                                   #     prebacuje elemente DataFrame u listu
                for i in self.buton1_df:
                        l = self.buton1_df[i].tolist()
                        #self.lista.append(self.buton1_df[i].tolist())                            # vraca listu lista
                        self.lista.append(l[0])                                                   # jedan nacin vraca liste redova iy DF
                        #self.lista.append(l)                                                         # drugi nacin vraca listu lista
                a=self.lista[0]
                b=self.lista[1]
                self.rezultat='Ime stanara je: '+a+', JMBG stanara je: '+b
                return self.rezultat

        def buton2 (self,kriterijum1,uslov1,kriterijum2,uslov2,kriterijum3,uslov3):                 #       Prikaz broja članova domaćinstva
                A.buton1(kriterijum1,uslov1,kriterijum2,uslov2,kriterijum3,uslov3)
                self.vlasnik=self.lista[0]
                self.odrasli=self.lista[6]
                self.deca=self.lista[7]
                self.brojclanova='Vlasnik stana je '+self.vlasnik+'. Broj draslih je: '+ str(self.odrasli) +'. Broj dece je: '+str(self.deca)
                ##print(self.brojclanova)
                return(self.brojclanova)
            
        def buton3 (self,kriterijum1,uslov1,kriterijum2,uslov2,kriterijum3,uslov3):                 #       Vrednost izabranog stana
                A.buton1(kriterijum1,uslov1,kriterijum2,uslov2,kriterijum3,uslov3)
                self.vlasnik=self.lista[0]
                self.cena=self.lista[4]
                self.cenastana_rez='Vlasnik stana je: '+self.vlasnik+'. Vrednost stana je '+str(self.cena)+' evra.'
                return self.cenastana_rez


        def buton4 (self,zgrada,lamela,sprat,povrsina_cena,kriterijum,uslov):                 #       Lista vlasnika stana prema kriterijumu sprata, lamele ili veličine stana
                self.buton4_df = self.baza_sve_df[(self.baza_sve_df.idzgrade==zgrada)
                                                    &(self.baza_sve_df.brulaza==lamela)
                                                    ]
                A.podaci_zgrada_ID(zgrada)
                A.podatak_zgrade_ulaz(zgrada,lamela,povrsina_cena,kriterijum,uslov)
                self.buton_4=self.podatak_zgrada_df
                self.buton_4=self.buton_4['idvlasnik']
                self.buton4_lista=self.buton_4.tolist()
                ##print(self.buton4_lista)




        def buton5 (self,imeprezime):                                                               #       Pretraga baze prema kriterijumu: ime prezime sa prikazom podataka
                self.vlasnik_df=self.baza_sve_df[self.baza_sve_df.idvlasnik==imeprezime]
                self.vlista=[]
                for i in self.vlasnik_df:
                                self.vlista.append(self.vlasnik_df[i].tolist()[0]) 
                self.rezultat='Ime i prezime: ' + self.vlista[0] + ', JMBG: ' + self.vlista[1] + ', adresa: '+self.vlista[9]+', br. ulaza '+str(self.vlista[8])+', opstina '+str(self.vlista[11])
                return self.rezultat
        
        def brisanje_stanara_stanari_ID(self,imeprezime):            # podaci o zgradi prema ID
                file_name='Podaci.xlsx'
                self.baza_sve_df.to_excel(file_name)
                self.brisi_stanara_df=self.baza_sve_df[self.baza_sve_df.idvlasnik == imeprezime]
                a=len(self.brisi_stanara_df.index)              # vraca broj redova DF
                if a==1:
                        self.baza_sve_df=self.baza_sve_df[self.baza_sve_df.idvlasnik != imeprezime]
                        self.bazastanara_svi_df=self.bazastanara_svi_df[self.bazastanara_svi_df.idvlasnik != imeprezime]
                        file_name='Podaci1.xlsx'
                        self.brisi_stanara_df.to_excel(file_name)
                        file_name='Podaci1.xlsx'
                        self.baza_sve_df.to_excel(file_name)
                        A.export_excel()
                        return 'Stanar ' +imeprezime+' je uspesno obrisan i izvrsen je export u xlsx bazu'
                else:
                        return 'Postoji vise stanara sa izabranim imenom ili ne postoji stanar sa unetim imenom'
               
        def promena_vlasnika(self,zgrada,ulaz,stan,ime_prezime,JMBG,odrasli,deca):
                stanar=self.bazastanara_svi_df[(self.bazastanara_svi_df.brstana==stan)
                                                                &(self.bazastanara_svi_df.brulaza==ulaz)
                                                                &(self.bazastanara_svi_df.idzgrade==zgrada)]
                a=stanar.loc[:,'idvlasnik']
                b=a.tolist()[0]
                ##print(b)
                stanar=self.bazastanara_svi_df[(self.bazastanara_svi_df.brstana!=stan)
                                               &(self.bazastanara_svi_df.idvlasnik!=b)]
                
                list_row=[ime_prezime,zgrada,ulaz,stan,JMBG,odrasli,deca]
                stanar.loc[len(self.bazastanara_svi_df)] = list_row
                self.bazastanara_svi_df=stanar
                A.export_excel ()

        def brisanje_stanara_brzo(self,stanar):
                stanari=self.bazastanara_svi_df.loc[self.bazastanara_svi_df['idvlasnik']!=stanar]
                self.bazastanara_svi_df=stanari
                A.export_excel ()
                ##print(stanari)

        def promena_broja_stanara(self,ime,odrasli,deca):
                if ime not in self.bazastanara_svi_df:
                        print('Stanar ne postoji. Proverite unos!!!')
                        return 'Stanar ne postoji'
                stanar=self.bazastanara_svi_df[self.bazastanara_svi_df.idvlasnik==ime]
                stanar.loc[:,'brodrasli']=odrasli
                stanar.loc[:,'brdeca']=deca
                ##print(stanar,'rezultat')
                aa=stanar.values.tolist()
                ##print(aa,'test')
                stanar2=self.bazastanara_svi_df[self.bazastanara_svi_df.idvlasnik!=ime]
                ##print(stanar2)
                cc=len(self.bazastanara_svi_df)

                stanar2.loc[cc]=aa[0]
                self.bazastanara_svi_df=stanar2
                ##print(self.bazastanara_svi_df)
                A.export_excel ()

        def ispis_zgrade(self):
                self.ispis_z=[]
                aa=''
                bb=''
                for i in self.lista_zgrada:
                        aa=aa+'|'+str(i[0])
                        bb=bb+'|'+str(i[1])
                self.ispis_z=[aa,bb]


A=Admin_zgrade()
A.ucitaj_bazu()
##print(A.lista_stana(1,1))
A.export_excel()
#print(A.baza_sve_df)
#A.podaci_zgrada_ID(1)
#A.podatak_zgrade_ulaz(1,1,'cena',10000,'vece od')
#print(A.buton1('idzgrade',1,'brulaza',2,'brstana',11))
#print(A.buton2('idzgrade',1,'brulaza',1,'brstana',12))
#print(A.buton3('idzgrade',1,'brulaza',1,'brstana',11))
#A.buton4(1,1,3,'povrsina',50,'vece od')
#A.buton5('Jovana Simic')
#A.brisanje_stanara_stanari_ID('Bruce Lee')
#A.update_SQL()
#A.promena_vlasnika(1,1,11,'Vasilije Danilovic','555555555555555',2,5)
#A.brisanje_stanara_brzo('Vasilije Danilovic')
#A.promena_broja_stanara('Milica Mulj',10,6)
#print(A.prazan_stan(2,1))
#print(A.lista_zgrada)
#A.ispis_zgrade()
