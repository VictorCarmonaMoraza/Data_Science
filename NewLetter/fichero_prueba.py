import pandas as pd

df = pd.read_csv(r'C:\Users\Victo\Desktop\CursoDataScience\Unidad 1\1.3\info_pais.csv'
                 ,delimiter=';', encoding='ISO-8859-1')

df.columns = df.columns.str.strip()
print(df.columns.tolist())


df_ordenado = df.sort_values(by='Esperanza de vida', ascending=False)

print(df_ordenado)


                 