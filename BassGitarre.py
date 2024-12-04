from Gitarre import Gitarre

class BassGitarre(Gitarre):
    def __init__(self, marke, modell, preis, mensur, bundanzahl):
        super().__init__(marke, modell, preis)
        self.mensur = mensur
        self.bundanzahl = bundanzahl
       

    def beschreibung(self):
        return (super().beschreibung() + 
                f", Mensur: {self.mensur}, Bünde: {self.bundanzahl}")
