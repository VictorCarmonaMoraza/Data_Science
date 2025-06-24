import matplotlib.pyplot as plt

año = [1970,1975,1980,1985,1990,1995,2000,2005,2010,2015,2020]
poblacion = [5.5,6,7,8,9,10,5,7,3,4,1]
plt.title("Población mundial")

plt.xlabel("Año")
plt.ylabel("Población (miles de millones)")
plt.xticks(año, rotation=45)
plt.scatter(año,poblacion)
plt.scatter(año, poblacion, c='red')
plt.tight_layout()
plt.show()