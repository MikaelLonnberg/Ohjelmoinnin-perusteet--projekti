import random

# Funktio arvaa_numero toteuttaa itse pelin logiikan
def arvaa_numero():
    # Arvotaan satunnainen luku väliltä 1-10 ja tallennetaan muuttujaan "muuttuja"
    muuttuja = random.randint(1, 10)
    # Kysytään käyttäjältä nimimerkki ja tallennetaan se muuttujaan "nimimerkki"
    nimimerkki = input("Anna nimimerkki: ")
    # Alustetaan muuttuja "yritykset", joka pitää kirjaa arvauskertojen määrästä
    yritykset = 0

    # Annetaan pelaajalle ohjeet
    print("Arvaa numero 1-10. Ohjelma kertoo arvauksien jälkeen oliko arvaus liian pieni vai liian suuri. Jos saat oikein, peli ilmoittaa onnittelusi ja tallentaa tuloksesi tiedostoon.")
    arvaus = None

    # Suoritetaan peli, kunnes pelaaja arvaa oikean numeron
    while arvaus != muuttuja:
        # Kysytään käyttäjältä arvaus ja muunnetaan se kokonaisluvuksi
        arvaus = int(input("Arvaa numero 1-10: "))
        # Lisätään yritysten määrää yhdellä joka kierroksella
        yritykset += 1

        # Tarkistetaan, onko arvaus oikea
        if arvaus < muuttuja:
            print("Liian pieni")
        elif arvaus > muuttuja:
            print("Liian suuri")
        else:
            # Jos arvaus on oikein, tulostetaan onnitteluteksti ja arvausten määrä
            print(f"Voitit. Sinulla meni {yritykset} yritystä.")
            # Tallennetaan tulos tiedostoon talteen
            tallenna_tulos(nimimerkki, yritykset)

# Funktio tallenna_tulos tallentaa pelaajan tuloksen tiedostoon
def tallenna_tulos(nimimerkki, yritykset):
    # Tiedosto avataan lisäämismoodissa ("a"), jotta vanhat tulokset säilyvät
    with open("tulokset.txt", "a") as tiedosto:
        # Tulos tallennetaan muodossa "nimimerkki: yritysten määrä"
        tiedosto.write(f"{nimimerkki}: {yritykset}\n")

# Funktio lue_tulokset lukee tallennetut tulokset tiedostosta
def lue_tulokset():
    tulokset = []
    try:
        # Tiedosto avataan lukumoodissa ("r")
        with open("tulokset.txt", "r") as tiedosto:
            # Luetaan jokainen rivi tiedostosta
            for rivi in tiedosto:
                 # Rivin osat erotetaan ":", ja nimimerkki ja yritysten määrä tallennetaan listaan
                osat = rivi.strip().split(": ")
                nimimerkki = osat[0]
                yritykset = int(osat[1])
                tulokset.append((nimimerkki, yritykset))
    except FileNotFoundError:
        pass
    return tulokset

# Funktio nayta_top_10_tulokset näyttää top 10 tulokset
def nayta_top_10_tulokset():
    # Luetaan tallennetut tulokset tiedostosta
    tulokset = lue_tulokset()
    # Järjestetään tulokset yritysten määrän perusteella ja otetaan vain 10 parasta
    top_10 = sorted(tulokset, key=lambda x: x[1])[:10]
    print("Top 10 tulokset:")
    # Tulostetaan top 10 tulokset
    for i, (nimimerkki, yritykset) in enumerate(top_10, 1):
        print(f"{i}. {nimimerkki} - {yritykset} yritystä")

# Pääfunktio main hallitsee ohjelman suoritusta
def main():
    while True:
        # Tulostetaan valikko
        print("\n1. Pelaa peliä")
        print("2. Näytä Top 10 tulokset")
        print("3. Lopeta")
        # Kysytään käyttäjältä valinta
        valinta = input("Valitse toiminto: ")

        if valinta == "1":
            # Kutsutaan pelifunktiota
            arvaa_numero()
        elif valinta == "2":
            # Kutsutaan funktiota top 10 tulosten näyttämiseksi
            nayta_top_10_tulokset()
        elif valinta == "3":
            # Lopetaan peli ja kiitetään pelaajaa
            print("Kiitos pelaamisesta! Hei hei!")
            break
        else:
            # Jos painat jotain muuta kuin 1, 2 tai 3 niin esitetään virheilmoitus
            print("Virheellinen valinta, yritä uudelleen.")

if __name__ == "__main__":
    main()