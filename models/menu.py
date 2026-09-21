from abc import ABC, abstractmethod

class Menu(ABC):
    def __init__(self, nombre: str):
        self._nombre = nombre

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    @abstractmethod
    def costo_sesion(self) -> float:
        pass

    def __str__(self) -> str:
        return self._nombre

class MenuEjecutivo(Menu):
    def __init__(self):
        super().__init__("Menú ejecutivo")

    @property
    def costo_sesion(self) -> float:
        return 35000.0

class MenuVegetariano(Menu):
    def __init__(self):
        super().__init__("Menú vegetariano")

    @property
    def costo_sesion(self) -> float:
        return 28000.0

class MenuDegustacion(Menu):
    def __init__(self):
        super().__init__("Menú degustacion")

    @property
    def costo_sesion(self) -> float:
        return 75000.0

class MenuInfantil(Menu):
    def __init__(self):
        super().__init__("Menú infantil")

    @property
    def costo_sesion(self) -> float:
        return 20000.0

class MenuGourmet(Menu):
    def __init__(self):
        super().__init__("Menú gourmet")

    @property
    def costo_sesion(self) -> float:
        return 95000.0