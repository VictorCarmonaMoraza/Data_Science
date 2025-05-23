import pandas as pd 

df  = pd.read_csv(r'PEATONES_2020.csv',
                  delimiter=';',encoding='ISO-8859-1')

#Ver el numero de registros y de columnas -->SALIDA: (filas,columnas)
print(df.shape)

#Obtener los primeros 5 registros
print(df.head())

#Establecer que nos muestre 10 registros
print(df.head(10))

#Obtener informacion de nuestro dataframe
print(df.info())

#Total de registros
print(df.count())

#Obtener la mediana de la columna PEATONES
print(f'La mediana de la columna peatones es: {df['PEATONES'].median()}')

#Obtener el promedio de la columna PEATONES(MEDIA)
print(f'El promedio de la columna peatones es: {df['PEATONES'].mean()}')

# Obtenr el perncentil de la columna PEATONES
# Con esto nos esta dciendo que el 90% de los datos estan por debajo de este valor en
# las calles
print(f'El percentil 90 de la columna peatones es: {df['PEATONES'].quantile(0.9)}')

#Obtener la primera fecha de la columna FECHA
print(f'La primera fecha de la columna FECHA es: {df['FECHA'].min()}')

#Obtener la ultima fecha de la columna FECHA
print(f'La ultima fecha de la columna FECHA es: {df['FECHA'].max()}')

#Obtener sobre nuestras columnas de valores numericos todas sus estadisticas
print(df.describe())

#Creamos un nueva columna acumulativa(sumara todos los valores que tenga la columna PEATONES)
df['ACUMULADO'] = df['PEATONES'].cumsum()
print(df.head(10))

