class Korisnici:
    def __init__(self, Username , Password, Ime,):
        self.Username = Username
        self.Password = Password
        self.Ime = Ime

    def Provjera_pass(self, passwordcheck):
        if passwordcheck == self.Password:
            return True
        else:
            return False


# | Za sada smatram da je ovo bezpotrebno posto citam it db |
    def Ispis_Korisnika(self):
        print(self.Username)
        print(self.Password)
        print(self.Ime)


#------------------------------------------------------------

  # | Ovo se jos mora doraditi kada dodem do delegacije |
    def Delegacija_prava(self):
        if self.name == "Tomislav":
            print("Imate prava")
        else:
            print("Nemate prava")
  # --------------------------------------------------------