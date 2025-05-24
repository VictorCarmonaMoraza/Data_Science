'''
A partir del dataframe con la ifnormacion de trafico peatonal(PEATONES_2020_mod.csv),
verificar el numero de registros y a continuacion eliminar duplicados como aquellos 
registros que tienen los valores de todas las columnas iguales:

¿Cuanto valores duplicaod existian? 

Elimina todas los valores erroneos(NaN) del dataframe.
   - ¿Cuantos valores NaN existian?
   - ¿Que porcentaje de los datos originales eran erroneos?
'''

import pandas as pd

#Cargamos el DataFrame
df  = pd.read_csv(r'PEATONES_2020_mod.csv',
                  delimiter=';',encoding='ISO-8859-1')

#Obtener el numero de registros(filas,columnas)
print(df.shape)

#Obtener valores duplicados
valores_duplicados = df.duplicated().sum()
print(f'El numero de valores duplicados es: {valores_duplicados}')

#Eliminar duplicaods(eliminaremos aquellos que tiene todos su valores 
# iguales en todas las columnas)
# implcae = true --> se eliminan los duplicados en el mismo dataframe
df.drop_duplicates(inplace=True)

#Si imprimos ahora los registros encontraremos una difernecia de 6 registros menos
print(df.shape)

#verficar los valores erroneos
df.dropna(inplace=True)


print(df.shape)
valores_erroneos = 288749 - 284863
print(f'El numero de valores erroneos es: {valores_erroneos}')

#Porcentaje valores eroneos
porcentaje_erroneos = (valores_erroneos/288755 * 100)
print(f'El porcentaje de valores erroneos es: {porcentaje_erroneos:.2f}%')

