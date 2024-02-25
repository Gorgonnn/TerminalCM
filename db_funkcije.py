import os
import sys

import pymysql
import cl_main
import smtplib
from pwinput import pwinput
import random

Mysql_baza = {
    "host": "tzivkodb.cshmnu8njvkr.us-east-1.rds.amazonaws.com",
    "user": "admin",
    "password": "Toma09072303-",
    "database": "Prva_Baza"
}


def Provjera_username(username):
    with pymysql.connect(**Mysql_baza) as baza:
        with baza.cursor() as cursor:
            querry = "Select * from Korisnici_python  where username = %s"
            cursor.execute(querry, (username,))
            ispis = cursor.fetchone()
            print(ispis)


def Zaglavlje(user):
    os.system("cls")
    print((30 * "="))
    print(f"Welcome! {user}")
    print((30 * "="))



Veza = pymysql.connect(**Mysql_baza)

kursor = Veza.cursor()
i = 0

def Broj_redova():

    baza = pymysql.connect(**Mysql_baza)
    pokazivac = baza.cursor()
    querry = "Select count(*) from information_schema.columns where table_name = 'Korisnici_python'"
    pokazivac.execute(querry)

    redovi = pokazivac.fetchone()[0]
    baza.close()
    return redovi

def Provjera_Unosa():
    querry = "SELECT * FROM Korisnici_python;"
    kursor.execute(querry)
    rjesenje = kursor.fetchall()
    Veza.close()
    for element in rjesenje:
        print(50 * "-")
        print(f" Username: {element[1]}\n Password: {element[2]}\n Ime: {element[3]}\n Registracija[yyyy-mm-dd HH:mm:ss]:  {element[4]}")
        print(50*"-")



def Novi_Unos(user, passw, name):
    with pymysql.connect(**Mysql_baza) as db_connection:
        with db_connection.cursor() as pokazivac:
            query = "INSERT INTO Korisnici_python (username, passwor_d, ime) VALUES (%s,%s,%s)"
            pokazivac.execute(query,(user, passw, name))
            db_connection.commit()



def Prijava():

    while True:
        os.system('cls')
        print("            --- Register ---")
        Sign_in_credentials = cl_main.Korisnici(input("Username: "), pwinput("Password: ", mask="*"), input("Ime: "))
        provjera = Sign_in_credentials.Provjera_pass(pwinput("Provjera pass: "))
        #Moras provjeriti jos i username
        if provjera == True and Provjera_username(Sign_in_credentials.Username) == None:
           rand_broj = e_mail_vertifikacija()
           if str(rand_broj) == input("Enter Email verifikacion number: "):
               Novi_Unos(Sign_in_credentials.Username, Sign_in_credentials.Password, Sign_in_credentials.Ime)
               break

           else:
               print("Invalid number : ")
        else:
            os.system("cls")
            print("Usename is in use!: ")
            pass






#TREBA JOS DORADITI NA FUNKCIJI, NE ZELI SLATI VISELINIJSKI TEXT U MAIL, MISLIM DA JE DO NETWORKINGA|
def e_mail_vertifikacija():
    Email_korisnik = input("Enter E-mail for Vertification: ")
    Email_aplikacija = "taplikaciju@gmail.com"
    Rand_broj = random.randint(678, 1723)
    text = str(Rand_broj)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(Email_aplikacija,"jtul vwbm yxyb scnk")

    server.sendmail(Email_aplikacija, Email_korisnik, msg=text)
    print("We sent u e-mail with code for vertification")
    #dosao sam quit, ako ne radi mail to je mozda razlog
    server.quit()
    return text


def log_in():
    while True:

        print(25*"-" + "Log in" + 25 * "-")
        Var_Username = input("Username: ")
        Var_Password = pwinput(prompt="Password: ", mask="*")
        with pymysql.connect(**Mysql_baza) as baza:
            with baza.cursor() as kursor:
                querry = f"Select * from Korisnici_python where username = %s and passwor_d = %s; "
                kursor.execute(querry, (Var_Username, Var_Password))
                rezultat = kursor.fetchone()
                if rezultat is None:
                    os.system("cls")
                    print("-----Username or Password are incorrect!-----\n")
                    log = input("For log|quit|register type: <log><quit><reg>: ")
                    if log.lower() == "log":
                        pass
                    if log.lower() == "quit":
                        os.system("\ncls")
                        sys.exit("Shutting down app!")
                    if log.lower() == "reg":
                        os.system("cls")
                        Prijava()
                if rezultat != None:
                    return rezultat

def Kreiranje_korisnickog_direktorija(user):
    if os.path.exists(fr"C:\Users\tomis\Documents\Moj_projekt\{user}"):
        os.system("cls\n")
    else:
        os.mkdir(fr"C:\Users\tomis\Documents\Moj_projekt\{user}")



