import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a professional style for the plots
sns.set_theme(style="whitegrid")

# Cargar los datos
data = pd.read_csv('datos.csv', header=None)

# Separar las secciones de datos
resistencia_10k = data.iloc[:26, :2]  # Filas correspondientes a la resistencia de 10k ohm
resistencia_10k.columns = ['Voltaje (V)', 'Corriente (A)']

resistencia_96_8 = data.iloc[28:42, :2]  # Filas correspondientes a la resistencia de 96.8 ohm en kohm 
resistencia_96_8.columns = ['Voltaje (V)', 'Corriente (A)']

resistencia_4_62k = data.iloc[43:54, :2]  # Filas correspondientes a la resistencia de 4.62k ohm
resistencia_4_62k.columns = ['Voltaje (V)', 'Corriente (A)']
resistencia_4_62k = resistencia_4_62k.apply(pd.to_numeric, errors='coerce').dropna()

# Convertir a valores numéricos
resistencia_10k = resistencia_10k.apply(pd.to_numeric, errors='coerce').dropna()
resistencia_96_8 = resistencia_96_8.apply(pd.to_numeric, errors='coerce').dropna()

# Recta lineal teórica (usando ley de Ohm)
# I = V / R
resistencia_10k['Corriente Teórica (A)'] = resistencia_10k['Voltaje (V)'] / 9.94
resistencia_96_8['Corriente Teórica (A)'] = resistencia_96_8['Voltaje (V)'] / 0.0968

# Residuos
resistencia_10k['Residuos'] = resistencia_10k['Corriente (A)'] - resistencia_10k['Corriente Teórica (A)']
resistencia_96_8['Residuos'] = resistencia_96_8['Corriente (A)'] - resistencia_96_8['Corriente Teórica (A)']


# Graficar los datos para resistencia de 10kΩ
plt.figure(figsize=(10, 6))
plt.plot(resistencia_10k['Voltaje (V)'], resistencia_10k['Corriente (A)'], label='Experimental', marker='o', color='darkblue')
plt.plot(resistencia_10k['Voltaje (V)'], resistencia_10k['Corriente Teórica (A)'], label='Teórica', color='orange')

# Conectar los puntos experimentales con la recta teórica
for i in range(len(resistencia_10k)):
    plt.plot(
        [resistencia_10k['Voltaje (V)'].iloc[i], resistencia_10k['Voltaje (V)'].iloc[i]],
        [resistencia_10k['Corriente (A)'].iloc[i], resistencia_10k['Corriente Teórica (A)'].iloc[i]],
        color='gray', linestyle=':', linewidth=1
    )

# Configuración del gráfico 1
#plt.title('Voltaje vs Corriente para Resistencia de 10kΩ', fontsize=16, fontweight='bold')
plt.xlabel('Voltaje (V)', fontsize=14)
plt.ylabel('Corriente (A)', fontsize=14)
plt.legend(fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Graficar los datos para resistencia de 96.8Ω
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

# Configuración del gráfico 2
#plt.title('Voltaje vs Corriente para Resistencia de 96.8Ω', fontsize=16, fontweight='bold')
plt.xlabel('Voltaje (V)', fontsize=14)
plt.ylabel('Corriente (A)', fontsize=14)
plt.legend(fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


R_teorico = 4.62  # en kΩ
resistencia_4_62k['Corriente Teórica (A)'] = resistencia_4_62k['Voltaje (V)'] / R_teorico
resistencia_4_62k['Residuos'] = resistencia_4_62k['Corriente (A)'] - resistencia_4_62k['Corriente Teórica (A)']

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(resistencia_4_62k['Voltaje (V)'], resistencia_4_62k['Corriente (A)'],
         label='Experimental', marker='o', color='darkblue')
plt.plot(resistencia_4_62k['Voltaje (V)'], resistencia_4_62k['Corriente Teórica (A)'],
         label='Teórica', color='orange')

# Líneas de residuos (verticales)
for i in range(len(resistencia_4_62k)):
    plt.plot(
        [resistencia_4_62k['Voltaje (V)'].iloc[i]] * 2,
        [resistencia_4_62k['Corriente (A)'].iloc[i], resistencia_4_62k['Corriente Teórica (A)'].iloc[i]],
        color='gray', linestyle=':', linewidth=1
    )
# Configuracion del gráfico 3
#plt.title('Voltaje vs Corriente para Resistencia de 4.62kΩ', fontsize=16, fontweight='bold')
plt.xlabel('Voltaje (V)', fontsize=14)
plt.ylabel('Corriente (A)', fontsize=14)
plt.legend(fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
