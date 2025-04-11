import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = pd.read_csv('datos.csv', header=None)

# resistencia = data.iloc[:26, :2]  
# resistencia.columns = ['Voltaje (V)', 'Corriente (A)']
# resistencia = resistencia.apply(pd.to_numeric, errors='coerce').dropna()

# # miliamperes
# resistencia['Corriente (mA)'] = resistencia['Corriente (A)'] * 1000

# def modelo_lineal(V, m, b):
#     return m * V + b

# popt, pcov = curve_fit(modelo_lineal, resistencia['Voltaje (V)'], resistencia['Corriente (mA)'])
# pendiente, ordenada = popt
# error_pendiente, error_ordenada = np.sqrt(np.diag(pcov))

# R = 1000 / pendiente  #  ohmios
# error_R = 1000 * error_pendiente / pendiente**2

# # Error del multímetro (según especificaciones)
# error_voltaje_multimetro = 0.01 / 100 * resistencia['Voltaje (V)'] + 0.002  # 0.01% + 2 mV
# error_corriente_multimetro = 0.01 / 100 * resistencia['Corriente (mA)'] + 5  # 0.01% + 5 mA

# # Error total de la resistencia
# error_R_total = np.sqrt(error_R**2 + (error_voltaje_multimetro.mean() / resistencia['Voltaje (V)'].mean())**2)

# # Imprimir resultados con el error total
# print(f"Resistencia ajustada: R = {R:.2f} Ω ± {error_R_total:.2f} Ω")
# print(f"Ordenada al origen: b = {ordenada:.2f} mA ± {error_ordenada:.2f} mA")

# # Graficar con barras de error
# plt.figure(figsize=(10, 6))
# plt.errorbar(
#     resistencia['Voltaje (V)'], resistencia['Corriente (mA)'],
#     xerr=error_voltaje_multimetro, yerr=error_corriente_multimetro,
#     fmt='o', label='Datos experimentales (con error)', color='navy', ecolor='blue', capsize=7, elinewidth=1.5
# )
# plt.plot(
#     resistencia['Voltaje (V)'], modelo_lineal(resistencia['Voltaje (V)'], *popt),
#     color='orange', label='Ajuste lineal'
# )

# # Etiquetas y leyenda
# plt.xlabel('Voltaje (V)', fontsize=14)
# plt.ylabel('Corriente (mA)', fontsize=14)
# plt.legend(fontsize=12)
# plt.grid(True)

# # Texto con resultados
# texto = f"R = {R:.2f} Ω ± {error_R_total:.2f} Ω"
# plt.text(resistencia['Voltaje (V)'].min() * 1.1, resistencia['Corriente (mA)'].max() * 0.9, texto, fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

# plt.tight_layout()
# plt.show()

def graficos1(data, filas, nombre_resistencia):
    """
    Genera un gráfico con ajuste lineal y barras de error para una resistencia específica.

    Parámetros:
    - data: DataFrame con los datos experimentales.
    - filas: Tupla con el rango de filas correspondientes a la resistencia (inicio, fin).
    - nombre_resistencia: Nombre de la resistencia para el título del gráfico.
    """
    # Filtrar los datos para la resistencia específica
    resistencia = data.iloc[filas[0]:filas[1], :2]
    resistencia.columns = ['Voltaje (V)', 'Corriente (A)']
    resistencia = resistencia.apply(pd.to_numeric, errors='coerce').dropna()

    # Convertir corriente a miliamperes
    resistencia['Corriente (mA)'] = resistencia['Corriente (A)'] * 1000

    # Definir el modelo lineal
    def modelo_lineal(V, m, b):
        return m * V + b

    # Ajuste lineal
    popt, pcov = curve_fit(modelo_lineal, resistencia['Voltaje (V)'], resistencia['Corriente (mA)'])
    pendiente, ordenada = popt
    error_pendiente, error_ordenada = np.sqrt(np.diag(pcov))

    # Calcular la resistencia y su error
    R = 1000 / pendiente  # ohmios
    error_R = 1000 * error_pendiente / pendiente**2

    # Error del multímetro (según especificaciones)
    error_voltaje_multimetro = 0.01 / 100 * resistencia['Voltaje (V)'] + 0.002  # 0.01% + 2 mV
    error_corriente_multimetro = 0.01 / 100 * resistencia['Corriente (mA)'] + 5  # 0.01% + 5 mA

    # Error total de la resistencia
    error_R_total = np.sqrt(error_R**2 + (error_voltaje_multimetro.mean() / resistencia['Voltaje (V)'].mean())**2)

    # Graficar con barras de error
    plt.figure(figsize=(10, 6))
    plt.errorbar(
        resistencia['Voltaje (V)'], resistencia['Corriente (mA)'],
        xerr=error_voltaje_multimetro, yerr=error_corriente_multimetro,
        fmt='o', label='Datos experimentales (con error)', color='navy', ecolor='darkblue', capsize=7, elinewidth=1.5
    )
    plt.plot(
         modelo_lineal(resistencia['Voltaje (V)'], *popt), resistencia['Voltaje (V)'],
        color='orange', label='Ajuste lineal'
    )

    # Etiquetas y leyenda
    plt.xlabel('Voltaje (V)', fontsize=14)
    plt.ylabel('Corriente (mA)', fontsize=14)
    plt.title(f'Ajuste lineal - {nombre_resistencia}', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True)

    # Texto con resultados
    texto = f"R = {R:.2f} Ω ± {error_R_total:.2f} Ω\nb = {ordenada:.2f} mA ± {error_ordenada:.2f} mA"
    plt.text(resistencia['Voltaje (V)'].min() * 1.1, resistencia['Corriente (mA)'].max() * 0.9, texto, fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

    plt.tight_layout()
    plt.show()

# Graficar para diferentes resistencias
graficos1(data, (0, 26), "Resistencia 1 (10 kΩ)")
graficos1(data, (28, 42), "Resistencia 2 (96.8 Ω)")
graficos1(data, (43, 54), "Resistencia 3 (4.62 kΩ)")