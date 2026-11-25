def calcular_velocidad(distancia_km, tiempo_horas):
    if tiempo_horas <= 0:
        raise ValueError("El tiempo debe ser mayor que cero para calcular la velocidad.")
    return distancia_km / tiempo_horas


# Ejemplo de uso
try:
    print(f"Velocidad: {calcular_velocidad(120, 2)} km/h")
    print(f"Velocidad: {calcular_velocidad(120, 0)} km/h")
except ValueError as e:
    print(f"Excepción capturada: {e}")