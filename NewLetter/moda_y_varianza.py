#Forma tradiucional de calcular la moda
##Moda(Valor que mas se repite)
lista_moda = [2, 8, 9, 10, 13, 8, 9, 10, 13, 8]

# Contar la frecuencia de cada valor
frecuencias = {}
for valor in lista_moda:
    if valor in frecuencias:
        frecuencias[valor] += 1
    else:
        frecuencias[valor] = 1

# Encontrar el valor con mayor frecuencia
moda = max(frecuencias, key=frecuencias.get)
print("Moda(Forma tradicional):", moda)

# Forma con la librería statistics
import statistics
moda_statistics = statistics.mode(lista_moda)
print("Moda con statistics:", moda_statistics)

##Caso mas de una moda
datos = [10, 20, 20, 30, 30, 40]

# Contar frecuencias
frecuencias = {}
for valor in datos:
    frecuencias[valor] = frecuencias.get(valor, 0) + 1

# Obtener la(s) moda(s)
max_frecuencia = max(frecuencias.values())
modas = [k for k, v in frecuencias.items() if v == max_frecuencia]
print("Moda(s):", modas)

#Varianza(Forma tradicional de calcular la varianza)
datos = [10, 20, 30, 40, 50]

# Calcular la media
media = sum(datos) / len(datos)

# Calcular las diferencias al cuadrado
diferencias_cuadrado = [(x - media)**2 for x in datos]

# Calcular varianza muestral
varianza = sum(diferencias_cuadrado) / (len(datos) - 1)

print("Varianza muestral (manual):", varianza)

# Varianza con la librería statistics
import statistics
varianza_statistics = statistics.variance(datos)
print("Varianza muestral con statistics:", varianza_statistics)
