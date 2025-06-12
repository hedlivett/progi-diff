class Dobások:
    _dobások: list[int] = []  # protected adattag, 1db "_" -el kezdődik

    @property  # jellemző lett a metódusból (függvényből), olyan függvény, aminek nincs paramétere
    def dobások_száma(self) -> int:
        return len(self._dobások)

    def __init__(self, állomány_neve: str) -> None:
        with open(állomány_neve, "r", encoding="utf-8") as file:
            for dobás in file.read().split(" "):  # [1:] - első sor kihagyása
                self._dobások.append(int(dobás))
