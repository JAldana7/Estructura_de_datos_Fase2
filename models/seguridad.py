"""
Autor: Johan Aldana
Fecha: 24/09/2026
Fuente: Autoria propia
"""

class Seguridad:
    def __init__(self, password: str = "1793"):
        self._password = password

    @property
    def password(self) -> str:
        return self._password
    
    def validar_contrasena(self, contrasena: str) -> bool:
        return contrasena == self._password