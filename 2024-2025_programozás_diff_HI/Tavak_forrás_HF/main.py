from Megoldás import Megoldás

# színsávos feladat
# 32-bites egész típusú adato == int
# str-eket nem lehet összeadni
# 2. feladat: split, átalakít, jellemző
# jövő hétig házi, kövi óra önálló, hibában segít
# sor:str
# [] == lista
# 10.feladat fájba írás, w a második praméter, íopen agrev
# legalább 7. feladatig


def main() -> None:
    pass  # Kezd a kódolást itt!


m: Megoldás = Megoldás("tavak.txt")
print(f"5. feladat: Tavak száma: {m.tavak_száma} db")
print(f"6. feladat: kanadai tavak száma: {m.kanadai_tavak_száma} fő")  # nem ujó
print(f"7. feladat: A legnagyobb tó adatai: {0}")
# print("\tNév:")
# print("\tOrszág(ok): ")
# print("\tÁtlagos terület: {} Km2")


if __name__ == "__main__":
    main()
