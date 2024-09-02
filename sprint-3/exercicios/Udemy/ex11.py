import json

arquivo = open('person.json')
dados = json.load(arquivo)
arquivo.close()
print(dados)
