lista = {}
#inicializa um dicionário para contar as aparições dos filmes


with open('actors.csv', 'r', encoding='utf-8') as file:
#abertura do arquivo usando comnados padrões do python
    first_line = True
    #variável booleana para pular a primeira linha do arquivo com os rótulos
    cont = 0
    #contador de linhas para pular a sexta linha que causa erro no programa

    for linha in file:
        linha = linha.strip()
        cont += 1
        if first_line or cont == 6: #se for a primeira ou sexta linha
            first_line = False
            continue #elas são puladas
        
        colunas = linha.split(',') #recepção das linhas separadas por colunas

        #entrada do total gross e o respectivo ator no dicionário
        ator = colunas[0]
        gross = float(colunas[1])
        lista[ator] = gross

#ordena o dicionário pelo número de aparições (em ordem decrescente)
lista_ordenada = sorted(lista.items(), key=lambda x: x[1], reverse=True)

resultado = 'parte-5.txt'

#comando padrão do python para printar o resultado no arquivo de saída
with open(resultado, 'w') as saida:

    #laço para printar todo o dicionário
    for actor, total in lista_ordenada:
        print(f"{actor} - {total}", file=saida)