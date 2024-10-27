# Desafio

## Tema
*Qual a diferença de avaliação/bilheteria de filmes baseados/inspirados ou não em fatos reais?*

Com esse tema irei fazer uma comparação entre o engajamento do público de filmes baseados/inspirados em fatos reais e os que não são, já que é uma curiosidade para mim porque tenho preferência pelos baseados em fatos reais, então desejo analisar para ver se realmente é um padrão entre o público.


## Entregáveis
1. Dockerfile
[Dockerfile](../Desafio/Dockerfile)

2. Arquivo python
[bucket.py](../Desafio/bucket.py)


## Etapas

1. **ETAPA 1**

Criação do bucket data-lake-amanda ainda sem objetos pelo próprio console da AWS.

2. **ETAPA 2**

Criação do arquivo [bucket.py](../Desafio/bucket.py) com o código que insere os objetos no bucket criado com os arquivos CSV do desafio.
No código precisei especificar as chaves de acesso para acessar o console dentro do container pelo boto3, já que ele não reconhece as credencias da máquina local.

3. **ETAPA 3**

Criação do Dockerfile [Dockerfile](../Desafio/Dockerfile) que transforma o código em container e os dois arquivos CSV em volume para o container. Após essa etapa o container pode ser executado para criar os objetos na RAW Zone.
