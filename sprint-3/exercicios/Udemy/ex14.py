def imprimir(*args, **kwargs):
    for parametro in args:
        print(parametro)
    
    for nome, valor in kwargs.items():
        print(valor)


imprimir(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)