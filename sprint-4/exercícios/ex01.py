with open("number.txt", 'r') as file:
    numeros = list(map(int, file.readlines()))

pares = filter(lambda x: x % 2 == 0, numeros)

sortedPares = sorted(pares, reverse = True)

topCinco = sortedPares[:5]

print(topCinco)
print(sum(topCinco))