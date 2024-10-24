import random
from collections import Counter

""" 
Royal Flush
Straight Flush
Vierling(four of a kind)
Full House
Flush
Straße
Drilling(Three of a kind)
Zwei Paare
Paare
High Card
"""

farben = ['Pik', 'Herz', 'Karo', 'Kreuz']  
werte = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'B', 'D', 'K', 'A'] 

kartendeck = [(wert, farbe) for wert in werte for farbe in farben]

def draw_hand():
    return random.sample(kartendeck, 5)

def get_value_counts(hand):
    werte_in_hand = [karte[0] for karte in hand]
    return Counter(werte_in_hand)

# Prüfen auf Paar
def has_pair(hand):
    counts = get_value_counts(hand)
    return 2 in counts.values()

# Prüfen auf Drilling
def has_three_of_a_kind(hand):
    counts = get_value_counts(hand)
    return 3 in counts.values()

# Prüfen auf Vierling (Poker)
def has_four_of_a_kind(hand):
    counts = get_value_counts(hand)
    return 4 in counts.values()

# Prüfen auf Full House (Drilling + Paar)
def has_full_house(hand):
    counts = get_value_counts(hand)
    return 3 in counts.values() and 2 in counts.values()

# Prüfen auf Flush (5 Karten der gleichen Farbe)
def has_flush(hand):
    farben_in_hand = [karte[1] for karte in hand]
    return len(set(farben_in_hand)) == 1

# Prüfen auf Straße (5 aufeinanderfolgende Karten)
def has_straight(hand):
    werte_reihenfolge = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'B', 'D', 'K', 'A']
    werte_in_hand = sorted([werte_reihenfolge.index(karte[0]) for karte in hand])
    
    # Prüfen auf eine Reihenfolge von 5 Karten
    return all(werte_in_hand[i] + 1 == werte_in_hand[i + 1] for i in range(4))

# Prüfen auf Straight Flush (Straße + Flush)
def has_straight_flush(hand):
    return has_straight(hand) and has_flush(hand)

# Prüfen auf Royal Flush (10, B, D, K, A in einer Farbe)
def has_royal_flush(hand):
    werte_in_hand = {karte[0] for karte in hand}
    farben_in_hand = {karte[1] for karte in hand}
    
    return werte_in_hand == {'10', 'B', 'D', 'K', 'A'} and len(farben_in_hand) == 1

# Funktion, um zu prüfen, welche Kombinationen eine Hand hat
def classify_hand(hand):
    if has_royal_flush(hand):
        return 'Royal Flush'
    elif has_straight_flush(hand):
        return 'Strassen Flush'
    elif has_four_of_a_kind(hand):
        return 'Vierling'
    elif has_full_house(hand):
        return 'Full House'
    elif has_flush(hand):
        return 'Flush'
    elif has_straight(hand):
        return 'Strasse'
    elif has_three_of_a_kind(hand):
        return 'Drilling'
    elif has_pair(hand):
        return 'Paar'
    else:
        return 'Hohe Karte'

# 3. Simulation von 100000 Spielen
def simulate_poker_games(n):
    ergebnisse = Counter()
    for _ in range(n):
        hand = draw_hand()
        kombination = classify_hand(hand)
        ergebnisse[kombination] += 1
    return ergebnisse

# 4. Berechnung der Wahrscheinlichkeiten
def calculate_probabilities(ergebnisse, gesamt_spiele):
    wahrscheinlichkeiten = {}
    for kombination, anzahl in ergebnisse.items():
        wahrscheinlichkeiten[kombination] = (anzahl / gesamt_spiele) * 100
    return wahrscheinlichkeiten

# 5. Simuliere 100000 Spiele und zeige die Ergebnisse
if __name__ == "__main__":
    gesamt_spiele = 100000
    ergebnisse = simulate_poker_games(gesamt_spiele)
    wahrscheinlichkeiten = calculate_probabilities(ergebnisse, gesamt_spiele)
    
    
    print("Ergebnisse nach 100000 Spielen:")
    for kombination, wahrscheinlichkeit in wahrscheinlichkeiten.items():
        print(f"{kombination}: {wahrscheinlichkeit:.5f}%")
