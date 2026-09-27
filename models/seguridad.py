#clase seguridad
class Seguridad:
    #constructor
    def __init__(self, password: str = "1793"):
        self._password = password

    @property
    def password(self) -> str:
        return self._password

    #funcion para validar la contraseña ingresada
    def validar_contrasena(self, contrasena: str) -> bool:
        return contrasena == self._password