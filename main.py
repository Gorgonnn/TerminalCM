# This is a sample Python script.
import db_funkcije
import Home_funkcije

if __name__ == '__main__':

#Prvo pokrecem log_in() funkciju
   #Ona provjerava postojeceg ili kreira novog korisnika u protivnom ide u loop/gasi program
 """Broj_redova = db_funkcije.Broj_redova()"""

"""db_funkcije.Prijava()
db_funkcije.Novi_Unos()"""
"""db_funkcije.Provjera_Unosa()"""
"""db_funkcije.Prijava()"""
"""
korisnik = db_funkcije.log_in()
db_funkcije.Zaglavlje(korisnik[2])
Provjera_korisnika = input("Provjera korisnika:  <p>")
if Provjera_korisnika.lower() == "p":
 db_funkcije.Zaglavlje(korisnik[2])
else:
 pass
"""

#Brza provjera

#


korisnik = db_funkcije.log_in()
db_funkcije.Kreiranje_korisnickog_direktorija(korisnik[1])
Home_funkcije.Home_screen(korisnik[1])




