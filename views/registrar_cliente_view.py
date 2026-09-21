import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import ctypes
from models.menu import (
    MenuEjecutivo, MenuVegetariano, MenuDegustacion, 
    MenuInfantil, MenuGourmet
)

class RegistroClienteView(tk.Tk):
    def __init__(self):
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1) #mejorar la resolucion
        except:
            pass
        super().__init__()

        # Configuración principal
        self.title("Sabor & Sazón — Registro de Cliente")
        self.geometry("750x600")
        self.configure(bg="#F4F6F8")
        self.resizable(False, False)

        # Mapeo de objetos de Menú
        self.menus_disponibles = {
            "Menú ejecutivo": MenuEjecutivo(),
            "Menú vegetariano": MenuVegetariano(),
            "Menú degustación": MenuDegustacion(),
            "Menú infantil": MenuInfantil(),
            "Menú gourmet": MenuGourmet()
        }

        # Configurar estilos visuales de TTK
        self._configurar_estilos()

        # Construir la interfaz
        self._crear_interfaz()

    def _configurar_estilos(self):
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

        # Colores principales
        self.COLOR_VERDE = "#0F4C3A"
        self.COLOR_FONDO = "#F4F6F8"
        
        # Estilos generales
        self.style.configure(".", background=self.COLOR_FONDO)
        self.style.configure("Card.TFrame", background="#FFFFFF", relief="flat")
        self.style.configure("Header.TFrame", background=self.COLOR_VERDE)

        # Etiquetas (Labels)
        self.style.configure("FieldLabel.TLabel", background="#FFFFFF", foreground="#334155", font=("Segoe UI", 9, "bold"))
        self.style.configure("Info.TLabel", background="#FFFFFF", foreground="#64748B", font=("Segoe UI", 8, "italic"))

        # RadioButtons
        self.style.configure("Custom.TRadiobutton", background="#FFFFFF", font=("Segoe UI", 9), foreground="#334155")

        # Botones
        self.style.configure("Main.TButton", font=("Segoe UI", 9, "bold"), background=self.COLOR_VERDE, foreground="#FFFFFF")
        self.style.map("Main.TButton", background=[("active", "#0B3B2D")])

        self.style.configure("Secondary.TButton", font=("Segoe UI", 9, "bold"), background="#E2E8F0", foreground="#0F172A")
        self.style.map("Secondary.TButton", background=[("active", "#CBD5E1")])

        self.style.configure("Exit.TButton", font=("Segoe UI", 9, "bold"), background="#FFFFFF", foreground="#EF4444")
        self.style.map("Exit.TButton", background=[("active", "#FEE2E2")])

    def _crear_interfaz(self):
        # -------------------------------------------------------------
        # 1. ENCABEZADO / BANNER SUPERIOR
        # -------------------------------------------------------------
        header_frame = ttk.Frame(self, style="Header.TFrame", padding=(20, 15))
        header_frame.pack(fill="x", side="top")

        lbl_logo = tk.Label(header_frame, text="🍴", font=("Segoe UI", 24), bg=self.COLOR_VERDE, fg="#FFFFFF")
        lbl_logo.pack(side="left", padx=(0, 10))

        text_container = tk.Frame(header_frame, bg=self.COLOR_VERDE)
        text_container.pack(side="left")

        lbl_titulo = tk.Label(text_container, text="Registro de Cliente", font=("Segoe UI", 16, "bold"), bg=self.COLOR_VERDE, fg="#FFFFFF")
        lbl_titulo.pack(anchor="w")

        lbl_subtitulo = tk.Label(text_container, text="Completa la información del cliente para continuar", font=("Segoe UI", 9), bg=self.COLOR_VERDE, fg="#D1E7DD")
        lbl_subtitulo.pack(anchor="w")

        lbl_marca = tk.Label(header_frame, text=" Sabor & Sazón", font=("Segoe UI", 12, "bold", "italic"), bg=self.COLOR_VERDE, fg="#FFFFFF")
        lbl_marca.pack(side="right")

        # -------------------------------------------------------------
        # 2. TARJETA CONTENEDORA (FORMULARIO)
        # -------------------------------------------------------------
        card_frame = ttk.Frame(self, style="Card.TFrame", padding=20)
        card_frame.pack(fill="both", expand=True, padx=20, pady=15)

        card_frame.columnconfigure(0, weight=1)
        card_frame.columnconfigure(1, weight=1)

        # 1. Identificación y Nombre
        ttk.Label(card_frame, text=" Identificación *", style="FieldLabel.TLabel").grid(row=0, column=0, sticky="w", pady=(5, 2))
        self.txt_identificacion = ttk.Entry(card_frame, width=30)
        self.txt_identificacion.grid(row=1, column=0, sticky="ew", padx=(0, 10), pady=(0, 10))

        ttk.Label(card_frame, text=" Nombre completo *", style="FieldLabel.TLabel").grid(row=0, column=1, sticky="w", pady=(5, 2))
        self.txt_nombre = ttk.Entry(card_frame, width=30)
        self.txt_nombre.grid(row=1, column=1, sticky="ew", padx=(10, 0), pady=(0, 10))

        # 2. Género
        ttk.Label(card_frame, text=" Género *", style="FieldLabel.TLabel").grid(row=2, column=0, columnspan=2, sticky="w", pady=(5, 2))
        self.var_genero = tk.StringVar(value="Masculino")

        frame_genero = ttk.Frame(card_frame, style="Card.TFrame")
        frame_genero.grid(row=3, column=0, columnspan=2, sticky="w", pady=(0, 10))

        ttk.Radiobutton(frame_genero, text="♂ Masculino", value="Masculino", variable=self.var_genero, style="Custom.TRadiobutton").pack(side="left", padx=(0, 20))
        ttk.Radiobutton(frame_genero, text="♀ Femenino", value="Femenino", variable=self.var_genero, style="Custom.TRadiobutton").pack(side="left")

        # 3. Menú y Costo
        ttk.Label(card_frame, text=" Tipo de menú *", style="FieldLabel.TLabel").grid(row=4, column=0, sticky="w", pady=(5, 2))
        self.cmb_menu = ttk.Combobox(card_frame, values=list(self.menus_disponibles.keys()), state="readonly")
        self.cmb_menu.set("Selecciona un tipo de menú")
        self.cmb_menu.grid(row=5, column=0, sticky="ew", padx=(0, 10), pady=(0, 10))
        self.cmb_menu.bind("<<ComboboxSelected>>", self._actualizar_costo_sesion)

        ttk.Label(card_frame, text=" Costo por sesión", style="FieldLabel.TLabel").grid(row=4, column=1, sticky="w", pady=(5, 2))
        self.txt_costo_sesion = ttk.Entry(card_frame, width=30)
        self.txt_costo_sesion.grid(row=5, column=1, sticky="ew", padx=(10, 0), pady=(0, 10))
        self.txt_costo_sesion.config(state="disabled")  # Propiedad Enabled = False

        # 4. Sesiones y Fecha
        ttk.Label(card_frame, text=" Número de sesiones *", style="FieldLabel.TLabel").grid(row=6, column=0, sticky="w", pady=(5, 2))
        self.txt_sesiones = ttk.Entry(card_frame, width=30)
        self.txt_sesiones.grid(row=7, column=0, sticky="ew", padx=(0, 10), pady=(0, 10))

        ttk.Label(card_frame, text=" Fecha de registro", style="FieldLabel.TLabel").grid(row=6, column=1, sticky="w", pady=(5, 2))
        self.txt_fecha = ttk.Entry(card_frame, width=30)
        self.txt_fecha.insert(0, datetime.now().strftime("%d/%m/%Y %H:%M"))
        self.txt_fecha.config(state="disabled")
        self.txt_fecha.grid(row=7, column=1, sticky="ew", padx=(10, 0), pady=(0, 10))

        # Mensaje de campos requeridos
        ttk.Label(card_frame, text="ℹ  Los campos marcados con * son obligatorios.", style="Info.TLabel").grid(row=8, column=0, columnspan=2, sticky="w", pady=(10, 0))

        # -------------------------------------------------------------
        # 3. BARRA DE BOTONES INFERIOR
        # -------------------------------------------------------------
        frame_botones = ttk.Frame(self, padding=(20, 0))
        frame_botones.pack(fill="x", side="bottom", pady=(0, 15))

        frame_botones.columnconfigure(0, weight=1)
        frame_botones.columnconfigure(1, weight=1)
        frame_botones.columnconfigure(2, weight=1)

        self.btn_guardar = ttk.Button(frame_botones, text=" Guardar Registro", style="Secondary.TButton")
        self.btn_guardar.grid(row=0, column=0, sticky="ew", padx=(0, 5), ipady=5)

        self.btn_reporte = ttk.Button(frame_botones, text=" Calcular / Reporte", style="Main.TButton")
        self.btn_reporte.grid(row=0, column=1, sticky="ew", padx=5, ipady=5)

        self.btn_salir = ttk.Button(frame_botones, text="🗑 Salir", style="Exit.TButton", command=self._confirmar_salida)
        self.btn_salir.grid(row=0, column=2, sticky="ew", padx=(5, 0), ipady=5)

    def _actualizar_costo_sesion(self, event):
        """Actualiza la caja deshabilitada con el costo del menú."""
        seleccion = self.cmb_menu.get()
        if seleccion in self.menus_disponibles:
            obj_menu = self.menus_disponibles[seleccion]
            
            # Habilitar temporalmente para modificar valor
            self.txt_costo_sesion.config(state="normal")
            self.txt_costo_sesion.delete(0, tk.END)
            self.txt_costo_sesion.insert(0, f"$ {obj_menu.costo_sesion:,.0f}")
            self.txt_costo_sesion.config(state="disabled")

    def _confirmar_salida(self):
        """Muestra cuadro de diálogo de confirmación."""
        respuesta = messagebox.askyesno("Confirmar salida", "¿Realmente desea salir de la aplicación?")
        if respuesta:
            self.destroy()

if __name__ == "__main__":
    app = RegistroClienteView()
    app.mainloop()