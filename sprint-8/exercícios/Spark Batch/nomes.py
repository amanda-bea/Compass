import names
import random
import time

random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = []
for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))

dados = [] 

for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

with open('nomes_aleatorios.txt', 'w') as arquivo:
    for nome in dados:
        arquivo.write(f"{nome} \n")
