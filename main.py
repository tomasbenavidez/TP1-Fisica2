import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = pd.read_csv('datos.csv', header=None)

# === CAMBIrrr ESTAS LÍNEAS PARA CADA RESISTENCIA ===
resistencia = data.iloc[:26, :2]  
resistencia.columns = ['Voltaje (V)', 'Corriente (A)']
resistencia = resistencia.apply(pd.to_numeric, errors='coerce').dropna()

# miliamperes
resistencia['Corriente (mA)'] = resistencia['Corriente (A)'] * 1000

def modelo_lineal(V, m, b):
    return m * V + b

popt, pcov = curve_fit(modelo_lineal, resistencia['Voltaje (V)'], resistencia['Corriente (mA)'])
pendiente, ordenada = popt
error_pendiente, error_ordenada = np.sqrt(np.diag(pcov))

R = 1000 / pendiente  #  ohmios
error_R = 1000 * error_pendiente / pendiente**2

print(f"Resistencia ajustada: R = {R:.2f} Ω ± {error_R:.2f} Ω")
print(f"Ordenada al origen: b = {ordenada:.2f} mA ± {error_ordenada:.2f} mA")

plt.figure(figsize=(10, 6))
plt.scatter(resistencia['Voltaje (V)'], resistencia['Corriente (mA)'], label='Datos experimentales', color='navy')
plt.plot(resistencia['Voltaje (V)'], modelo_lineal(resistencia['Voltaje (V)'], *popt), color='orange', label='Ajuste lineal')
plt.xlabel('Voltaje (V)', fontsize=14)
plt.ylabel('Corriente (mA)', fontsize=14)
plt.title('Ajuste lineal - Resistencia desconocida')
plt.legend()
plt.grid(True)

texto = f"R = {R:.2f} Ω ± {error_R:.2f} Ω\nb = {ordenada:.2f} mA ± {error_ordenada:.2f} mA"
plt.text(0.08, resistencia['Corriente (mA)'].max() * 0.9, texto, fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

plt.tight_layout()
plt.show()
print(resistencia['Voltaje (V)'].min())



#---------Resistencia 96.0----------


resistencia_96_8 = data.iloc[28:42, :2]  # Filas correspondientes a la resistencia de 96.8 ohm en kohm 
resistencia_96_8.columns = ['Voltaje (V)', 'Corriente (A)']
resistencia_96_8 = resistencia_96_8.apply(pd.to_numeric, errors='coerce').dropna()
resistencia_96_8['Corriente Teórica (A)'] = resistencia_96_8['Voltaje (V)'] / 0.0968
resistencia_96_8['Residuos'] = resistencia_96_8['Corriente (A)'] - resistencia_96_8['Corriente Teórica (A)']
resistencia_96_8['Error abs'] = resistencia_96_8['Residuos'].abs()


plt.figure(figsize=(10, 6))
plt.plot(resistencia_96_8['Voltaje (V)'], resistencia_96_8['Corriente (A)'], label='Experimental', marker='o', color='darkblue')
plt.plot(resistencia_96_8['Voltaje (V)'], resistencia_96_8['Corriente Teórica (A)'], label='Teórica', color='orange')
# Conectar los puntos experimentales con la recta teórica
for i in range(len(resistencia_96_8)):
    plt.plot(
        [resistencia_96_8['Voltaje (V)'].iloc[i], resistencia_96_8['Voltaje (V)'].iloc[i]],
        [resistencia_96_8['Corriente (A)'].iloc[i], resistencia_96_8['Corriente Teórica (A)'].iloc[i]],
        color='gray', linestyle=':', linewidth=1
    )

#gráfico 2
#plt.title('Voltaje vs Corriente para Resistencia de 96.8Ω', fontsize=16, fontweight='bold')
plt.errorbar(
    resistencia_96_8['Voltaje (V)'],
    resistencia_96_8['Corriente (A)'],
    yerr=resistencia_96_8['Error abs'],
    fmt='o',
    label='Error abs',
    color='darkblue',
    ecolor='gray',
    capsize=4
)
plt.xlabel('Voltaje (V)', fontsize=14)
plt.ylabel('Corriente (A)', fontsize=14)
plt.legend(fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()



# ---------Resistencia 4.62k----------

resistencia_4_62k = data.iloc[43:54, :2]  # Filas correspondientes a la resistencia de 4.62k ohm
resistencia_4_62k.columns = ['Voltaje (V)', 'Corriente (A)']
resistencia_4_62k = resistencia_4_62k.apply(pd.to_numeric, errors='coerce').dropna()

R_teorico = 4.62  # en kΩ
resistencia_4_62k['Corriente Teórica (A)'] = resistencia_4_62k['Voltaje (V)'] / R_teorico
resistencia_4_62k['Residuos'] = resistencia_4_62k['Corriente (A)'] - resistencia_4_62k['Corriente Teórica (A)']
resistencia_4_62k['Error abs'] = resistencia_4_62k['Residuos'].abs()


# Graficar
plt.figure(figsize=(10, 6))
plt.plot(resistencia_4_62k['Voltaje (V)'], resistencia_4_62k['Corriente (A)'],
         label='Experimental', marker='o', color='darkblue')
plt.plot(resistencia_4_62k['Voltaje (V)'].to_list(), resistencia_4_62k['Corriente Teórica (A)'].to_list(),
         label='Teórica', color='orange')

# Líneas de residuos (verticales)
for i in range(len(resistencia_4_62k)):
    plt.plot(
        [resistencia_4_62k['Voltaje (V)'].iloc[i]] * 2,
        [resistencia_4_62k['Corriente (A)'].iloc[i], resistencia_4_62k['Corriente Teórica (A)'].iloc[i]],
        color='gray', linestyle=':', linewidth=1
    )
# gráfico 3
#plt.title('Voltaje vs Corriente para Resistencia de 4.62kΩ', fontsize=16, fontweight='bold')
plt.errorbar(
    resistencia_4_62k['Voltaje (V)'],
    resistencia_4_62k['Corriente (A)'],
    yerr=resistencia_4_62k['Error abs'],
    fmt='o',
    label='Error abs',
    color='darkblue',
    ecolor='grey',
    capsize=4
)
plt.xlabel('Voltaje (V)', fontsize=14)
plt.ylabel('Corriente (A)', fontsize=14)
plt.legend(fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
