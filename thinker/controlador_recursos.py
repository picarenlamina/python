import os
import tkinter as tk
from tkinter import ttk, messagebox
import psutil

# ==========================================
# 1. MODELO (Consulta al sistema operativo)
# ==========================================
class MonitorModelo:
    """Obtiene métricas de hardware y gestiona los procesos del sistema."""

    def obtener_metricas_sistema(self) -> dict:
        # interval=None evita bloquear el programa esperando una muestra de CPU
        cpu = psutil.cpu_percent(interval=None)
        ram = psutil.virtual_memory().percent
        # os.path.abspath(os.sep) detecta la raíz del disco principal (C:\ en Windows, / en Linux/Mac)
        disco = psutil.disk_usage(os.path.abspath(os.sep)).percent
        
        return {
            "cpu": cpu,
            "ram": ram,
            "disco": disco
        }

    def obtener_top_procesos(self, limite: int = 10) -> list[dict]:
        procesos = []
        # Iteramos de forma segura solicitando solo los atributos necesarios
        for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
            try:
                info = proc.info
                if info['memory_info'] is not None:
                    # Convertir bytes a Megabytes (MB)
                    memoria_mb = info['memory_info'].rss / (1024 * 1024)
                    procesos.append({
                        "pid": info['pid'],
                        "nombre": info['name'],
                        "memoria_mb": round(memoria_mb, 1)
                    })
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Ignorar procesos del sistema protegidos o que cerraron mientras leíamos
                continue

        # Ordenar de mayor a menor consumo de RAM y devolver solo los 'limite' primeros
        procesos.sort(key=lambda p: p["memoria_mb"], reverse=True)
        return procesos[:limite]

    def terminar_proceso(self, pid: int):
        try:
            proceso = psutil.Process(pid)
            proceso.terminate()
        except psutil.NoSuchProcess:
            raise ValueError("El proceso ya no existe.")
        except psutil.AccessDenied:
            raise PermissionError("Acceso denegado. Ejecuta como Administrador para cerrar este proceso.")


# ==========================================
# 2. VISTA (Interfaz Gráfica / Tkinter)
# ==========================================
class MonitorVista(tk.Tk):
    """Dibuja barras de progreso, la tabla de procesos y botones de control."""

    def __init__(self):
        super().__init__()
        self.title("Monitor de Recursos MVC")
        self.geometry("520x440")
        self.resizable(False, False)
        self._crear_widgets()

    def _crear_widgets(self):
        # --- SECCIÓN SUPERIOR: Métricas de Hardware ---
        frame_metricas = tk.LabelFrame(self, text="Uso de Recursos en Tiempo Real", padx=15, pady=10)
        frame_metricas.pack(fill="x", padx=15, pady=10)

        # CPU
        self.lbl_cpu = tk.Label(frame_metricas, text="CPU: 0.0%", width=15, anchor="w")
        self.lbl_cpu.grid(row=0, column=0, pady=4)
        self.bar_cpu = ttk.Progressbar(frame_metricas, length=310, maximum=100)
        self.bar_cpu.grid(row=0, column=1, padx=10)

        # RAM
        self.lbl_ram = tk.Label(frame_metricas, text="RAM: 0.0%", width=15, anchor="w")
        self.lbl_ram.grid(row=1, column=0, pady=4)
        self.bar_ram = ttk.Progressbar(frame_metricas, length=310, maximum=100)
        self.bar_ram.grid(row=1, column=1, padx=10)

        # Disco
        self.lbl_disco = tk.Label(frame_metricas, text="Disco: 0.0%", width=15, anchor="w")
        self.lbl_disco.grid(row=2, column=0, pady=4)
        self.bar_disco = ttk.Progressbar(frame_metricas, length=310, maximum=100)
        self.bar_disco.grid(row=2, column=1, padx=10)

        # --- SECCIÓN CENTRAL: Tabla de Top 10 Procesos ---
        frame_tabla = tk.LabelFrame(self, text="Top 10 Procesos por Consumo de RAM", padx=10, pady=10)
        frame_tabla.pack(fill="both", expand=True, padx=15, pady=5)

        columnas = ("pid", "nombre", "memoria")
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=10)
        
        self.tabla.heading("pid", text="PID")
        self.tabla.heading("nombre", text="Nombre del Proceso")
        self.tabla.heading("memoria", text="Memoria (MB)")

        self.tabla.column("pid", width=80, anchor="center")
        self.tabla.column("nombre", width=260, anchor="w")
        self.tabla.column("memoria", width=110, anchor="e")
        self.tabla.pack(fill="both", expand=True)

        # --- SECCIÓN INFERIOR: Botón de Acción ---
        self.btn_finalizar = tk.Button(self, text="Finalizar Proceso Seleccionado", bg="#d9534f", fg="white")
        self.btn_finalizar.pack(pady=12)

    # Métodos públicos para que el Controlador actualice la pantalla
    def actualizar_metricas(self, metricas: dict):
        self.lbl_cpu.config(text=f"CPU: {metricas['cpu']:.1f}%")
        self.bar_cpu["value"] = metricas["cpu"]

        self.lbl_ram.config(text=f"RAM: {metricas['ram']:.1f}%")
        self.bar_ram["value"] = metricas["ram"]

        self.lbl_disco.config(text=f"Disco: {metricas['disco']:.1f}%")
        self.bar_disco["value"] = metricas["disco"]

    def actualizar_tabla(self, procesos: list[dict]):
        # Guardamos qué PID estaba seleccionado antes de refrescar la tabla
        pid_seleccionado = self.obtener_pid_seleccionado()

        # Limpiamos filas anteriores
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Insertamos las nuevas filas
        for proc in procesos:
            item_id = self.tabla.insert("", tk.END, values=(proc["pid"], proc["nombre"], f"{proc['memoria_mb']} MB"))
            # Si este proceso estaba seleccionado antes del refresco, mantenemos la selección
            if proc["pid"] == pid_seleccionado:
                self.tabla.selection_set(item_id)

    def obtener_pid_seleccionado(self) -> int | None:
        seleccion = self.tabla.selection()
        if not seleccion:
            return None
        valores = self.tabla.item(seleccion[0], "values")
        return int(valores[0])

    def confirmar_accion(self, mensaje: str) -> bool:
        return messagebox.askyesno("Confirmar", mensaje)

    def mostrar_mensaje(self, titulo: str, mensaje: str, es_error: bool = False):
        if es_error:
            messagebox.showerror(titulo, mensaje)
        else:
            messagebox.showinfo(titulo, mensaje)


# ==========================================
# 3. CONTROLADOR (Ciclo de actualización)
# ==========================================
class MonitorControlador:
    """Coordina el refresco automático cada 2 segundos y los eventos del usuario."""

    def __init__(self, modelo: MonitorModelo, vista: MonitorVista):
        self.modelo = modelo
        self.vista = vista

        # Enlazar botón
        self.vista.btn_finalizar.config(command=self.finalizar_proceso_seleccionado)

        # Iniciar el ciclo automático de actualización
        self.refrescar_datos()

    def refrescar_datos(self):
        # 1. Consultar datos frescos al Modelo
        metricas = self.modelo.obtener_metricas_sistema()
        procesos = self.modelo.obtener_top_procesos(limite=10)

        # 2. Actualizar la Vista
        self.vista.actualizar_metricas(metricas)
        self.vista.actualizar_tabla(procesos)

        # 3. Programar la próxima ejecución dentro de 2000 ms (2 segundos) sin bloquear la GUI
        self.vista.after(2000, self.refrescar_datos)

    def finalizar_proceso_seleccionado(self):
        pid = self.vista.obtener_pid_seleccionado()
        if pid is None:
            self.vista.mostrar_mensaje("Aviso", "Selecciona primero un proceso de la tabla.", es_error=True)
            return

        if not self.vista.confirmar_accion(f"¿Seguro que deseas finalizar el proceso con PID {pid}?"):
            return

        try:
            self.modelo.terminar_proceso(pid)
            self.vista.mostrar_mensaje("Éxito", f"Proceso {pid} finalizado correctamente.")
            # Actualizar inmediatamente sin esperar los 2 segundos
            metricas = self.modelo.obtener_metricas_sistema()
            procesos = self.modelo.obtener_top_procesos(limite=10)
            self.vista.actualizar_metricas(metricas)
            self.vista.actualizar_tabla(procesos)
        except (ValueError, PermissionError) as error:
            self.vista.mostrar_mensaje("Error", str(error), es_error=True)


# ==========================================
# PUNTO DE ENTRADA
# ==========================================
if __name__ == "__main__":
    modelo = MonitorModelo()
    vista = MonitorVista()
    controlador = MonitorControlador(modelo, vista)
    
    vista.mainloop()