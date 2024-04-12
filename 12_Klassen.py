class Pflanze:
    def __init__(self, farbe):
        self.farbe = farbe
  
  
class Auto:
    def __init__(self, marke):
        self.marke = marke 


class Motorrad:
    def __init__(self, kubik):
        self.kubik = kubik


class Lehrling:
    def __init__(self, alter):
        self.alter = alter
        
        
class Fernseher:
    def __init__(self, zoll):
        self.zoll = zoll


P1 = Pflanze ("Rot")
P2 = Pflanze ("Grün") 
P3 = Pflanze ("Blau")
print(P1.farbe)
print(P2.farbe)
print(P3.farbe)


A1 = Auto ("Audi")
A2 = Auto ("BMW")
A3 = Auto ("Porsche")
print(A1.marke)
print(A2.marke)
print(A3.marke)


M1 = Motorrad ("1000ccm")
M2 = Motorrad ("125ccm")
M3 = Motorrad ("50ccm")
print(M1.kubik)
print(M2.kubik)
print(M3.kubik)


L1 = Lehrling ("18 Jahre")
L2 = Lehrling ("17 Jahre")
L3 = Lehrling ("16 Jahre")
print(L1.alter)
print(L2.alter)
print(L3.alter)


F1 = Fernseher ("75 zoll")
F2 = Fernseher ("55 zoll")
F3 = Fernseher ("100 zoll")
print(F1.zoll)
print(F2.zoll)
print(F3.zoll)