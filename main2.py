import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('datos2.csv')

#separar los datos
I = 0.28 #Corriente maxima en amperios 

resitencias = df.iloc[:, 0].apply(pd.to_numeric, errors='coerce')
volt_fuente = df.iloc[:, 1].apply(lambda x: str(x).replace(',', '.')).apply(pd.to_numeric, errors='coerce')
volt_multimetro = df.iloc[:, 2].apply(lambda x: str(x).replace(',', '.')).apply(pd.to_numeric, errors='coerce')

print(resitencias)
print(volt_fuente)
print(volt_multimetro)

#calcular el valor de la resistencia del multimetro
#V_v = V_0 / (R / R_V) + 1))
#                                                                                                                                                                   

R_v = volt_multimetro * resitencias / (volt_fuente - volt_multimetro)
print(R_v)

# Graficar
plt.figure(figsize=(10, 6))
plt.scatter(resitencias, R_v, label='Resistencia del Multímetro', color='darkblue')
#plt.title('Resistencia del Multímetro vs Resistencia Nominal', fontsize=16, fontweight='bold')
plt.xlabel('Resistencia Nominal (Ω)', fontsize=14)
plt.ylabel('Resistencia del Multímetro (Ω)', fontsize=14)
plt.legend(fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlim(2.5, 6.5)
# plt.ylim(0, 10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
