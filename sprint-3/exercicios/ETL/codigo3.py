lista = {}
#inicialização de um dicionário para receber o número de aparições

with open('actors.csv', 'r') as arquivo:
#abertura do arquivo usando comnados padrões do python

    for linha in arquivo:
        linha = linha.strip()
        partes = linha.split(',') #recepção de cada linha separada em colunas

        #recepção dos dados no dicionário
        media = partes[3]
        ator = partes[0]
        lista[ator] = media

#variáveis que irão receber o ator com maior média de receita bruta
maior = 0
ator = None


first_line = True #variável para ignorar o cabeçalho salvo

#laço para comparação de todos os valores salvos no dicionário e selecionar apenas o maior float
for actor, media in lista.items():
    if first_line:
        first_line = False
        continue
    if float(media) > maior:
        ator = actor
        maior = float(media)

resultado = 'parte-3.txt'

#comando padrão do python para printar o resultado no arquivo de saída
with open(resultado, 'w') as saida:
    print("Ator/atriz com maior média de receita bruta por filme:", ator, file=saida)