import matplotlib.pyplot as plt
import pandas as pd

# 1. Configuración de datos de matrícula universitaria histórica
matricula_data = {
    "Año": [1945, 1950, 1955, 1960, 1965, 1970, 1975, 1980, 2012, 2021],
    "Estudiantes": [47400, 80445, 138317, 160047, 222903, 261342, 487389, 386743, 1824904, 2549789]
}
df_matricula = pd.DataFrame(matricula_data)

# 2. Configuración de datos de estudiantes extranjeros
extranjeros_data = {
    "Año": [2005, 2015, 2019, 2021, 2022],
    "Estudiantes Extranjeros": [26354, 57953, 100382, 117820, 122769],
    "% del total": [1.12, 3.05, 4.0, 3.9, 4.5]
}
df_extranjeros = pd.DataFrame(extranjeros_data)

# 3. Configuración de datos por tipo de gestión (2021 y 2022)
gestion_data = {
    "Año": ["2021", "2021", "2022", "2022"],
    "Gestión": ["Estatal", "Privada", "Estatal", "Privada"],
    "% Extranjeros": [4.1, 5.5, 4.25, 5.58]
}
df_gestion = pd.DataFrame(gestion_data)

# =====================================================================
# DISEÑO Y CONFIGURACIÓN DE LOS GRÁFICOS (Estilo Corporativo / Crítico)
# =====================================================================
# Cambiamos el estilo visual a uno más sobrio y limpio
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

fig, axs = plt.subplots(3, 1, figsize=(10, 16))

# Gráfico 1: Evolución histórica (Muestra la presión presupuestaria)
axs[0].plot(df_matricula["Año"], df_matricula["Estudiantes"], marker='o', color='#1e3a8a', linewidth=2.5, markersize=6)
axs[0].set_title("Crecimiento de la Matrícula Universitaria Argentina (1945–2021)", fontsize=13, fontweight='bold', color='#1e293b')
axs[0].set_xlabel("Año", fontsize=11)
axs[0].set_ylabel("Cantidad de Estudiantes (en millones)", fontsize=11)
axs[0].ticklabel_format(style='plain', axis='y') # Evita la notación científica molesta

# Gráfico 2: Estudiantes Extranjeros (El eje del debate)
axs[1].bar(df_extranjeros["Año"], df_extranjeros["Estudiantes Extranjeros"], color='#ef4444', width=3)
axs[1].set_title("Evolución del Ingreso de Estudiantes Extranjeros", fontsize=13, fontweight='bold', color='#1e293b')
axs[1].set_xlabel("Año", fontsize=11)
axs[1].set_ylabel("Cantidad de Extranjeros", fontsize=11)

# Gráfico 3: Comparación por tipo de gestión (Pública vs Privada arancelada)
colores_gestion = {"2021": "#94a3b8", "2022": "#3b82f6"} # Gris para 2021, Azul para 2022
for year in ["2021", "2022"]:
    subset = df_gestion[df_gestion["Año"] == year]
    axs[2].bar(subset["Gestión"] + " " + year, subset["% Extranjeros"], color=colores_gestion[year], width=0.5)

axs[2].set_title("Proporción de Alumnos Extranjeros por Tipo de Gestión (%)", fontsize=13, fontweight='bold', color='#1e293b')
axs[2].set_ylabel("% del Total de Alumnos", fontsize=11)
axs[2].set_ylim(0, 7) # Le damos aire arriba para que se vean bien las barras

# Ajustes generales de la imagen
plt.tight_layout()

# Guardar el gráfico automáticamente para poder subirlo a GitHub
plt.savefig('analisis_matricula_universitaria.png', dpi=300, bbox_inches='tight')
print("¡Gráfico generado y guardado como 'analisis_matricula_universitaria.png'!")

plt.show()
