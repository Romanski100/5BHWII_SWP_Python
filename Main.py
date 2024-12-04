from AkustikGitarre import AkustikGitarre
from EGitarre import EGitarre
from BassGitarre import BassGitarre

gitarre1 = AkustikGitarre("Yamaha", "FG800", 250, "Fichte", 6, False)
gitarre2 = EGitarre("Fender", "Stratocaster", 1200, "Single-Coil", "Tremolo", "Sunburst")
gitarre3 = BassGitarre("Ibanez", "SR500E", 900, "34\"", 24)

print(gitarre1.beschreibung())
print(gitarre2.beschreibung())
print(gitarre3.beschreibung())
