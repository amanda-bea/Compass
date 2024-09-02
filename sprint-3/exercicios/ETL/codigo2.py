soma = 623.40
#inicilação da variável soma com o valor da sexta linha que causa erro no programa

with open('actors.csv', 'r') as arquivo:
#abertura do arquivo usando comnados padrões do python
    first_line = True
    #variável booleana para pular a primeira linha do arquivo com os rótulos
    contador = 0
    #contador de linhas para pular a sexta linha que causa erro no programa

    for linha in arquivo:
        linha = linha.strip()
        partes = linha.split(',') #recepção de cada linha separada em colunas
        contador += 1

        if first_line or contador == 6: #se for a primeira ou sexta linha
            first_line = False
            continue #elas são puladas
        
        #recepção das linhas da sexta coluna e soma do valor
        gross = partes[5]
        soma += float(gross)

#cálculo da média   
media = soma / contador

resultado = 'parte-2.txt'

#comando padrão do python para printar o resultado no arquivo de saída
with open(resultado, 'w') as saida:
    print("Média de bilheteria =", media, file=saida)