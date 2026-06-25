import matplotlib.pyplot as plt
import pandas as pd

# Datos de matrícula universitaria histórica (pregrado y grado)
matricula_data = {
    "Año": [1945, 1950, 1955, 1960, 1965, 1970, 1975, 1980, 2012, 2021],
    "Estudiantes": [47400, 80445, 138317, 160047, 222903, 261342, 487389, 386743, 1824904, 2549789]
}
df_matricula = pd.DataFrame(matricula_data)

# Datos de estudiantes extranjeros
extranjeros_data = {
    "Año": [2005, 2015, 2019, 2021, 2022],
    "Estudiantes Extranjeros": [26354, 57953, 100382, 117820, 122769],
    "% del total": [1.12, 3.05, 4.0, 3.9, 4.5]
}
df_extranjeros = pd.DataFrame(extranjeros_data)

# Datos por tipo de gestión (2021 y 2022)
gestion_data = {
    "Año": ["2021", "2021", "2022", "2022"],
    "Gestión": ["Estatal", "Privada", "Estatal", "Privada"],
    "% Extranjeros": [4.1, 5.5, 4.25, 5.58]
}
df_gestion = pd.DataFrame(gestion_data)

# Crear los gráficos
fig, axs = plt.subplots(3, 1, figsize=(10, 18))

# Gráfico 1: Evolución histórica de matrícula total
axs[0].plot(df_matricula["Año"], df_matricula["Estudiantes"], marker='o', color='navy')
axs[0].set_title("Evolución de la Matrícula Universitaria Argentina (1945–2021)", fontsize=14)
axs[0].set_xlabel("Año")
axs[0].set_ylabel("Cantidad de estudiantes")
axs[0].grid(True)

# Gráfico 2: Estudiantes Extranjeros vs. Año
axs[1].bar(df_extranjeros["Año"], df_extranjeros["Estudiantes Extranjeros"], color='darkgreen')
axs[1].set_title("Cantidad de Estudiantes Extranjeros en Universidades Argentinas", fontsize=14)
axs[1].set_xlabel("Año")
axs[1].set_ylabel("Cantidad de extranjeros")
axs[1].grid(True)

# Gráfico 3: Comparación por tipo de gestión
for year in ["2021", "2022"]:
    subset = df_gestion[df_gestion["Año"] == year]
    axs[2].bar(subset["Gestión"] + " " + year, subset["% Extranjeros"], label=year)
axs[2].set_title("Porcentaje de Estudiantes Extranjeros por Tipo de Gestión", fontsize=14)
axs[2].set_ylabel("% del total de estudiantes")
axs[2].legend(title="Año")
axs[2].grid(True)

plt.tight_layout()
plt.show()
