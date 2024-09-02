def soma(lista):
    soma = 0
    for num in lista:
        soma += int(num)
    
    return soma
        

string = "1,3,4,6,10,76"
nova = list(string.split(","))
saida = soma(nova)
print(saida)