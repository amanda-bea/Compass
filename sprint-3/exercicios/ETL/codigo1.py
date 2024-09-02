contador = {}
#inicialização de um dicionário para receber o número de aparições

with open('actors.csv', 'r') as arquivo:
#abertura do arquivo usando comnados padrões do python
    first_line = True
    #variável booleana para pular a primeira linha do arquivo com os rótulos
    cont = 0
    #contador de linhas para pular a sexta linha que causa erro no programa
    
    for linha in arquivo:
        linha = linha.strip()
        partes = linha.split(',') #recepção de cada linha separada em colunas
        cont += 1

        if first_line or cont == 6: #se for a primeira ou sexta linha
            first_line = False
            continue #elas são puladas

        #recepção dos dados no dicionário
        number = partes[2]
        ator = partes[0]
        contador[ator] = number


#variáveis que irão receber o ator com mais aparições e seu número de filmes
maior = 0
actor = None

#laço que encontra o maior número de aparições em filmes e o respectivo ator
for ator, number in contador.items():
    if int(number) > maior:
        actor = ator
        maior = int(number)

resultado = 'parte-1.txt'

#comando padrão do python para printar o resultado no arquivo de saída
with open(resultado, 'w') as saida:
    print("Ator/atriz, Number of movies", file=saida)
    print(actor, maior, sep=",", file=saida)
