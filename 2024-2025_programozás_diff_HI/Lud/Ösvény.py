class Ösvény:
    _sorszám: int
    _mezők: str

    @property
    def sorszám(self) -> int:
        return self._sorszám

    @property
    def mezők(self) -> str:
        return self._mezők

    @property
    def hossz(self) -> int:
        return len(self._mezők)

    def __init__(self, sorszám: int, mezők: str) -> None:
        self._sorszám = sorszám
        self._mezők = mezők

    def mezők_száma(self, mező_típusa: str) -> int:
        return self._mezők.count(mező_típusa)

    def ez_különleges(self, mező_sorszáma: int) -> bool:
        return (
            self._mezők[mező_sorszáma - 1] == "V"
            or self._mezők[mező_sorszáma - 1] == "E"
        )

    def mező(self, mező_sorszáma: int) -> str:
        return self._mezők[mező_sorszáma - 1]
