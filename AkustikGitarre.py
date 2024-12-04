from Gitarre import Gitarre

class AkustikGitarre(Gitarre):
    def __init__(self, marke, modell, preis, korpusmaterial, saitenanzahl, cutaway):
        super().__init__(marke, modell, preis)
        self.korpusmaterial = korpusmaterial
        self.saitenanzahl = saitenanzahl
        self.cutaway = cutaway

    def beschreibung(self):
        return (super().beschreibung() + 
                f", Material: {self.korpusmaterial}, Saiten: {self.saitenanzahl}, Cutaway: {'Ja' if self.cutaway else 'Nein'}")
