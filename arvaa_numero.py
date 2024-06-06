import random

def arvaa_numero():
    muuttuja = random.randint(1, 10)
    nimimerkki = input("Anna nimimerkki: ")
    yritykset = 0

    print("Arvaa numero 1-10. Ohjelma kertoo arvauksien jälkeen oliko arvaus liian pieni vai liian suuri. Jos saat oikein, peli ilmoittaa onnittelusi ja tallentaa tuloksesi tiedostoon.")
    arvaus = None

    while arvaus != muuttuja:
        arvaus = int(input("Arvaa numero 1-10: "))
        yritykset += 1

        if arvaus < muuttuja:
            print("Liian pieni")
        elif arvaus > muuttuja:
            print("Liian suuri")
        else:
            print(f"Voitit. Sinulla meni {yritykset} yritystä.")
            tallenna_tulos(nimimerkki, yritykset)

def tallenna_tulos(nimimerkki, yritykset):
    with open("tulokset.txt", "a") as tiedosto:
        tiedosto.write(f"{nimimerkki}: {yritykset}\n")

def lue_tulokset():
    tulokset = []
    try:
        with open("tulokset.txt", "r") as tiedosto:
            for rivi in tiedosto:
                osat = rivi.strip().split(": ")
                nimimerkki = osat[0]
                yritykset = int(osat[1])
                tulokset.append((nimimerkki, yritykset))
    except FileNotFoundError:
        pass
    return tulokset

def nayta_top_10_tulokset():
    tulokset = lue_tulokset()
    top_10 = sorted(tulokset, key=lambda x: x[1])[:10]
    print("Top 10 tulokset:")
    for i, (nimimerkki, yritykset) in enumerate(top_10, 1):
        print(f"{i}. {nimimerkki} - {yritykset} yritystä")

def main():
    while True:
        print("\n1. Pelaa peliä")
        print("2. Näytä Top 10 tulokset")
        print("3. Lopeta")
        valinta = input("Valitse toiminto: ")

        if valinta == "1":
            arvaa_numero()
        elif valinta == "2":
            nayta_top_10_tulokset()
        elif valinta == "3":
            print("Kiitos pelaamisesta! Hei hei!")
            break
        else:
            print("Virheellinen valinta, yritä uudelleen.")

if __name__ == "__main__":
    main()