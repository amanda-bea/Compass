# Desafio


## Entregáveis
1. Evidências
[evidências](../evidencias/README.md)

2. Arquivo Python com cóidgo utilizado no AWS Lambda
[lambda.py](../Desafio/lambda.py)


## Explicações

### API

O TMDB foi a única API utilizada no desafio, pois sua base de dados é grande e detalhada o suficiente para que eu possa desenvolver o tema escolhido nesse desafio final. O filtro foi feito apenas com gênero Crime/Guerra da SQUAD 2 e filmes a partir dos anos 2000, já que acho interessante analisá-los(a bilheteria nos últimos anos mostram valores maiores do que anos atrás) e no CSV não haviam muitos.

### Tema

*Qual a diferença de avaliação/bilheteria de filmes baseados/inspirados ou não em fatos reais?*

Com esse tema irei fazer uma comparação entre o engajamento do público de filmes baseados/inspirados em fatos reais e os que não são, já que é uma curiosidade para mim porque tenho preferência pelos baseados em fatos reais, então desejo analisar para ver se realmente é um padrão entre o público.
A análise sera feita com base em dealhes especificados no próprio TMDB: avaliação e bilheteria.
Na maioria dos filmes também é possível extrair a informação de ser baseada pelos detalhes/overview fornecidos no banco de dados


## Etapas

1. **ETAPA 1**

Após o cadastro no site do TMDB tive acesso a uma chave de API que me permitiu fazer a requisições de filmes no BD.
A mesma chave foi salva como variável de ambiente no Lambda.
Para não gerar filmes iguais ao CSV realizo uma comparação com os filmes requisitados e os do já salvos no bucket como comentado no código [lambda](./lambda.py).

2. **ETAPA 2**

Também foi necessário criar duas camadas no Lambda: Pandas e Requests, as camadas foram criadas pelo zip dos arquivos gerados pelo pip install dentro de um container docker com o sistema linux da amazon para evitar erros de compatibilidade(similar ao que foi mostrado no LAB AWS Lambda).

3. **ETAPA 3**

Criação de uma função do zero, onde foi necessário mudar o tempo e memória para uma melhor execução.
