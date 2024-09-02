def divide(lista):
    n = len(lista)
    parte1 = lista[:n//3]
    parte2 = lista[n//3:2*n//3]
    parte3 = lista[2*n//3:]
    
    return (parte1, parte2, parte3)
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lista1, lista2, lista3 = divide(lista)
print(lista1, lista2, lista3)