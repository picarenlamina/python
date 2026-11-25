import os
import shutil
import tempfile
import tkinter as tk
from tkinter import messagebox

# ==========================================
# 1. MODELO (Operaciones del sistema Windows)
# ==========================================
class LimpiadorModelo:
    """Analiza y limpia la carpeta temporal de usuario de Windows."""

    def __init__(self):
        # Obtiene automáticamente la ruta C:\Users\<Usuario>\AppData\Local\Temp
        self.ruta_temp = tempfile.gettempdir()

    def analizar_espacio(self) -> tuple[int, float]:
        """Devuelve (cantidad_de_archivos, tamaño_total_en_MB)."""
        total_bytes = 0
        cantidad_archivos = 0

        for raiz, _, archivos in os.walk(self.ruta_temp):
            for archivo in archivos:
                ruta_completa = os.path.join(raiz, archivo)
                try:
                    total_bytes += os.path.getsize(ruta_completa)
                    cantidad_archivos += 1
                except OSError:
                    # Ignorar archivos bloqueados o sin permisos
                    continue

        tamano_mb = round(total_bytes / (1024 * 1024), 2)
        return cantidad_archivos, tamano_mb

    def limpiar_temporales(self) -> tuple[int, int]:
        """Elimina archivos y carpetas libres. Devuelve (eliminados, omitidos_en_uso)."""
        eliminados = 0
        omitidos = 0

        for elemento in os.listdir(self.ruta_temp):
            ruta_completa = os.path.join(self.ruta_temp, elemento)
            try:
                if os.path.isfile(ruta_completa) or os.path.islink(ruta_completa):
                    os.unlink(ruta_completa)
                    eliminados += 1
                elif os.path.isdir(ruta_completa):
                    shutil.rmtree(ruta_completa)
                    eliminados += 1
            except OSError:
                # Si Windows o un programa abierto está usando el archivo, se omite sin fallar
                omitidos += 1

        return eliminados, omitidos


# ==========================================
# 2. VISTA (Interfaz Gráfica / Tkinter)
# ==========================================
class LimpiadorVista(tk.Tk):
    """Ventana principal de la herramienta de mantenimiento."""

    def __init__(self):
        super().__init__()
        self.title("Limpiador Temporal Windows (MVC)")
        self.geometry("380x230")
        self.resizable(False, False)
        self._crear_widgets()

    def _crear_widgets(self):
        tk.Label(self, text="Mantenimiento de Archivos Temporales", font=("Segoe UI", 11, "bold")).pack(pady=(15, 5))

        self.lbl_ruta = tk.Label(self, text="Ruta: ...", fg="gray", wraplength=340)
        self.lbl_ruta.pack(pady=2)

        self.lbl_estado = tk.Label(self, text="Pulsa 'Analizar' para calcular espacio", font=("Segoe UI", 10))
        self.lbl_estado.pack(pady=15)

        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=10)

        self.btn_analizar = tk.Button(frame_botones, text="1. Analizar", width=14)
        self.btn_analizar.grid(row=0, column=0, padx=8)

        self.btn_limpiar = tk.Button(frame_botones, text="2. Limpiar Ahora", width=14, bg="#28a745", fg="white")
        self.btn_limpiar.grid(row=0, column=1, padx=8)

    def mostrar_ruta(self, ruta: str):
        self.lbl_ruta.config(text=f"Carpeta: {ruta}")

    def actualizar_estado(self, texto: str):
        self.lbl_estado.config(text=texto)

    def confirmar_limpieza(self) -> bool:
        return messagebox.askyesno(
            "Confirmar limpieza",
            "¿Deseas eliminar los archivos temporales que no estén en uso?"
        )

    def mostrar_resultado(self, mensaje: str):
        messagebox.showinfo("Limpieza completada", mensaje)


# ==========================================
# 3. CONTROLADOR (Coordinación)
# ==========================================
class LimpiadorControlador:
    """Conecta las acciones del usuario con el análisis y limpieza en Windows."""

    def __init__(self, modelo: LimpiadorModelo, vista: LimpiadorVista):
        self.modelo = modelo
        self.vista = vista

        self.vista.mostrar_ruta(self.modelo.ruta_temp)
        self.vista.btn_analizar.config(command=self.analizar)
        self.vista.btn_limpiar.config(command=self.limpiar)

    def analizar(self):
        archivos, mb = self.modelo.analizar_espacio()
        self.vista.actualizar_estado(f"Encontrados: {archivos} archivos ({mb} MB)")

    def limpiar(self):
        if not self.vista.confirmar_limpieza():
            return

        eliminados, omitidos = self.modelo.limpiar_temporales()
        self.vista.mostrar_resultado(
            f"Elementos eliminados: {eliminados}\n"
            f"Omitidos (en uso por Windows): {omitidos}"
        )
        # Vuelve a analizar para reflejar el nuevo estado en pantalla
        self.analizar()


# ==========================================
# PUNTO DE ENTRADA
# ==========================================
if __name__ == "__main__":
    modelo = LimpiadorModelo()
    vista = LimpiadorVista()
    controlador = LimpiadorControlador(modelo, vista)

    vista.mainloop()