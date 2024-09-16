def maiores_que_media(conteudo: dict) -> list:
    precos = list(conteudo.values())
    media = sum(precos) / len(precos)
    
    produtos_filtrados = list(filter(lambda x: x[1] > media, conteudo.items()))
    produtos_filtrados.sort(key=lambda x: x[1])

    return produtos_filtrados
