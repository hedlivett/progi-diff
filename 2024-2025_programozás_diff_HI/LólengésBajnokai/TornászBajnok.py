class TornászBajnok:
    # Év;ROrszág;RVaros;BNév;BOrszág;Kor
    _év: int            # számolunk vele. szótárba kell
    _ország: str         # rendező ország
    _város: str
    _név: str
    _nemzet: str         # versenyző ország
    _kor: int            # számolunk vele

    @property 
    def év(self) -> int:  #hogy ha szükség van rá, akkor csináljuk meg a propertyt, feladattal haladva
        return self._év

    @property #nézheted.olvashatod, de nem nyúlhatsz hozzá
    def kor(self) -> int:  #hogy ha szükség van rá, akkor csináljuk meg a propertyt, feladattal haladva
        return self._kor
    
    @property
    def bajnok_adatok(self) -> str:
        vissza: str = ""
        vissza += f"\tNév: {self._név}\n"
        vissza += f"\tOrszág: {self._nemzet}\n"
        vissza += f"\tKor: {self._kor}"
        return vissza
    
    @property
    def rendező_ország(self) -> str:
        return self._ország

    # konstruktor
    def __init__(self, sor:str) -> None:
        év, ország, város, név, nemzet, kor = sor.split(";")
        self._év = int(év)
        self._ország = ország
        self._város = város
        self._név = név
        self._nemzet = nemzet
        self._kor = int(kor)
