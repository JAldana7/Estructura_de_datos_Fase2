from tkinter import messagebox
from models.seguridad import Seguridad
from views.registrar_cliente_view import RegistroClienteView
from controllers.gestion_controller import GestionController

class LoginController:
    """Controlador que maneja la lógica de login y conecta la vista con el modelo."""

    def __init__(self, view):
        self._view = view
        self._seguridad = Seguridad()

        # Conectar el controlador a la vista
        self._view.set_controller(self)

    def procesar_login(self):
        """Valida la clave ingresada en la vista."""
        clave_ingresada = self._view.txt_password.get()

        if not clave_ingresada:
            messagebox.showwarning("Atención", "Por favor, ingrese la contraseña.")
            return

        # Validar credenciales con el modelo
        if self._seguridad.validar_contrasena(clave_ingresada):
            messagebox.showinfo("Acceso Exitoso", "¡Bienvenido al sistema Sabor & Sazón!")
            
            # 1. Destruir/cerrar la ventana de Login actual
            self._view.destroy()
            
            # 2. CÓDIGO DEL PUNTO 3 (VA AQUÍ AL FINAL)
            app_registro = RegistroClienteView()
            controller_registro = GestionController(app_registro)  # Asocia el controlador a la vista
            app_registro.mainloop()

        else:
            messagebox.showerror("Acceso Denegado", "Contraseña incorrecta. Intente nuevamente.")
            self._txt_password_limpiar()

    def _txt_password_limpiar(self):
        """Limpia el campo de texto y le da foco de nuevo."""
        self._view.txt_password.delete(0, 'end')
        self._view.txt_password.focus()