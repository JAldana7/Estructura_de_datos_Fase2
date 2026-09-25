import sys
import os
import tkinter as tk
from tkinter import ttk
from models.gestionar_clientes import GestionClientes

# Permitir ejecuciones directas resolviendo la ruta raíz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class ReporteView(tk.Toplevel):
    """Ventana modal para visualizar el reporte detallado del cliente."""

    def __init__(self, parent, cliente: GestionClientes):
        super().__init__(parent)

        self.cliente = cliente

        # Configuración de la ventana
        self.title("Sabor & Sazón — Reporte")
        self.geometry("500x580")
        self.configure(bg="#F4F6F8")
        self.resizable(False, False)

        # Hacer la ventana modal
        self.transient(parent)
        self.grab_set()

        self._configurar_estilos()
        self._crear_interfaz()

    def _configurar_estilos(self):
        self.COLOR_VERDE = "#0F4C3A"
        self.COLOR_FONDO = "#F4F6F8"
        self.COLOR_TARJETA = "#FFFFFF"

        self.style = ttk.Style(self)
        self.style.configure("ReportCard.TFrame", background=self.COLOR_TARJETA)
        
        # Estilos de botones
        self.style.configure("Print.TButton", font=("Segoe UI", 9, "bold"), background="#FFFFFF", foreground="#0F172A")
        self.style.map("Print.TButton", background=[("active", "#E2E8F0")])

        self.style.configure("Close.TButton", font=("Segoe UI", 9, "bold"), background="#FFFFFF", foreground="#EF4444")
        self.style.map("Close.TButton", background=[("active", "#FEE2E2")])

    def _crear_interfaz(self):
        # -------------------------------------------------------------
        # 1. ENCABEZADO VERDE
        # -------------------------------------------------------------
        header_frame = tk.Frame(self, bg=self.COLOR_VERDE, padx=20, pady=15)
        header_frame.pack(fill="x", side="top")

        lbl_header = tk.Label(
            header_frame, 
            text="📋  Reporte — Sabor & Sazón", 
            font=("Segoe UI", 14, "bold"), 
            bg=self.COLOR_VERDE, 
            fg="#FFFFFF"
        )
        lbl_header.pack(anchor="w")

        # Contenedor Principal (Tarjeta General)
        main_container = tk.Frame(self, bg=self.COLOR_FONDO, padx=20, pady=15)
        main_container.pack(fill="both", expand=True)

        # -------------------------------------------------------------
        # 2. TARJETA SUPERIOR: PERFIL DEL CLIENTE
        # -------------------------------------------------------------
        card_cliente = tk.Frame(main_container, bg=self.COLOR_TARJETA, bd=1, relief="solid", highlightbackground="#E2E8F0", padx=15, pady=12)
        card_cliente.pack(fill="x", pady=(0, 12))

        # Avatar con iniciales
        iniciales = "".join([n[0].upper() for n in self.cliente.nombre.split()[:2]]) if self.cliente.nombre else "CL"
        lbl_avatar = tk.Label(
            card_cliente, 
            text=iniciales, 
            font=("Segoe UI", 14, "bold"), 
            bg="#D1E7DD", 
            fg=self.COLOR_VERDE, 
            width=3, 
            height=2
        )
        lbl_avatar.pack(side="left", padx=(0, 15))

        info_user_frame = tk.Frame(card_cliente, bg=self.COLOR_TARJETA)
        info_user_frame.pack(side="left")

        lbl_nombre = tk.Label(
            info_user_frame, 
            text=self.cliente.nombre, 
            font=("Segoe UI", 13, "bold"), 
            bg=self.COLOR_TARJETA, 
            fg="#0F172A"
        )
        lbl_nombre.pack(anchor="w")

        lbl_subinfo = tk.Label(
            info_user_frame, 
            text=f"ID: {self.cliente.identificacion}   |   {self.cliente.genero}", 
            font=("Segoe UI", 10), 
            bg=self.COLOR_TARJETA, 
            fg="#64748B"
        )
        lbl_subinfo.pack(anchor="w")

        # -------------------------------------------------------------
        # 3. TARJETA INFERIOR: DETALLE DEL SERVICIO Y COSTOS
        # -------------------------------------------------------------
        card_detalle = tk.Frame(main_container, bg=self.COLOR_TARJETA, bd=1, relief="solid", highlightbackground="#E2E8F0", padx=15, pady=15)
        card_detalle.pack(fill="both", expand=True, pady=(0, 15))

        # Fila A: Tipo de Menú
        self._crear_fila_detalle(card_detalle, "🍱  Tipo de menú", self.cliente.menu.nombre)
        
        # Fila B: Sesiones Tomadas
        self._crear_fila_detalle(card_detalle, "📅  Sesiones tomadas", str(self.cliente.numero_sesiones))

        # Fila C: Costo por Sesión
        self._crear_fila_detalle(card_detalle, "💵  Costo por sesión", f"$ {self.cliente.costo_sesion:,.0f}")

        # Fila D: Fecha de Registro
        self._crear_fila_detalle(card_detalle, "🗓️  Fecha de registro", self.cliente.fecha_registro)

        # Separador visual
        ttk.Separator(card_detalle, orient="horizontal").pack(fill="x", pady=15)

        # --- SECCIÓN DESTACADA: COSTO TOTAL DEL SERVICIO ---
        frame_costo_total = tk.Frame(card_detalle, bg=self.COLOR_TARJETA)
        frame_costo_total.pack(fill="x", pady=(0, 5))

        lbl_tag_costo = tk.Label(
            frame_costo_total, 
            text=" 💰 Costo total del servicio ", 
            font=("Segoe UI", 10, "bold"), 
            bg="#D1E7DD", 
            fg=self.COLOR_VERDE
        )
        lbl_tag_costo.pack(side="left")

        costo_total_val = self.cliente.calcular_costo_total()
        lbl_val_costo = tk.Label(
            frame_costo_total, 
            text=f"$ {costo_total_val:,.0f}", 
            font=("Segoe UI", 16, "bold"), 
            bg="#D1E7DD", 
            fg=self.COLOR_VERDE,
            padx=10,
            pady=3
        )
        lbl_val_costo.pack(side="right")

        # Fórmula explicativa en cursiva
        lbl_formula = tk.Label(
            card_detalle, 
            text=f"costoTotal = {self.cliente.numero_sesiones} sesiones × $ {self.cliente.costo_sesion:,.0f}", 
            font=("Segoe UI", 9, "italic"), 
            bg=self.COLOR_TARJETA, 
            fg="#64748B"
        )
        lbl_formula.pack(anchor="w", pady=(5, 0))

        # -------------------------------------------------------------
        # 4. BOTONES INFERIORES
        # -------------------------------------------------------------
        frame_botones = tk.Frame(main_container, bg=self.COLOR_FONDO)
        frame_botones.pack(fill="x")

        frame_botones.columnconfigure(0, weight=1)
        frame_botones.columnconfigure(1, weight=1)

        btn_imprimir = ttk.Button(frame_botones, text="🖨️   Imprimir", style="Print.TButton")
        btn_imprimir.grid(row=0, column=0, sticky="ew", padx=(0, 5), ipady=6)

        btn_cerrar = ttk.Button(frame_botones, text="❌   Cerrar reporte", style="Close.TButton", command=self.destroy)
        btn_cerrar.grid(row=0, column=1, sticky="ew", padx=(5, 0), ipady=6)

    def _crear_fila_detalle(self, parent, etiqueta, valor):
        """Crea una fila alineada clave-valor."""
        f = tk.Frame(parent, bg=self.COLOR_TARJETA)
        f.pack(fill="x", pady=6)

        lbl_e = tk.Label(f, text=etiqueta, font=("Segoe UI", 10), bg=self.COLOR_TARJETA, fg="#334155")
        lbl_e.pack(side="left")

        lbl_v = tk.Label(f, text=valor, font=("Segoe UI", 10, "bold"), bg=self.COLOR_TARJETA, fg="#0F172A")
        lbl_v.pack(side="right")