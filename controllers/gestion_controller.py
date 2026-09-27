#Importaciones importantes
from tkinter import messagebox
from typing import List, Optional
from models.gestionar_clientes import GestionClientes
from models.menu import Menu
from views.reporte_view import ReporteView

#clase gestion controller
class GestionController:
    #constructor
    def __init__(self, view):
        self._view = view
        self._lista_clientes: List[GestionClientes] = [] # Lista interna para almacenar los registros creados
        self._cliente_actual: Optional[GestionClientes] = None 

        self._view.set_controller(self) # Conectar el controlador con la vista

    #Funcion para guardar los registros
    def guardar_registro(self) -> bool:
        #Valida y guarda los datos ingresados en el formulario.
        identificacion = self._view.txt_identificacion.get().strip()
        nombre = self._view.txt_nombre.get().strip()
        genero = self._view.var_genero.get()
        nombre_menu = self._view.cmb_menu.get()
        str_sesiones = self._view.txt_sesiones.get().strip()

        # Validaciones del formularios
        if not identificacion:
            messagebox.showwarning("Atención", "Por favor, ingrese el documento de Identificación.")
            self._view.txt_identificacion.focus()
            return False

        if not nombre:
            messagebox.showwarning("Atención", "Por favor, ingrese el Nombre Completo.")
            self._view.txt_nombre.focus()
            return False

        if nombre_menu not in self._view.menus_disponibles:
            messagebox.showwarning("Atención", "Por favor, seleccione un Tipo de Menú válido.")
            self._view.cmb_menu.focus()
            return False

        if not str_sesiones:
            messagebox.showwarning("Atención", "Por favor, ingrese el Número de Sesiones.")
            self._view.txt_sesiones.focus()
            return False

        try:
            sesiones = int(str_sesiones)
            if sesiones <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Dato Inválido", "El número de sesiones debe ser un número entero mayor a 0.")
            self._view.txt_sesiones.delete(0, 'end')
            self._view.txt_sesiones.focus()
            return False

        menu_obj: Menu = self._view.menus_disponibles[nombre_menu] #Conectar el controlador con la vista

        nuevo_cliente = GestionClientes(
            identificacion = identificacion,
            nombre = nombre, 
            genero = genero,
            menu = menu_obj,
            numero_sesiones = sesiones
        )

        # Almacenar en la lista del controlador
        self._lista_clientes.append(nuevo_cliente)
        self._cliente_actual = nuevo_cliente

        messagebox.showinfo("Éxito", f"Registro del cliente '{nombre}' guardado correctamente.")
        return True

    #funcion para mostra el reporte del cliente guardado
    def mostrar_reporte(self):
        if self._cliente_actual is None or self._hay_cambios_en_formulario():
            exito = self.guardar_registro()
            if not exito:
                return

        ReporteView(parent=self._view, cliente=self._cliente_actual) # Abrir la ventana emergente con la información del cliente

    # Funcion para verifica si los campos en la vista difieren del cliente guardado actualmente
    def _hay_cambios_en_formulario(self) -> bool:
        if not self._cliente_actual:
            return True
            
        str_sesiones = self._view.txt_sesiones.get().strip()
        sesiones_actuales = int(str_sesiones) if str_sesiones.isdigit() else 0

        nombre_menu_guardado = getattr(self._cliente_actual.menu, 'tipo_menu', getattr(self._cliente_actual.menu, 'nombre', ''))

        return (
            self._view.txt_identificacion.get().strip() != self._cliente_actual.identificacion or
            self._view.txt_nombre.get().strip() != self._cliente_actual.nombre or
            self._view.var_genero.get() != self._cliente_actual.genero or
            self._view.cmb_menu.get() != nombre_menu_guardado or
            sesiones_actuales != self._cliente_actual.numero_sesiones
        )