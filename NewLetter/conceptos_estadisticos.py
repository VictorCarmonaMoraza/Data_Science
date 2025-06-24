import statistics

##Forma tradiucional de calcular la media
lista_media=[2,8,9,10,13]

media = sum(lista_media) / len(lista_media)
print("Media(Forma tradicional):", media)

##Forma con la librería statistics
media_statistics = statistics.mean(lista_media)
print("Media con statistics:", media_statistics)

##Forma tradicional de calcular la mediana
lista_mediana = [2, 8, 9, 10, 13,81,69, 45, 23, 12]
##Ordenacion de los datos, es necesario para calcular la mediana
lista_mediana.sort()
if len(lista_mediana) % 2 == 0:
    mediana = (lista_mediana[len(lista_mediana) // 2 - 1] + lista_mediana[len(lista_mediana) // 2]) / 2
print("Mediana(Forma tradicional):", mediana)

##Forma con la librería statistics
mediana_statistics = statistics.median(lista_mediana)
print("Mediana con statistics:", mediana_statistics)
