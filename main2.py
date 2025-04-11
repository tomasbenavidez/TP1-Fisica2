import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Cargar los datos
df = pd.read_csv('datos2.csv')  # Cambiá a la ruta correcta si lo corrés localmente

# Convertir texto a números (por si vienen con comas decimales)
df["resistencia (Mohm)"] = df["resistencia (Mohm)"].astype(str).str.replace(",", ".").astype(float)
df["Volt Fuente"] = df["Volt Fuente"].astype(str).str.replace(",", ".").astype(float)
df["Volt Multimetro"] = df["Volt Multimetro"].astype(str).str.replace(",", ".").astype(float)

# Extraer columnas
R = df["resistencia (Mohm)"]
V_fuente = df["Volt Fuente"]
V_mult = df["Volt Multimetro"]

# Cálculo de Rv (resistencia interna del voltímetro)
Rv = R * V_mult / (V_fuente - V_mult)

# Estimación del error:
# - 5% de tolerancia en la resistencia (horizontal)
# - 10% de incertidumbre relativa en Rv como estimación (vertical)
err_R = R * 0.05
err_Rv = Rv * 0.10

# Calcular promedio de Rv
Rv_prom = Rv.mean()

# Graficar con barras de error
plt.figure(figsize=(8, 5))
plt.errorbar(R, Rv, xerr=err_R, yerr=err_Rv,color='blue', fmt='o', label="Mediciones", capsize=5)

# Línea horizontal con el promedio
plt.axhline(Rv_prom, color='red', linestyle='--', label=f"Promedio $R_V$ ≈ {Rv_prom:.2f} MΩ")

# Estética
plt.xlabel("Resistencia conectada (MΩ)")
plt.ylabel("Resistencia interna estimada del voltímetro $R_V$ (MΩ)")
plt.title("Estimación de $R_V$ con barras de error")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
