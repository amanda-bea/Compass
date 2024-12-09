# Desafio

## Sprint 6

A primeira etapa consistiu na criação de um container docker para a criação do data lake no S3, com ele todos os dados inicias do csv como volume.

## Sprint 7

Na etapa de ingestão por API, foi necessário realizar requisições usando o Lambda para a injeção de mais dados para análise no bucket.

## Sprint 8

Criação da camada Trusted: O Glue foi utilizado para a criação da camada com os arquivos reformatados para parquet e um pouco mais refinados, para a prevenção de erros, usando o Spark.

## Sprint 9

Camada Refined: Tratamento final dos dados usando novamente o Spark no Glue, com formato e informações prontas para análise.


## Sprint 10

Visualização dos dados, respondendo todas as perguntas da análise usando o QuickSight.
