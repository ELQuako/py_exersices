class Auto:
    def __init__(self, marke, modell):
        self.marke = marke
        self.modell = modell

    def details_anzeigen(self):
        print("Marke:", self.marke)
        print("Modell:", self.modell)

auto1 = Auto("Porsche", "911 GT3RS")
auto1.details_anzeigen()