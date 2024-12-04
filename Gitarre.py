class Gitarre:
    def __init__(self, marke, modell, preis):
        self.marke = marke
        self.modell = modell
        self.preis = preis

    def beschreibung(self):
        return f"{self.marke} {self.modell}, Preis: {self.preis} €"
