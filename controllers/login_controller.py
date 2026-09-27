#importacion importantes 
from tkinter import messagebox
from models.seguridad import Seguridad
from views.registrar_cliente_view import RegistroClienteView
from controllers.gestion_controller import GestionController

#clase controlador del inicio de sesion
class LoginController:
    #constructor
    def __init__(self, view):
        self._view = view
        self._seguridad = Seguridad()
        self._view.set_controller(self) # Conectar el controlador a la vista

    def procesar_login(self):
        clave_ingresada = self._view.txt_password.get() #Valida la clave ingresada en la vista

        if not clave_ingresada:
            messagebox.showwarning("Atención", "Por favor, ingrese la contraseña.")
            return

        # Validar credenciales con el modelo
        if self._seguridad.validar_contrasena(clave_ingresada):
            messagebox.showinfo("Acceso Exitoso", "¡Bienvenido al sistema Sabor & Sazón!")
            
            self._view.destroy() #cerrar la ventana de Login actual
            
            app_registro = RegistroClienteView()
            controller_registro = GestionController(app_registro)  # Asocia el controlador a la vista
            app_registro.mainloop()
        else:
            messagebox.showerror("Acceso Denegado", "Contraseña incorrecta. Intente nuevamente.")
            self._txt_password_limpiar()

    #Limpiar datos
    def _txt_password_limpiar(self):
        self._view.txt_password.delete(0, 'end')
        self._view.txt_password.focus()