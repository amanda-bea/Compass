def my_map(lista, f):
    return [f(x) for x in lista]
    

def pot(numero):
    return numero ** 2
    
    
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
saida = my_map(num, pot)
print(saida)
