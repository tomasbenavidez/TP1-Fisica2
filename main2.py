import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('datos2.csv')

#separar los datos
I = 0.28 #Corriente maxima en amperios 

resistencias = df.iloc[:, 0].apply(pd.to_numeric, errors='coerce')
volt_fuente = df.iloc[:, 1].apply(lambda x: str(x).replace(',', '.')).apply(pd.to_numeric, errors='coerce')
volt_multimetro = df.iloc[:, 2].apply(lambda x: str(x).replace(',', '.')).apply(pd.to_numeric, errors='coerce')

# Calcular el valor de la resistencia del multímetro
R_v = volt_multimetro * resistencias / (volt_fuente - volt_multimetro)

# Calcular error de R_v por propagación de incertidumbre
delta_Vf = 0.1   # Error en voltaje de fuente
delta_Vm = 0.01  # Error en voltaje de multímetro

rel_error_Vm = delta_Vm / volt_multimetro
rel_error_Vf = delta_Vf / (volt_fuente - volt_multimetro)
R_v_error = R_v * np.sqrt(rel_error_Vm**2 + rel_error_Vf**2)

# Imprimir resultados
print("\nResistencias:")
print(resistencias)
print("\nVoltaje fuente:")
print(volt_fuente)
print("\nVoltaje multímetro:")
print(volt_multimetro)
print("\nR_v calculado:")
print(R_v)
print("\nError estimado en R_v:")
print(R_v_error)

# Graficar con barras de error
plt.figure(figsize=(10, 6))
plt.errorbar(resistencias, R_v, yerr=R_v_error, fmt='o', capsize=5,
             label='Resistencia del Multímetro con error', color='darkblue')
plt.xlabel('Resistencia Nominal (MΩ)', fontsize=14)
plt.ylabel('Resistencia Interna del Multímetro $R_V$ (MΩ)', fontsize=14)
#plt.title('Estimación de $R_V$ con Barras de Error', fontsize=16, fontweight='bold')
plt.legend(fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlim(2.5, 6.5)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
