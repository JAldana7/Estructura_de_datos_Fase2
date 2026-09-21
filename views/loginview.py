import sys
import os
import tkinter as tk
import ctypes
from tkinter import ttk, messagebox

# Permitir ejecuciones directas resolviendo la ruta raíz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class LoginView(tk.Tk):
    def __init__(self):
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1) #mejorar la resolucion
        except:
            pass
        super().__init__()

        # Configuración de la ventana principal
        self.title("Sabor & Sazón — Acceso")
        self.geometry("600x580")
        self.configure(bg="#F4F6F8")
        self.resizable(False, False)

        # Estado para mostrar/ocultar contraseña
        self._password_visible = False

        # Configuración de estilos visuales
        self._configurar_estilos()

        # Construir la interfaz
        self._crear_interfaz()

    def _configurar_estilos(self):
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

        self.COLOR_VERDE = "#0F4C3A"
        self.COLOR_FONDO = "#F4F6F8"

        self.style.configure(".", background=self.COLOR_FONDO)
        self.style.configure("Card.TFrame", background="#FFFFFF")
        self.style.configure("Header.TFrame", background=self.COLOR_VERDE)

        # Estilo para el botón principal de ingreso
        self.style.configure("Login.TButton", 
                             font=("Segoe UI", 10, "bold"), 
                             background=self.COLOR_VERDE, 
                             foreground="#FFFFFF")
        self.style.map("Login.TButton", background=[("active", "#0B3B2D")])

    def _crear_interfaz(self):
        # -------------------------------------------------------------
        # 1. BANNER / ENCABEZADO SUPERIOR
        # -------------------------------------------------------------
        header_frame = ttk.Frame(self, style="Header.TFrame", padding=(25, 20))
        header_frame.pack(fill="x", side="top")

        # Contenedor de la izquierda (Logo y subtítulo)
        left_header = tk.Frame(header_frame, bg=self.COLOR_VERDE)
        left_header.pack(side="left")

        lbl_logo = tk.Label(
            left_header, 
            text="🧑‍🍳 Sabor & Sazón", 
            font=("Segoe UI", 20, "bold"), 
            bg=self.COLOR_VERDE, 
            fg="#FFFFFF"
        )
        lbl_logo.pack(anchor="w")

        lbl_subtitulo_header = tk.Label(
            left_header, 
            text="Sistema de Gestión de Clientes", 
            font=("Segoe UI", 11), 
            bg=self.COLOR_VERDE, 
            fg="#D1E7DD"
        )
        lbl_subtitulo_header.pack(anchor="w", pady=(2, 0))

        # Texto decorativo a la derecha
        lbl_slogan = tk.Label(
            header_frame, 
            text="Buena comida,\nmejores momentos", 
            font=("Segoe UI", 11, "italic"), 
            bg=self.COLOR_VERDE, 
            fg="#A7F3D0",
            justify="right"
        )
        lbl_slogan.pack(side="right")

        # -------------------------------------------------------------
        # 2. TARJETA BLANCA CONTENEDORA (LOGIN)
        # -------------------------------------------------------------
        card_frame = ttk.Frame(self, style="Card.TFrame", padding=25)
        card_frame.pack(fill="both", expand=True, padx=35, pady=25)

        # --- SECCIÓN A: Datos del Autor / Estudiante ---
        author_frame = tk.Frame(card_frame, bg="#FFFFFF")
        author_frame.pack(fill="x", pady=(0, 15))

        lbl_avatar = tk.Label(author_frame, text="👤", font=("Segoe UI", 28), bg="#D1E7DD", fg=self.COLOR_VERDE, width=2, height=1)
        lbl_avatar.pack(side="left", padx=(0, 15))

        author_info = tk.Frame(author_frame, bg="#FFFFFF")
        author_info.pack(side="left")

        lbl_nombre_autor = tk.Label(
            author_info, 
            text="Johan David Aldana Castillo", 
            font=("Segoe UI", 12, "bold"), 
            bg="#FFFFFF", 
            fg="#0F172A"
        )
        lbl_nombre_autor.pack(anchor="w")

        lbl_carrera_autor = tk.Label(
            author_info, 
            text="Ingeniería de Sistemas — UNAD", 
            font=("Segoe UI", 10), 
            bg="#FFFFFF", 
            fg="#64748B"
        )
        lbl_carrera_autor.pack(anchor="w")

        # Línea divisora
        ttk.Separator(card_frame, orient="horizontal").pack(fill="x", pady=10)

        # --- SECCIÓN B: Indicaciones de la contraseña ---
        lbl_indicacion_titulo = tk.Label(
            card_frame, 
            text="🛡️  Ingrese la contraseña para continuar", 
            font=("Segoe UI", 11, "bold"), 
            bg="#FFFFFF", 
            fg="#0F172A"
        )
        lbl_indicacion_titulo.pack(anchor="w", pady=(5, 2))

        lbl_indicacion_sub = tk.Label(
            card_frame, 
            text="La contraseña está enmascarada (***).", 
            font=("Segoe UI", 9), 
            bg="#FFFFFF", 
            fg="#64748B"
        )
        lbl_indicacion_sub.pack(anchor="w", pady=(0, 15))

        # --- SECCIÓN C: Campo de Contraseña con icono de visibilidad ---
        input_container = tk.Frame(card_frame, bg="#F8FAFC", highlightbackground="#CBD5E1", highlightthickness=1)
        input_container.pack(fill="x", pady=(0, 20))

        lbl_lock = tk.Label(input_container, text="🔒", font=("Segoe UI", 12), bg="#F8FAFC")
        lbl_lock.pack(side="left", padx=10)

        self.txt_password = tk.Entry(
            input_container, 
            font=("Segoe UI", 11), 
            show="*", 
            bg="#F8FAFC", 
            bd=0, 
            relief="flat"
        )
        self.txt_password.pack(side="left", fill="x", expand=True, pady=8)

        self.btn_toggle_eye = tk.Button(
            input_container, 
            text="👁️", 
            font=("Segoe UI", 10), 
            bg="#F8FAFC", 
            bd=0, 
            cursor="hand2",
            command=self._toggle_password_visibility
        )
        self.btn_toggle_eye.pack(side="right", padx=10)

        # --- SECCIÓN D: Botón Ingresar ---
        self.btn_ingresar = ttk.Button(
            card_frame, 
            text="➔   Ingresar al sistema   ➔", 
            style="Login.TButton"
        )
        self.btn_ingresar.pack(fill="x", ipady=8, pady=(5, 0))

        # -------------------------------------------------------------
        # 3. PIE DE PÁGINA (FOOTER)
        # -------------------------------------------------------------
        footer_frame = tk.Frame(self, bg=self.COLOR_FONDO)
        footer_frame.pack(side="bottom", fill="x", pady=(0, 15))

        lbl_footer = tk.Label(
            footer_frame, 
            text="🛡️  Estructura de Datos  ·  Cod. 301305  ·  ECBTI", 
            font=("Segoe UI", 8), 
            bg=self.COLOR_FONDO, 
            fg="#64748B"
        )
        lbl_footer.pack()

    def _toggle_password_visibility(self):
        """Alterna entre ocultar y mostrar el texto de la contraseña."""
        if self._password_visible:
            self.txt_password.config(show="*")
            self._password_visible = False
        else:
            self.txt_password.config(show="")
            self._password_visible = True

if __name__ == "__main__":
    app = LoginView()
    app.mainloop()