precio_base = float(input("Introduce el precio del producto (€): "))

con_descuento = precio_base * 0.85
precio_final = con_descuento * 1.21

print(f"Precio con descuento: {con_descuento:.2f} €")
print(f"Precio final con IVA (21%): {precio_final:.2f} €")