from Solution import Solution


def main() -> None:
    sol: Solution = Solution("lakes.txt")
    print(f"2. feladat: Tavak száma: {sol.number_of_lakes}")

    # Határozzuk meg a több ország területén fekvő tavak számát
    print(f"3. feladat: Több ország területén fekvő tavak száma: {sol.number_of_multi_lakes}")

    # Eldöntés: Határozd meg, hogy van-e olyan tó, amely "n" ország területén fekszik!
    print("4. feladat: Van-e?")
    n: int = 4
    print(f"\t{'Van' if sol.there_are_n_countires_lakes(n) else 'Nincs'}")
    
    print("5. feladat: Statisztika")
    print(sol.statistics)

    print("6. feladat: próba.txt") # új txt létrehozása ebben a néven
    sol.create_new_file("próba.txt")

if __name__ == "__main__":
    main()

# Hf: Határozd meg a 20.000 km2 terület feletti tavak számát
# + írjad ki a legnagyobb tó adatait
# + írjad ki legkisebb tó adatait

# írás is egyszerű