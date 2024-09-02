with open('arquivo_texto.txt', 'rt', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    print(linha, end='')