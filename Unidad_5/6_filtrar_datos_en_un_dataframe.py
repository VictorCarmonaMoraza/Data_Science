# Filtrar datos en un dataframe
# Ejercicio: Crear el dataframe (df) a partir del fichero con la informacion de trafico peatonal
# (PEATONES_2020_mod.csv):

# - Cree un dataframe (df2) con el filtrado de datos necesarios si queremos enfocar nuestros analisis
# en que ocurrio los dias comprendidos en el rango [01/01/2020 - 01/05/2020]. (mm/dd/aaaa)

# Sobre el mismo dataframe (df2) realice el filtrado para distrito "Centro". Utilice str.contains

# Verifique si hay valores erroneos en la columna "PEATONES" en estas condiciones, en caso afirmati-
# vo cree el dataframe df_interp con la interpolacion lineal de df2

import pandas as pd

#Cargamos el DataFrame
df  = pd.read_csv(r'PEATONES_2020_mod.csv',
                  delimiter=';',encoding='ISO-8859-1')

#Imprimir los 10 primeros registros
print(df.head(10))

#Obtener el numero de registros(filas,columnas)
print(df.shape)

#Crear un dataframe con el rango de dos fechas
df2 = df[(df['FECHA'] >= '01/01/2020') & (df['FECHA'] <= '01/05/2020') & (df['DISTRITO'] == 'Centro')]
print(f'El dataframe (df2) filtrado por fechas tiene una cantidad de: {df2.shape}')

#Obtener la fecha maxima y minima del dataframe df2
print(f'Fecha minima: {df2["FECHA"].min()}') 
print(f'Fecha maxima: {df2["FECHA"].max()}')

#Comporbar is tenemos valores erroneos en la columna PEATONES
print(df2.count())

#Obtener los ficheros erroneos en la columna PEATONES
valores_erroneos = df2['PEATONES'].isnull().sum()
print(f'El numero de valores erroneos en la columna PEATONES es: {valores_erroneos}')

#epresntar esos dos registros erroneos
print(df2[df2['PEATONES'].isnull()])

#Interpolamos nuestros dataframe df2 para solucionar esos dos registros nulos
df_interp = df2.interpolate(method='linear', limit_direction='forward')
print(df_interp.count())
