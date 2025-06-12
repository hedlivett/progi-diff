from Ösvény import Ösvény


class Ösvények:
    _ösvények: list[Ösvény] = []

    @property
    def ösvények_száma(self) -> int:
        return len(self._ösvények)

    @property
    def leghosszabb_ösvény(self) -> Ösvény:
        leghosszabb: Ösvény = self._ösvények[0]
        for akt_ösvény in self._ösvények[1:]:
            if akt_ösvény.hossz > leghosszabb.hossz:
                leghosszabb = akt_ösvény
        return leghosszabb

    def __init__(self, állomány_neve: str) -> None:
        sorszám: int = 1
        with open(állomány_neve, "r", encoding="utf-8") as file:
            for ösvény in file.read().splitlines():
                self._ösvények.append(Ösvény(sorszám, ösvény))
                sorszám += 1

    def mező_statiszta(self, ösvény_sorszáma: int) -> str:
        ösvény_indexe: int = ösvény_sorszáma - 1
        ösvény: Ösvény = self._ösvények[ösvény_indexe]
        vissza: str = ""
        # m_db: int = ösvény.mezők_száma("M")
        # e_db: int = ösvény.mezők_száma("E")
        # v_db: int = ösvény.mezők_száma("V")

        # if m_db > 0:
        #     vissza += f"M: {m_db} darab\n"
        # if e_db > 0:
        #     vissza += f"E: {e_db} darab\n"
        # if v_db > 0:
        #     vissza += f"V: {v_db} darab\n"

        for mező_típusa in "MEV":
            db: int = ösvény.mezők_száma(mező_típusa)
            if db > 0:
                vissza += f"{mező_típusa}: {db} darab\n"

        return vissza

    def _különleges_mezők_listája(self, ösvény_sorszáma: int) -> list[str]:
        vissza: list[str] = []
        ösvény_indexe: int = ösvény_sorszáma - 1
        ösvény: Ösvény = self._ösvények[ösvény_indexe]
        for mező_sorszáma in range(1, ösvény.hossz + 1):
            if ösvény.ez_különleges(mező_sorszáma):
                vissza.append(f"{mező_sorszáma}.\t{ösvény.mező(mező_sorszáma)}\n")
        return vissza

    def különleges_mezők_állományba(self, állomány_neve: str, ösvény_sorszáma: int) -> None:
        with open(állomány_neve, "w", encoding="utf-8") as file:
            file.writelines(self._különleges_mezők_listája(ösvény_sorszáma))
