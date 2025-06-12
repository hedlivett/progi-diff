
from TornászBajnok import TornászBajnok


def betölt_adatforrás(forrás: str) -> list[TornászBajnok]:
    # a listát használat előtt inicialiálni kell ( = [])
    adatok: list[TornászBajnok] = []
    with open(forrás, "r", encoding="utf-8") as file:
        for sor in file.read().splitlines()[
            1:
        ]:  # [1:] - első sor kihagyása  # read== teljes állomány, spitlines adatok feldarabolása
            adatok.append(TornászBajnok(sor))
    return adatok


def olimpiák_száma(tbs: list[TornászBajnok]) -> int:  # tbs = tornászbajnokok
    évszám_halmaz: set[int] = (set())  # üres  halmaz inicializálva  # a halmaz nem engedélyezi a több ugyan olyan adatot
    for bajnok in tbs:
        évszám_halmaz.add(bajnok.év)
    return len(évszám_halmaz)


def átlagéletkor(tbs: list[TornászBajnok]) -> float:
    életkorok_összege: int = 0
    for bajnok in tbs:  # ífor előhívással
        életkorok_összege += bajnok.kor
        # vagy így: életkorok_összege = életkorok_összege + bajnok.kor
    return életkorok_összege / len(tbs)
    # vagy: #return round( életkorok_összege / len(tbs), 2)


def legfiatalabb_bajnok(tbs: list[TornászBajnok]) -> TornászBajnok:
    legfiatalabb: TornászBajnok = tbs[0]
    for bajnok in tbs[1:]:  # első vizsgálat átugrása, önmaga nem lehet
        if bajnok.kor < legfiatalabb.kor:
            legfiatalabb = bajnok  # ífor előhívással
    return legfiatalabb


def rendező_ország_volt(
    ország_neve: str, tbs: list[TornászBajnok]
) -> bool:  # paraméterek a ()-en belül. pl. a tbs is  paraméter
    # Ennek az ellenkezőjét próbáljuk bizonyítani
    for bajnok in tbs:
        if (bajnok.rendező_ország == ország_neve):  # most így furán jön ki, de mivel az osztály név tornászbajnbok ennek a névnek bajnoknak kell lennie
            return True
    return False

    #8.feladat, szótár, statisztika
def stat(tbs: list[TornászBajnok]) -> dict[int, int]:                 #statisztika # int, int két soros szótár, első sor: év, második sor: fők száma, mind 2 értéke szám [int]
    s: dict[int, int] = dict()          # szótár inicalizálása, üres szótár
    for bajnok in tbs:         # "ífor" beírásával feljön
        if bajnok.év in s:     #igaz vagy hamis    # az év már publikus, már megcsináltuk előzőleg
            #ha az évszám megtalálható már a szótárban
            s[bajnok.év] += 1
        else:
            # ha az évszám még nincs a szótárban, akkor beletesszük:
            s[bajnok.év] = 1      # az elsőt nem hagyhatom ki
    return s

def main() -> None:
    # 1.feladat - projekt létrehozás
    # 2.feladat
    bajnokok: list[TornászBajnok] = betölt_adatforrás(
        "lolenges.txt"
    )  # lista #bajnokok vátozónév egy pointer
    print(f"3. feladat: Bajnokok száma: {len(bajnokok)} fő")
    print(f"4. feladat: Olimpiák száma: {olimpiák_száma(bajnokok)}")
    print(f"5. feladat: Átlagéletkor: {átlagéletkor(bajnokok):.2f} év" )

    # :.2f - 2vel való kerekítés, a pont előtt, a ketőspont után megtudjuk határozni a szélességét,
    # utána nem, pl.::4.0f, f helyett e normál alak
    print("6. feladat: Legfiatalabb versenyző adatai:")
    print(legfiatalabb_bajnok(bajnokok).bajnok_adatok)

    # 7.feladat
    print("7. feladat: Kérek egy országot  [pl.: USA]: ", end="")  # következő sor end-el
    input_ország: str = input("")  # vagy egybe: input_ország: str = input("7. feladat: Kérek egy országot  [pl.: USA]: ")

    if rendező_ország_volt(input_ország, bajnokok):
    # felesleges a végére a == True # itt a sorrend nem mind 1
        print("\tRendeztek ebben az országban olimpiát.")
    else:
        print("\tNem rendeztek ebben az országban olimpiát.")
    # másik opció: short hand if-el:
    print(
        f"\t{'RendezteK' if rendező_ország_volt(input_ország, bajnokok) else ' Nem rendeztek'} ebben az országban olimpiát.") # amikor hívom akkor aktív paraméterek (pl.itt), mikor írjuk akkor formális paraméter
    # ha már hazsnáltál egyszer ""- t akkor már csak ''-t írhatsz

    #8.feladat, szótár
    print("8. feladat: Statisztika:")
    # Hf készíts többsoros sztringgel visszatérő függvényt !
    # print(stat_összeállít(bajnokok))
    # ez helyett a fentikánt nézzen ki, egy fgv, \t, \n, nézz utána
    for (key,value) in stat(bajnokok).items():
        if value > 1:
            print(f"\t{key} - {value} fő")



if __name__ == "__main__":
    main()

# átlag, szélsőérték, statisztika használata
# #7es-8as esetleg otthon, statisztika

# shift + tab == rendezi a rosszul másolt dolgokat egybe, sorok heyének javítása
