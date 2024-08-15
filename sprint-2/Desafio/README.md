# Desafio

1. Normalização
    1.1 Primeira Forma Normal
        Na primeira forma normal separei a tabela inical em tabelas menores para separar os colunas que possuiam mais de um dado e aproveitei os formatos de data que já estavam separados em data e hora.
    1.2 Segunda Forma Normal
        Separei em mais tabelas para juntar cada coluna dependente de sua chave, colocando tabelas por categora, ex: Cliente, Vendedor e etc.
    1.3 Terceira Forma Normal
        Eliminação de atributos dependentes de outro na tabela, no caso separei o endereço do cliente ta tabela cliente.

2. Desenhos

    * Modelagem Relacional
    ![Relacional](../evidencias/relacional.png)
    Obs: o modelo no DBeaver não gerou o relacionamento desejado, o programa utilizado foi o Astah utlizando o modelo de diagrama de classes mas similar ao crow's foot.

    * Modelagem Dimensional
    ![Dimensional](../evidencias/dimensional.sqlite.png)

3. Entregáveis

* Arquivos SQL gerados:
[Relacional](../evidencias/concessionariarelacional.sqlite)
[Dimensional](../evidencias/concessionariadimensional.sqlite)


## Detalhes

O modelo dimensional gerado foi o star pela falta de relações entre as dimensões e por ser mais comum.
Leitura dos conceitos de BigData realizada.