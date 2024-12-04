from Gitarre import Gitarre

class EGitarre(Gitarre):
    def __init__(self, marke, modell, preis, pickups, bruecke, farbe):
        super().__init__(marke, modell, preis)
        self.pickups = pickups
        self.bruecke = bruecke
        self.farbe = farbe

    def beschreibung(self):
        return (super().beschreibung() + 
                f", Pickups: {self.pickups}, Brücke: {self.bruecke}, Farbe: {self.farbe}")
