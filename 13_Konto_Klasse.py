class Konto(object): 
    def __init__(self, inhaber, kontonummer, kontostand, kontokorrent=0): 
        self.Inhaber = inhaber 
        self.Kontonummer = kontonummer 
        self.Kontostand = kontostand 
        self.Kontokorrent = kontokorrent

    def ueberweisen(self, ziel, betrag):
        if(self.Kontostand - betrag < -self.Kontokorrent):
            # Deckung nicht genug
            return False  
        else: 
            self.Kontostand -= betrag 
            ziel.Kontostand += betrag 
            return True

    def einzahlen(self, betrag): 
        self.Kontostand += betrag 

    def auszahlen(self, betrag): 
        if(self.Kontostand - betrag < -self.Kontokorrent):
            # Deckung nicht genug
            return False
        else:
            self.Kontostand -= betrag 
            return True

    def kontostand(self): 
        return self.Kontostand

    def kontoinhaber(self):
        return self.Inhaber

    def kontonummer(self):
        return self.Kontonummer

    def zinsen_berechnen(self, zinssatz):
        zinsen = self.Kontostand * (zinssatz / 100)
        self.Kontostand += zinsen

    def kontoauszug_drucken(self):
        print("Kontoauszug für:", self.Inhaber)
        print("Kontonummer:", self.Kontonummer)
        print("Aktueller Kontostand:", self.Kontostand)


# Beispiel für die Verwendung der Klasse Konto
konto1 = Konto("Ignaz Gorinschek", "1234567890", 1000)
konto2 = Konto("Leon Suppe", "0987654321", 500)

# Überweisung von konto1 auf konto2
konto1.ueberweisen(konto2, 200)

# Einzahlung auf konto1
konto1.einzahlen(300)

# Auszahlung von konto1
konto1.auszahlen(50)

# Kontostand abfragen
print("Kontostand von konto1:", konto1.kontostand())

# Kontoinhaber und Kontonummer abfragen
print("Inhaber von konto2:", konto2.kontoinhaber())
print("Kontonummer von konto2:", konto2.kontonummer())

# Zinsen berechnen und hinzufügen
konto1.zinsen_berechnen(1.5)

# Kontoauszug drucken
konto1.kontoauszug_drucken()
