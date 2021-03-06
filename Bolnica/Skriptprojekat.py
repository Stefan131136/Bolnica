# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 19:13:33 2020

@author: Stefan Kalafatic
"""
class Lekar:
    
    
    
    def __init__(self, ime, prezime, lozinka):
        self.ime = ime
        self.prezime = prezime
        self.spisak_zakazanih_pregleda = []
        self.lozinka = lozinka
        self.lista_pacijenata = []
        
    
    def loadLekar(self,ime,prezime):
        import os
        self.spisak_zakazanih_pregleda.clear()
        self.lista_pacijenata.clear()
        ok = os.stat(ime + prezime + "_lista_pacijenata.txt").st_size == 0
        if(ok):
            pass
        else:
            fajl = open(ime + prezime + "_lista_pacijenata.txt","r")
            for line in fajl.readlines():
                if(line == "\n"):
                    continue
                s = line.strip().split("|")
                self.lista_pacijenata.append(self.pomocna(s[0], s[1], s[2]))
                f = open(s[0] + s[1] + ".txt", "r")
                linija = f.readlines()
                for i in linija:
                    p = i.strip().split("|")
                    self.spisak_zakazanih_pregleda.append(self.pomocna2(s[0], s[1], s[2], p[2], p[3], p[4]))

                
                    
    
    
    def pomocna2(self, ime, prezime, jmbg, datum, vreme, cena):
        recnik = {}
        recnik["Ime"] = ime
        recnik["Prezime"] = prezime
        recnik["Jmbg"] = jmbg
        recnik["Datum"] = datum
        recnik["Vreme"] = vreme
        recnik["Cena"] = cena
        return recnik
    
    
    def pomocna(self, ime, prezime, jmbg):
        recnik = {}
        recnik["Ime"] = ime
        recnik["Prezime"] = prezime
        recnik["Jmbg"] = jmbg
        return recnik
        
    def dodavanje_pacijenta(self):
        import os
        
        ime = input("Unesite ime pacijenta: ")
        prezime = input("Unesite prezime pacijenta: ")
        jmbg = input("Unesite jmbg pacijenta: ")
        ime = ime.capitalize()
        prezime = prezime.capitalize()
        
        ok = os.stat(self.ime + self.prezime + "_lista_pacijenata.txt").st_size == 0
        if(ok):
            fajl = open(self.ime + self.prezime + "_lista_pacijenata.txt","a")
            fajl.write(ime +"|" + prezime  +"|"+ jmbg + "|"  + "\n")
            f = open(ime+prezime + ".txt","w+")
            f.close()
            fajl.close() 
            self.lista_pacijenata.append(self.pomocna(ime,prezime,jmbg))
            return True
        fajl = open(self.ime + self.prezime + "_lista_pacijenata.txt","r")
        lines = fajl.readlines()
        for line in lines:
                if(line == "\n"):
                    continue
                s = line.strip().split("|")
                if (ime == s[0]) and (s[1] == prezime) and (s[2] == jmbg):
                    print("Pacijent vec postoji! ")
                    ok = True 
                    break 
        if(ok != True):
            fajl = open(self.ime + self.prezime + "_lista_pacijenata.txt","a")
            fajl.write(ime +"|" + prezime  +"|"+ jmbg + "\n")
            f = open(ime+prezime + ".txt","w+")
            f.close()
            fajl.close() 
            self.lista_pacijenata.append(self.pomocna(ime,prezime,jmbg))
            print()
            print("??ifra Va??eg pacijenta je njegov jmbg, a username - " + ime + prezime)
            return True

        
    def zakazivanje_pregleda(self,datum,vreme):
        ime = input("Unesite ime pacijenta: ")
        ime = ime.replace(" ","")
        prezime = input("Unesite prezime pacijenta: ")
        prezime = prezime.replace(" ","")
        ok = True
        for d in self.lista_pacijenata: 
           i = d.get('Ime')
           p = d.get('Prezime')
           if((i == ime) and (p == prezime)):
               d["Datum"] = datum
               d["Vreme"] = vreme
               d["Cena"] = input("Unesite cenu pregleda")
               fajl = open(self.ime + self.prezime + "_lista_pregleda", "a")
               fajl.write(ime + "-" + prezime + "|" + datum + "|" + vreme)
               fajl.close()
               self.spisak_zakazanih_pregleda.append(d)
               f = open(ime + prezime + ".txt", "a")  
               f.write(self.ime +"|" + self.prezime  +"|"+ str(datum) + "|" + str(vreme) + "|" + d["Cena"] + "\n")
               f.close()
               ok = False
        if(ok):
            print("Molimo prvo dodajte pacijeta, pa onda zakazite pregled.")
        
        
    
    
    def stampaj_spisakk_pregleda(self):
        import datetime
        g = eval(input("Za koju godinu zelite da proverite preglede? "))
        m = eval(input("Za koji mesec zelite da proverite preglede? "))
        d = eval(input("Za koji dan zelite da proverite preglede? "))
        d = datetime.date(g, m, d)
        d = str(d)
        for n in self.spisak_zakazanih_pregleda:
            print(n.get("Datum"))
            print(d)
            if(n.get("Datum") == d):
                print(n.get("Ime") + n.get("Prezime") + ": " + str(n.get("Datum")) + "-" + str(n.get("Vreme")))

    def stampaj_spisak_svih_pregleda(self):
        ok = True
        for n in self.spisak_zakazanih_pregleda:
            print(n.get("Ime") + n.get("Prezime") + ": " + str(n.get("Datum")) + "-" + str(n.get("Vreme")))
            ok = False
        if(ok):
            print("Trenutno nema zakazanih pregleda.")

    def postavi_dijagnozu(self):
        ime = input("Unesite ime pacijenta: ")
        ime = ime.replace(" ","")
        prezime = input("Unesite prezime pacijenta: ")
        prezime = prezime.replace(" ","")
        ok = True
        for d in self.spisak_zakazanih_pregleda:
            i = d.get('Ime')
            p = d.get('Prezime')
            if((i == ime) and (p == prezime)):
                dijagnoza = input("Unesite dijagnozu pacijenta: ")
                d["Dijagnoza"] = dijagnoza 
                ok = False
                break
        if(ok):
            print("Ne postoji uneti pacijent!")
            
            
    def stampaj_pacijente_sa_dijagnozama(self):
        for d in self.spisak_zakazanih_pregleda:
            ime = d.get('Ime')
            prezime = d.get('Prezime')
            print (ime + prezime + " : %s" %  d.get('Dijagnoza'))
            
            
    

    
    
                         
class Pacijent:
    
    
    def __init__(self, ime, prezime, jmbg):
        self.ime = ime
        self.prezime = prezime
        self.jmbg = jmbg
        self.lista_pregleda = []
        
    def stampaj_listu_pregleda(self):
        f = open(self.ime + self.prezime + ".txt", "r")
        for line in f.readlines():
            print(line)
        f.close()


class Admin:
    
    
    lista_lekara = []

        
        
    def dodavanje_lekara(self):
        from random import randrange

        rand = randrange(999, 10000)
        
        ime = input("Unesite ime lekara: ")
        prezime = input("Unesite prezime lekara: ")
        ime = ime.capitalize()
        prezime = prezime.capitalize()
        s = ime + "-" + prezime
        ok = False
        for i in self.lista_lekara:
            if(s == i):
                ok = True
            else:
                continue
        if(ok):
            print("Lekar sa tim imenom vec postoji.")
        else:
            fajl = open(ime + prezime + "_lista_pregleda.txt","w+")
            fajl.close()
            
            fajl = open(ime + prezime + "_lista_pacijenata.txt","w+")
            fajl.close()
            
            
            fajl = open("Lista lekara.txt","a")
            fajl.write("\n" + ime + prezime  +"|"+ str(rand) +  "\n")
            fajl.close()
            print()
            print("??ifra Va??eg lekara je " + str(rand) + ", a username - " + ime + prezime)
            self.lista_lekara.append(str(s))
    

    def stampanje_liste_lekara(self):
        for n in self.lista_lekara:
            print(n)
    
    
    def brisanje_lekara(self):
        import os
        ime = input("Unesite kog lekara ??elite da otpustite ")
        ime = ime.replace(" ", "")
        


        for n in self.lista_lekara:
            sp = n.split("-")
            if((sp[0] + sp[1]) == ime):
                if os.path.exists(ime + "_lista_pregleda.txt"):
                    os.remove(ime + "_lista_pregleda.txt")
                if os.path.exists(ime + "_lista_pacijenata.txt"):
                    f = open(ime + "_lista_pacijenata.txt", "r")
                    for line in f.readlines():
                        s = line.strip().split("|")
                        if os.path.exists(ime + "_lista_pacijenata.txt"):
                            os.remove(s[0] + s[1] + ".txt")
                    f.close()
                    os.remove(ime + "_lista_pacijenata.txt")
                    self.lista_lekara.remove(n)
            self.brisanje_lekara_iz_fajla(ime)
    
        
        
    def brisanje_lekara_iz_fajla(self,ime):
        
        fajl = open("Lista lekara.txt", "r")
        lines = fajl.readlines()
        fajl.close()
        
        novi_fajl = open("Lista lekara.txt", "w")
        
        for line in lines:
            if ime not in line.strip("123456789|\n"):
                novi_fajl.write(line)
        print("Lekar otpu??ten!")
        novi_fajl.close()
        
       
            
    def stampanje_liste_lekara_sa_siframa(self):
        lista_lekara = open("Lista lekara.txt" , "r")
        for linija in lista_lekara:
            strip_linija = linija.strip()
            print(strip_linija)
        lista_lekara.close()
        
        
        
    

    def loadAdmin(self):
        import re
        self.lista_lekara.clear()
        fajl = open("Lista lekara.txt","r")
        for line in fajl.readlines():
            if(line == "\n"):
                    continue
            if("|" not in line):
                continue
            s = line.strip().split("|")
            user = s[0]
            lista = re.findall('[A-Z][^A-Z]*', user)
            lista[1] = lista[1].split("|")
            self.lista_lekara.append(str(lista[0] + "-" +  lista[1][0]))
        fajl.close() 


    def grafik(self):
        import matplotlib.pyplot as plt
        x_podaci = []
        y_podaci = []
        f = open("Lista lekara.txt", "r")
        for line in f.readlines():
            if(line == "\n"):
                continue
            s = line.strip().split("|")
            x_podaci.append(s[0])
            fajl = open(s[0] + "_lista_pacijenata.txt","r")
            lista = fajl.readlines()
            y_podaci.append(len(lista))
            fajl.close()
        plt.bar(x_podaci, y_podaci)
        plt.xlabel('Lekari')
        plt.xticks(rotation=90)
        plt.ylabel('Broj pacijenata po lekaru')
        plt.ylim(ymin=1, ymax=10)
        plt.show()    
    
    

def login(s):    
        import getpass
        import os
        import os.path
        from os import path
        if(s == 'a'):
            user = input("Username: ")
            passw = getpass.getpass("Password: ")
            f = open("users.txt", "r")
            for line in f.readlines():
                if("|" not in line):
                    continue
                us, pw = line.strip().split("|")
                if (user == us) and (passw == pw):
                    print("Login successful!")
                    return True, user, passw
            print ("Wrong username/password")
            return False, '', ''
        elif(s == 'l'):
            user = input("Username: ")
            passw = getpass.getpass("Password: ")
            f = open("Lista lekara.txt", "r")
            if(os.stat("Lista lekara.txt").st_size == 0):
                print("Ne postoje zaposleni lekari! ")
                return False, '', ''
            for line in f.readlines():
                if(line == "\n"):
                    continue
                if("|" not in line):
                    continue
                us, pw = line.strip().split("|")
                if (user == us) and (passw == pw):
                    print("Login successful!")
                    return True, user, passw
                    break   
            print ("Wrong username/password")
            return False, '', ''
        elif(s == 'p'):
            user = input("Username: ")
            passw = getpass.getpass("Password: ")
            
            if not path.exists(user + ".txt"):
                print("Ne postoji pacijent sa imenom: " + user)
                return False, '', ''
            else:
                lekarime = input("Ime Va??eg lekara: ")
                lekarpre = input("Prezime Va??eg lekara: ")
                if not (path.exists(lekarime + lekarpre + "_lista_pacijenata.txt")):
                    print("Ne postoji uneti lekar.")
                    return False, '', ''
                else:
                    f = open(lekarime + lekarpre + "_lista_pacijenata.txt", "r")
                    if(os.stat(lekarime + lekarpre + "_lista_pacijenata.txt").st_size == 0):
                        print("Ne postoje pacijenti! ")
                        return False, '', ''
                    for line in f.readlines():
                        if("|" not in line):
                            continue
                        if(line == "\n"):
                            continue
                        s = line.strip().split("|")
                        if (user == s[0] + s[1]) and (passw == s[2]):
                            print("Login successful!")
                            return True, user, passw
                        break            
                    print ("Wrong username/password")
                    return False, '', ''
        elif(s=='k'):
            return False , '', ''
        else:
            return False , '', ''
        
        
            
def menu1():

        print("Dobrodo??li! Admin")
        br = 99
        a = Admin()
        a.loadAdmin()
        while(br!='10'):         
            print(" 1 - Dodajte/Zaposlite lekara\n 2 - ??tampajte listu lekara\n 3 - Obri??ite lekara\n 4 - ??tampajte liste lekara sa ??iframa\n 5 - ??tampajte grafik\n 6 - Logout\n")  
            br = input("Unesite va??u opciju: ")
            if(br == '1'):
                a.dodavanje_lekara()
            elif(br == '2'):
                a.stampanje_liste_lekara()
            elif(br == '3'):
                a.brisanje_lekara()
            elif(br == '4'):
                a.stampanje_liste_lekara_sa_siframa()
            elif(br == '5'):
                a.grafik()
            elif(br == '6'):
                print("Odlogovani ste!")
                br = '10'
                logout()
            else:
                print("Pogresan unos, molimo pokusajte ponovo!")
                br = '99'
                

                
        
                

def menu2(user,passw):
        import re
        import datetime
        lista = re.findall('[A-Z][^A-Z]*', user)
        lista[1] = lista[1].split("|")
        l = Lekar(lista[0],lista[1][0],passw)
        l.loadLekar(lista[0],lista[1][0])
        print("Dobrodo??li! ")
        br = '99'
        while(br!='10'):

            print("1 - Dodajte pacijenta\n 2 - Zaka??ite pregled\n 3 - ??tampaj spisak za neki datum pregleda\n 4 - ??tampaj spisak svih pregleda\n 5 - Postavi dijagnozu za pacijenta\n 6 - ??tampaj pacijente sa dijagnozama\n 7 - Logout")  
            br = input("Unesite va??u opciju: ")
            if(br == '1'):
                l.dodavanje_pacijenta()
            elif(br == '2'):
                ok = False
                while(ok == False):
                    g = eval(input("Unesite godinu: "))
                    m = eval(input("Unesite mesec(Bez 0!): "))
                    d = eval(input("Unesite dan: "))
                    datum = datetime.date(g,m,d)
                    h = eval(input("Unesite sat(Bez 0!): "))
                    mi = eval(input("Unesite minut(Bez 0!): "))
                    vreme = datetime.time(h,mi)
                    ok = l.zakazivanje_pregleda(datum,vreme)
            elif(br == '3'):
                l.stampaj_spisakk_pregleda()
            elif(br == '4'):
                l.stampaj_spisak_svih_pregleda()
            elif(br == '5'):
                l.postavi_dijagnozu()
            elif(br == '6'):
                l.stampaj_pacijente_sa_dijagnozama()
            
            elif(br == '7'):
                print("Odlogovani ste!")
                br = '10'
                logout()
            else:
                print("Pogresan unos, molimo pokusajte ponovo!")
                br = '99'
     
          
def menu3(user,passw):
        import re
        lista = re.findall('[A-Z][^A-Z]*', user)
        lista[1] = lista[1].split("|")
        l = Pacijent(lista[0],lista[1][0],passw)
        
        print("Dobrodo??li! ")
        br = '99'
        while(br!='10'):

            print(" 1 - ??tampaj listu pregleda\n 2 - Logout")  
            br = input("Unesite va??u opciju: ")
            if(br == '1'):
                l.stampaj_listu_pregleda()
            elif(br == '2'):
                print("Odlogovani ste!")
                br = '10'
                logout()
            else:
                print("Pogresan unos, molimo pokusajte ponovo!")
                br = '99'        

def main():
        s = input("Da li se prijavljujete kao admin, lekar ili pacijent? Unesite A za admin, L za lekar, P za pacijent ili K za kraj: ")
        s = s.lower()

        touple = login(s)
        log = touple[0]
        user = touple[1]
        passw = touple[2]
        if ((log == True) and (s == 'a')):
             menu1()
        elif((log == True) and (s == 'l')):
            menu2(user, passw)
        elif((log == True) and (s == 'p')):
            menu3(user, passw)
        else:
            print("Kraj")
            
def logout():
    main()

main()














