from functools import reduce

def calcula_saldo(lancamentos):
    val = map(lambda x: x[0] * 1 if x[1] == 'C' else x[0] * -1, lancamentos)
    
    saldo = reduce(lambda acumula, valor: acumula + valor, val)
    
    return saldo