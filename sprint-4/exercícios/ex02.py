def conta_vogais(texto: str) -> int:

    vogais = 'aeiou'
    
    vogais_filtradas = filter(lambda x: x in vogais, texto.lower())
    
    numero = len(list(vogais_filtradas))
    
    return numero
