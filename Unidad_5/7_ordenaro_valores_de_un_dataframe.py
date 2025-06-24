import pandas as pd

df  = pd.read_csv(r'PEATONES_2020_mod.csv',
                  delimiter=';',encoding='ISO-8859-1')

print(df.shape)

print(df.head(10))

#Ordenar dataframe por la columna 'PEATONES'
df_sorted_by_PEATONES = df.sort_values(by='PEATONES', ascending=True)
df_sorted_by_PEATONES = df_sorted_by_PEATONES[df_sorted_by_PEATONES['PEATONES'] >= 10]
print(df_sorted_by_PEATONES.head())