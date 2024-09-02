contador = {}
#inicializa um dicionário para contar as aparições dos filmes

with open('actors.csv', 'r', encoding='utf-8') as file:
#abertura do arquivo usando comnados padrões do python
    first_line = True
    #variável booleana para pular a primeira linha do arquivo com os rótulos

    for linha in file:
        linha = linha.strip()
        if first_line:  #se for a primeira
            first_line = False
            continue #ela é pulada
        
        colunas = linha.split(',') #recepção de cada linha separada em colunas
        filme = colunas[4]  #seleciona a quinta coluna
            
        #incrementa o contador para o filme
        if filme in contador:
            contador[filme] += 1
        else:
            contador[filme] = 1

#ordena o dicionário pelo número de aparições (em ordem decrescente)
contador_ordenado = sorted(contador.items(), key=lambda x: x[1], reverse=True)

resultado = 'parte-4.txt'

#comando padrão do python para printar o resultado no arquivo de saída
with open(resultado, 'w') as saida:
    seq = 1

    #laço para printar todo o dicionário
    for filme, contagem in contador_ordenado:
        print(f"{seq} - O filme {filme} aparece {contagem} vez(es) no dataset", file=saida)
        seq += 1
