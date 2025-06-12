from Lake import Lake


class Solution:
    _lakes: list[Lake] = []

    @property
    def number_of_lakes(self) -> int:
        return len(self._lakes)

    @property
    def number_of_multi_lakes(self) -> int:
        piece: int = 0
        for lake in self._lakes:
            if lake.is_multi_countries:
                piece += 1
        return piece

    @property
    def _file_lines(self) -> list[str]:
        lines: list[str] = []
        # fejléc:
        lines.append("Tó;Terület_km2\n")
        # adatsorok:
        for lake in self._lakes:
            lines.append(f"{lake.name};{lake.area}\n")
        return lines

    def __init__(self, source_name: str) -> None:
        with open(source_name, "r", encoding="utf-8") as file:
            for line in file.read().splitlines()[1:]:  # [1:] - első sor kihagyása
                self._lakes.append(Lake(line))

    @property
    def _stat(self) -> dict[int, int]: #szótár,statisztika 
        d: dict[int, int] = {}
        for lake in self._lakes:
            noc: int = lake.number_of_countries              # ne keljen többször írni
            if noc in d:
                d[noc] += 1
            else:               # ha ez az első akkor az lesz 1
                d[noc] = 1
        return d

    @property
    def statistics(self) -> str:
        r: str = ""
        for k, v in self._stat.items():   # key,value
            r += f"\t{k} ország területén {v} darab tó fekszik.\n"
        return r



    def there_are_n_countires_lakes(self, n: int) -> bool:  # fgv. mert igazzal vagy hamissal tér vissza
        for lake in self._lakes:
            if lake.is_n_countries_lake(n):
                return True
        return False

    # Írás
    def create_new_file(self, filme_name: str) -> None:
        with open(filme_name, "w", encoding="utf-8") as file:
            file.writelines(self._file_lines)