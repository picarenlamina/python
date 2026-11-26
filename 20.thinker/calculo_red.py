import ipaddress
import tkinter as tk
from tkinter import messagebox
# ==========================================
# 1. MODELO (Lógica de redes y validación)
# ==========================================
class RedModelo:
    """Calcula la dirección de red a partir de una IP y una máscara."""
    
    def calcular_direccion_red(self, ip: str, mascara: str) -> str:
        ip = ip.strip()
        # Limpia la barra "/" por si el usuario escribe "/24" en vez de "24"
        mascara = mascara.strip().lstrip("/")
        
        if not ip or not mascara:
            raise ValueError("Debes completar ambos campos.")
            
        try:
            # strict=False permite pasar cualquier IP de host (ej. 192.168.1.45)
            # y extraer automáticamente su dirección base de red (192.168.1.0)
            red = ipaddress.IPv4Network(f"{ip}/{mascara}", strict=False)
            return str(red.network_address)
        except ValueError:
            raise ValueError("Dirección IP o máscara de subred no válidas.")


# ==========================================
# 2. VISTA (Interfaz Gráfica / Tkinter)
# ==========================================
class RedVista(tk.Tk):
    """Construye la ventana y expone métodos para leer y mostrar datos."""
    
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Red MVC")
        self.geometry("320x270")
        self.resizable(False, False)
        self._crear_widgets()

    def _crear_widgets(self):
        # Campo 1: Dirección IP
        tk.Label(self, text="Dirección IP (ej. 192.168.1.45):").pack(pady=(15, 2))
        self.entry_ip = tk.Entry(self, width=25, justify="center")
        self.entry_ip.pack(pady=2)

        # Campo 2: Máscara de subred
        tk.Label(self, text="Máscara (ej. 255.255.255.0 o 24):").pack(pady=(10, 2))
        self.entry_mascara = tk.Entry(self, width=25, justify="center")
        self.entry_mascara.pack(pady=2)

        # Botón de acción
        self.boton_calcular = tk.Button(self, text="Calcular Dirección de Red")
        self.boton_calcular.pack(pady=15)

        # Campo 3: Resultado (Solo lectura)
        tk.Label(self, text="Dirección de Red:").pack(pady=(5, 2))
        self.entry_resultado = tk.Entry(self, width=25, justify="center", state="readonly")
        self.entry_resultado.pack(pady=2)

    def obtener_datos(self) -> tuple[str, str]:
        return self.entry_ip.get(), self.entry_mascara.get()

    def mostrar_resultado(self, direccion_red: str):
        self.entry_resultado.config(state="normal")
        self.entry_resultado.delete(0, tk.END)
        self.entry_resultado.insert(0, direccion_red)
        self.entry_resultado.config(state="readonly")

    def mostrar_error(self, mensaje: str):
        messagebox.showerror("Error de formato", mensaje)


# ==========================================
# 3. CONTROLADOR (Intermediario)
# ==========================================
class RedControlador:
    """Conecta los eventos de la Vista con la lógica del Modelo."""
    
    def __init__(self, modelo: RedModelo, vista: RedVista):
        self.modelo = modelo
        self.vista = vista
        
        # Enlazar el clic del botón con el método del controlador
        self.vista.boton_calcular.config(command=self.procesar_calculo)

    def procesar_calculo(self):
        ip, mascara = self.vista.obtener_datos()
        
        try:
            direccion_red = self.modelo.calcular_direccion_red(ip, mascara)
            self.vista.mostrar_resultado(direccion_red)
        except ValueError as error:
            self.vista.mostrar_error(str(error))


# ==========================================
# PUNTO DE ENTRADA DE LA APLICACIÓN
# ==========================================
if __name__ == "__main__":
    modelo = RedModelo()
    vista = RedVista()
    controlador = RedControlador(modelo, vista)
    
    vista.mainloop()