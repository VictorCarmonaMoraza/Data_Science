import pandas as pd


df  = pd.read_csv(r'annual-enterprise-survey-2023-financial-year-provisional.csv',
                  delimiter=',',encoding='ISO-8859-1')

print(df.head(10))
print(f'El numero de registros del csv es: {len(df)}')
print(f'Los daotos estadisticos de dataframe son : {df.describe()}')