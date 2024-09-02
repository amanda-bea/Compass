lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] 
cont = 0
for i in lista:
    if lista[cont] == i[::-1]:
        print("A palavra:", i, "é um palíndromo")
    else:
        print("A palavra:", i, "não é um palíndromo")
    cont += 1
