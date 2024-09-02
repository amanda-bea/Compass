import random

random_list = random.sample(range(500), 50)

lista = sorted(random_list)

med = (lista[24] + lista[25]) / 2


mediana = med
media = sum(lista) / 50
valor_minimo = min(lista)
valor_maximo = max(lista)

print("Media: ", media,",", " Mediana: ", mediana,",", " Mínimo: ", valor_minimo, ",", " Máximo: ", valor_maximo, sep="")