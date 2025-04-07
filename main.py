import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import curve_fit
import numpy as np

# Set a professional style for the plots
sns.set_theme(style="whitegrid")

# Cargar los datos
data = pd.read_csv('datos.csv', header=None)

# Función lineal para el ajuste
def linear_fit(V, R):
    return V / R  # I = V / R

#---------Resistencia 10k----------
resistencia_10k = data.iloc[:26, :2]  # Filas correspondientes a la resistencia de 10k ohm
resistencia_10k.columns = ['Voltaje (V)', 'Corriente (mA)']
resistencia_10k = resistencia_10k.apply(pd.to_numeric, errors='coerce').dropna()

# Convertir corriente a mA
resistencia_10k['Corriente (mA)'] *= 1000

# Ajuste lineal
popt, pcov = curve_fit(linear_fit, resistencia_10k['Voltaje (V)'], resistencia_10k['Corriente (mA)'])
R_ajustada = popt[0]
error_R = np.sqrt(np.diag(pcov))[0]


# Graficar
plt.figure(figsize=(10, 6))
plt.scatter(resistencia_10k['Voltaje (V)'], resistencia_10k['Corriente (mA)'], label='Datos experimentales', color='darkblue')
plt.plot(resistencia_10k['Voltaje (V)'], linear_fit(resistencia_10k['Voltaje (V)'], R_ajustada), label=f'Ajuste lineal\nR = {R_ajustada:.2f} ± {error_R:.2f} kΩ', color='orange')

# Calcular el error de medición
resistencia_10k['Error Corriente (mA)'] = resistencia_10k['Corriente (mA)'] * 0.05  # Ejemplo: 5% de error
resistencia_10k['Error Voltaje (V)'] = resistencia_10k['Voltaje (V)'] * 0.05  # Ejemplo: 5% de error

# Graficar los errores
plt.errorbar(resistencia_10k['Voltaje (V)'], resistencia_10k['Corriente (mA)'],
             xerr=resistencia_10k['Error Voltaje (V)'], yerr=resistencia_10k['Error Corriente (mA)'],
             fmt='o', color='darkblue', label='Datos experimentales con error')

plt.xlabel('Voltaje (V)', fontsize=14)
plt.ylabel('Corriente (mA)', fontsize=14)
plt.legend(fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#---------Resistencia 96.8----------
resistencia_96_8 = data.iloc[28:42, :2]  # Filas correspondientes a la resistencia de 96.8 ohm
resistencia_96_8.columns = ['Voltaje (V)', 'Corriente (mA)']
resistencia_96_8 = resistencia_96_8.apply(pd.to_numeric, errors='coerce').dropna()

# Convertir corriente a mA
resistencia_96_8['Corriente (mA)'] *= 1000

# Ajuste lineal
popt, pcov = curve_fit(linear_fit, resistencia_96_8['Voltaje (V)'], resistencia_96_8['Corriente (mA)'])
R_ajustada = popt[0]
error_R = np.sqrt(np.diag(pcov))[0]

# Graficar
plt.figure(figsize=(10, 6))
plt.scatter(resistencia_96_8['Voltaje (V)'], resistencia_96_8['Corriente (mA)'], label='Datos experimentales', color='darkblue')
plt.plot(resistencia_96_8['Voltaje (V)'], linear_fit(resistencia_96_8['Voltaje (V)'], R_ajustada), label=f'Ajuste lineal\nR = {R_ajustada:.2f} ± {error_R:.2f} Ω', color='orange')

resistencia_96_8['Error Corriente (mA)'] = resistencia_96_8['Corriente (mA)'] * 0.05  # Ejemplo: 5% de error
resistencia_96_8['Error Voltaje (V)'] = resistencia_96_8['Voltaje (V)'] * 0.05  # Ejemplo: 5% de error

# Graficar los errores
plt.errorbar(resistencia_96_8['Voltaje (V)'], resistencia_96_8['Corriente (mA)'],
             xerr=resistencia_96_8['Error Voltaje (V)'], yerr=resistencia_96_8['Error Corriente (mA)'],
             fmt='o', color='darkblue', label='Datos experimentales con error')

plt.xlabel('Voltaje (V)', fontsize=14)
plt.ylabel('Corriente (mA)', fontsize=14)
plt.legend(fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#---------Resistencia 4.62k----------
resistencia_4_62k = data.iloc[43:54, :2]  # Filas correspondientes a la resistencia de 4.62k ohm
resistencia_4_62k.columns = ['Voltaje (V)', 'Corriente (mA)']
resistencia_4_62k = resistencia_4_62k.apply(pd.to_numeric, errors='coerce').dropna()

# Convertir corriente a mA
resistencia_4_62k['Corriente (mA)'] *= 1000

# Ajuste lineal
popt, pcov = curve_fit(linear_fit, resistencia_4_62k['Voltaje (V)'], resistencia_4_62k['Corriente (mA)'])
R_ajustada = popt[0]
error_R = np.sqrt(np.diag(pcov))[0]

# Graficar
plt.figure(figsize=(10, 6))
plt.scatter(resistencia_4_62k['Voltaje (V)'], resistencia_4_62k['Corriente (mA)'], label='Datos experimentales', color='darkblue')
plt.plot(resistencia_4_62k['Voltaje (V)'], linear_fit(resistencia_4_62k['Voltaje (V)'], R_ajustada), label=f'Ajuste lineal\nR = {R_ajustada:.2f} ± {error_R:.2f} kΩ', color='orange')

resistencia_4_62k['Error Corriente (mA)'] = resistencia_4_62k['Corriente (mA)'] * 0.05  # Ejemplo: 5% de error
resistencia_4_62k['Error Voltaje (V)'] = resistencia_4_62k['Voltaje (V)'] * 0.05  # Ejemplo: 5% de error

# Graficar los errores
plt.errorbar(resistencia_4_62k['Voltaje (V)'], resistencia_4_62k['Corriente (mA)'],
                xerr=resistencia_4_62k['Error Voltaje (V)'], yerr=resistencia_4_62k['Error Corriente (mA)'],
                fmt='o', color='darkblue', label='Datos experimentales con error')

plt.xlabel('Voltaje (V)', fontsize=14)
plt.ylabel('Corriente (mA)', fontsize=14)
plt.legend(fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()