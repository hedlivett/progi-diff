from Tó import Tó

class Megoldás:
    _tavak: list[Tó] = []

    @property
    def tavak_száma(self) -> int:
        return len(self._tavak)
    
    @property
    def kanadai_tavak_száma(self) -> int:
        db: int = 0
        for t in self._tavak:
            if t.ez_kanadai:
                db += 1
        return db
    
    
    @property
    def legnagyobb_tó_statisztika(self) -> None: #str
        pass

    def __init__(self, állomány_neve: str) -> None:
        with open(állomány_neve, "r", encoding="utf-8") as file:
            for sor in file.read().splitlines()[1:]:  # [1:] - első sor kihagyása
                self._tavak.append(Tó(sor))