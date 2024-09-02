def remove(lista):
    saida = list(set(lista))
    return saida
    
ent = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
saida = remove(ent)
print(saida)