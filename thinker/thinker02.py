import tkinter as tk
from tkinter import messagebox

# ==========================================
# LÓGICA / FUNCIONES DE LA APLICACIÓN
# ==========================================

def sumar():
    """Obtiene los valores de las dos entradas, realiza la suma y muestra el resultado."""
    try:
        # 1. Obtener y convertir a número flotante el texto ingresado en los dos primeros campos
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        # 2. Realizar la operación matemática
        resultado = num1 + num2
        
        # 3. Actualizar el campo de texto del resultado:
        # Tkinter no permite modificar directamente un Entry en estado "readonly", 
        # por lo que debemos cambiarlo temporalmente a "normal".
        entry_resultado.config(state="normal")
        entry_resultado.delete(0, tk.END)          # Limpia el valor anterior (desde el índice 0 al final)
        entry_resultado.insert(0, str(resultado))  # Inserta el nuevo resultado como texto
        entry_resultado.config(state="readonly")    # Bloquea de nuevo la caja para evitar edición manual
        
    except ValueError:
        # Se activa si el usuario ingresa letras, símbolos o deja los campos vacíos
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")


# ==========================================
# CONFIGURACIÓN DE LA VENTANA PRINCIPAL
# ==========================================

ventana = tk.Tk()
ventana.title("Suma con 3 Textbox")
ventana.geometry("300x260")     # Establece el tamaño de la ventana (ancho x alto)
ventana.resizable(False, False) # Deshabilita la opción de redimensionar la ventana


# ==========================================
# INTERFAZ GRÁFICA (WIDGETS)
# ==========================================

# Campo 1: Etiqueta y caja de texto para el primer número
label1 = tk.Label(ventana, text="Primer número:")
label1.pack(pady=(15, 2))  # Margen externo vertical: 15px arriba, 2px abajo

entry1 = tk.Entry(ventana)
entry1.pack(pady=2)

# Campo 2: Etiqueta y caja de texto para el segundo número
label2 = tk.Label(ventana, text="Segundo número:")
label2.pack(pady=(10, 2))

entry2 = tk.Entry(ventana)
entry2.pack(pady=2)

# Botón de acción: Al hacer clic, invoca la función sumar()
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=12)

# Campo 3: Etiqueta y caja de texto de solo lectura para el resultado
label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.pack(pady=(5, 2))

# state="readonly" permite seleccionar/copiar el resultado pero impide escribir en él
entry_resultado = tk.Entry(ventana, state="readonly")
entry_resultado.pack(pady=2)


# ==========================================
# INICIO DE LA APLICACIÓN
# ==========================================

# Mantiene la ventana abierta a la espera de eventos (clics, teclas, etc.)
ventana.mainloop()