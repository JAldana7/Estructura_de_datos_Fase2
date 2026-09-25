from models.menu import Menu # importamos menu
from datetime import datetime # importamos la libreria para guardar fecha automaticamente

#clase gestionar clientes
class GestionClientes:
    #constructor de la clase gestionclientes
    def __init__(self,
                identificacion: str,
                nombre: str,
                genero: str,
                menu: Menu,
                numero_sesiones: int):
        self._identificacion = identificacion
        self._nombre = nombre
        self._genero = genero
        self._menu = menu
        self._numero_sesiones = numero_sesiones
        self._costo_sesion = Menu.costo_sesion
        self._fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Getters para los datos encapsulados
    @property
    def identificacion(self) -> str:
        return self._identificacion

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def genero(self) -> str:
        return self._genero

    @property
    def menu(self) -> Menu:
        return self._menu

    @property
    def numero_sesiones(self) -> int:
        return self._numero_sesiones

    @property
    def costo_sesion(self) -> float:
        return self._costo_sesion
    @property
    def fecha_registro(self) -> str:
        return self._fecha_registro

    #metodo para calcular el costo total
    def calcular_costo_total(self) -> float:
        self.costo_total = self._numero_sesiones * self.menu.costo_sesion
        return self.costo_total