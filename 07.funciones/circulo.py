
def temperaturasMaxMinAvg(temperaturas):
    # Validamos que la lista no esté vacía para evitar errores
    if not temperaturas:
        return None, None, None

    temp_maxima = max(temperaturas)
    temp_minima = min(temperaturas)
    temp_media = sum(temperaturas) / len(temperaturas)

    return temp_maxima, temp_minima, temp_media


# --- Ejemplo de uso ---
registro_temperaturas = [18.5, 22.0, 25.3, 16.8, 19.2, 24.1, 21.0]

maxima, minima, media = temperaturasMaxMinAvg(registro_temperaturas)

if maxima is not None:
    print(f"Temperatura máxima: {maxima} °C")
    print(f"Temperatura mínima: {minima} °C")
    print(f"Temperatura media:  {media:.2f} °C")
else:
    print("La lista de temperaturas está vacía.")