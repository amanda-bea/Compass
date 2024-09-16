saida = []

with open("estudantes.csv", 'r') as file:
    linhas = file.readlines()
        
    for linha in linhas:
        partes = linha.strip().split(',')

        nome = partes[0]
        notas = list(map(int, partes[1:]))

        ordem = sorted(notas, reverse=True) 
        maiores = ordem[:3]
        media = round(sum(maiores) / 3, 2)

        saida.append((nome, maiores, media))

saida.sort(key=lambda x: x[0])

for nome, maiores, media in saida:
    print(f'Nome: {nome} Notas: {maiores} Média: {media}')