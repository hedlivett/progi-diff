class Tó:
    # Tó;Terület_km2;Ország
    _tó: str
    _terület_km2: str
    _ország: str

    @property
    def ez_kanadai(self) -> bool:
        return self._ország == "Kanada"

    # @property
    # def átlagos_terület(self) -> int:
    #     terület_összeg: float = 0
    #     terület_szám: int = 0
    #     for t in self._tó:
    #         terület_összeg += f.
    #     return terület_összeg / terület_szám

    @property
    def tó_adatok(self) -> str:
        vissza: str = f"\tNév: {self._tó}\n"
        vissza: str = f"\t Ország(ok): {self._ország}\n"
        # vissza: str = f"\tÁtlagos terület: {self._átlagos_terület} "
        return vissza

    def __init__(self, sor: str) -> None:
        t, te, o = sor.split(";")
        self._tó = t
        self._te = te  # int(te)
        self._ország = o
