class Lake:
    _name: str
    _area: int  # terület
    _countries: str

    @property
    def is_multi_countries(self) -> bool:
        # return self._countries.find(",",0) != -1 # find a vesszőt keresi, ha megtalálja a legelsővel tér vissza, ha nem -1 -el tér vissza , multicountries
        # return len(self._countries.split(",")) < 1
        for char in self._countries:  # eldöntés
            if char == ",":
                return True
        return False
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def area(self) -> int:
        return self._area

    @property
    def number_of_commas(self) -> int:  # vessző
        piece: int = 0
        for char in self._countries:  # számolás
            if char == ",":
                piece += 1
        return piece
    
    @property
    def number_of_countries(self) -> int:
        return self.number_of_commas + 1

    def __init__(self, data_line: str) -> None:
        n, a, c = data_line.split(";")
        self._name = n
        self._area = int(a)
        self._countries = c
        
    # alatta már fgv. nem kell property



    def is_n_countries_lake(self, n: int) -> bool:
        # Igen vagy nem, 5 ország? # 5 országot 4 db vessző választ el
        return self.number_of_commas == n - 1
