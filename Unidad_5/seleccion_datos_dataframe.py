import pandas as pd


df  = pd.read_csv(r'annual-enterprise-survey-2023-financial-year-provisional.csv',
                  delimiter=',',encoding='ISO-8859-1')

filtro_level1_valor = 'Level 1'

# 2. Crear una Serie booleana para las filas que cumplen la condición
condicion_filas_level1 = df['Industry_aggregation_NZSIOC'] == filtro_level1_valor

# 3. Seleccionar las filas que cumplen la condición y solo la columna 'Year'
# Aquí es donde combinas el filtro booleano con la selección de la columna.
# No necesitas .loc para el filtro de filas si usas una Serie booleana,
# pero sí para especificar la columna con su etiqueta.
# Esto es lo que quieres hacer:
df_level1_year = df.loc[condicion_filas_level1, ['Year','Industry_name_NZSIOC']]

print(df_level1_year)
print(len(df_level1_year))