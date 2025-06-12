from Dobások import Dobások
from Ösvények import Ösvények


def main() -> None:
    print("2. feladat")
    dobások: Dobások = Dobások("dobasok.txt")
    print(f"A dobások száma: {dobások.dobások_száma}")
    ösvények: Ösvények = Ösvények("osvenyek.txt")
    print(f"A ösvények száma: {ösvények.ösvények_száma}")

    print("\n3. feladat")
    leghosszabb = ösvények.leghosszabb_ösvény
    print(
        f"Az egyik leghosszabb ösvény a(z) {leghosszabb.sorszám}. ösvény, hossza: {leghosszabb.hossz} "
    )

    print("\n4. feladat")
    # ösvény_sorszáma: int = int(input("Adja meg egy ösvény sorszámát! "))
    # játékosok_száma: int = int(input("Adja meg a játékosok számát! "))
    ösvény_sorszáma: int = 9
    # játékosok_száma: int = 5

    print("\n5. feladat")
    print(ösvények.mező_statiszta(ösvény_sorszáma))

    print("\n6. feladat: különleges.txt")
    ösvények.különleges_mezők_állományba("különleges.txt", ösvény_sorszáma)


if __name__ == "__main__":
    main()
