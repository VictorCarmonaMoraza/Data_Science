import pandas as pd


#Creamos un diccionario, donde las claves seran las columnas y los valores seran las filas
info_pais = {
    "pais":["Mexico", "Colombia", "Argentina", "Chile"],
    "capital":["CDMX", "Bogota", "Buenos Aires", "Santiago"],
    "poblacion":[126000000, 50000000, 45000000, 19000000],
    "moneda":["Peso", "Peso", "Peso", "Peso"],
    "idioma":["Español", "Español", "Español", "Español"]
}

df_pais = pd.DataFrame(info_pais)

print(df_pais)