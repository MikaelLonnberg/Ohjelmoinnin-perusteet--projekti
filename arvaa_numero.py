#Tällä me saadaan tulokset talteen
"""
def tallenna_tulos(nimi, pisteet):
    with open("tulokset.txt", "a") as tiedosto:
        tiedosto.write(f"{nimi}: {pisteet}\n")

def main():
    nimi = input("Anna pelaajan nimi: ")
    pisteet = 100  # Laitetaan tähän oikeat pisteet
    tallenna_tulos(nimi, pisteet)

if __name__ == "__main__":
    main()
"""

#Tällä voi hakea top 10 tulokset
"""
def lue_tulokset():
    tulokset = []
    with open("tulokset.txt", "r") as tiedosto:
        for rivi in tiedosto:
            nimi, pisteet = rivi.strip().split(": ")
            tulokset.append((nimi, int(pisteet)))
    return tulokset

def top10_tulokset(tulokset):
    top10 = sorted(tulokset, key=lambda x: x[1], reverse=True)[:10]
    return top10

def main():
    tulokset = lue_tulokset()
    top10 = top10_tulokset(tulokset)
    print("Top 10 tulokset:")
    for i, (nimi, pisteet) in enumerate(top10, start=1):
        print(f"{i}. {nimi}: {pisteet}")

if __name__ == "__main__":
    main()
"""

#Tällä pelaaja näkee omat pisteensä pelikierrosten välissä, ja voi halutessaan jatkaa peliä.
"""
def tallenna_tulos(nimi, pisteet):
    with open("tulokset.txt", "a") as tiedosto:
        tiedosto.write(f"{nimi}: {pisteet}\n")

def pelikierros():
    nimi = input("Syötä pelaajan nimi: ")
    # Tässä voit lisätä itse pelin logiikan
    arvaus = int(input("Arvaa numero: "))
    # Oletetaan tässä yksinkertaisesti, että pisteet ovat arvattu numero
    pisteet = arvaus
    print("Pisteet:", pisteet)
    tallenna_tulos(nimi, pisteet)

def main():
    while True:
        pelikierros()
        jatka = input("Haluatko pelata uudestaan? (k/e): ")
        if jatka.lower() != "k":
            break

if __name__ == "__main__":
    main()
"""

#Tässä koko rimpsu yhdessä
"""
def tallenna_tulos(nimi, pisteet):
    with open("tulokset.txt", "a") as tiedosto:
        tiedosto.write(f"{nimi}: {pisteet}\n")

def pelikierros():
    nimi = input("Syötä pelaajan nimi: ")
    # Tässä voit lisätä itse pelin logiikan
    arvaus = int(input("Arvaa numero: "))
    # Oletetaan tässä yksinkertaisesti, että pisteet ovat arvattu numero
    pisteet = arvaus
    print("Pisteet:", pisteet)
    tallenna_tulos(nimi, pisteet)

def parhaat_tulokset():
    with open("tulokset.txt", "r") as tiedosto:
        tulokset = [rivi.strip() for rivi in tiedosto]
        tulokset.sort(key=lambda x: int(x.split(":")[1]), reverse=True)
        print("Parhaat tulokset:")
        for i, tulos in enumerate(tulokset[:10], start=1):
            print(f"{i}. {tulos}")

def main():
    while True:
        pelikierros()
        jatka = input("Haluatko pelata uudestaan? (k/e): ")
        if jatka.lower() != "k":
            break
    parhaat_tulokset()

if __name__ == "__main__":
    main()

"""
