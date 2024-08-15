# Projeto




# Exercícios

Ao executar os exercícios primeiramente no DBeaver, o SGDB retornava o código solicitado ou o erro, alguns exerícios foram mais complicados como o 4 ou a partir do 8 que precisei utilizar "subqueries". Todas as evidências dos códigos em: [Evidências](../exercicios/) (Formato PNG e TXT)

![Exercício 1](../exercicios/biblioteca/E01.png)

![Exercício 4](../exercicios/biblioteca/E04.png)

![Exercício 4](../exercicios/loja/E09.png)

Utilização de "SubQuery"
![Exercício 4](../exercicios/loja/E10.png)
[Exercício 4](../exercicios/biblioteca/E04.txt)

![Exercício 4](../exercicios/loja/E14.png)


# Exportação de dados

A parte principal da exportação de dados foi feita pela interface gráfica do DBeaver onde era possível escolher o separador dos arquivos .csv e comandos básicos de SQLite. Resultados:
[Separador "|"](../exercicios/exportação/5_Editoras.csv)
[Separador ";"](../exercicios/exportação/10_MaisCaros.csv)


# Desafio

A execução do desafio começou pela normalização da tabela fornecida até a terceira forma normal, para chegar nesse nível de formalização precisei separar em tabelas menores ligando cada coluna a sua chave na tabela, utilização do select distinct para não repetir valores nas tabelas em que fosse necessário e por último a criação do diagrama usando o Astah após tentativas falhas no DBeaver. Códigos usados para a criação das tabelas menores e mais específicas em: [Tabelas](../evidencias/tabelas.txt)
Exemplo criação e inserção dos dados em tabelas:
![Criação](../evidencias/criatabela.png)

![Inserção](../evidencias/inseredados.png)

Após fazer o mesmo com todas as tabelas esse foi o resultado

![relacional](../evidencias/relacional1.png)

![relacional](../evidencias/relacional2.png)

![relacional](../evidencias/relacional3.png)

O mesmo processo foi empregado para a criação da tabela dimensional, mas dessa vez com a criação de uam tabela fato que liga a todas as tabelas dimensão, gerando as tabelas:

![dimensional](../evidencias/dimensional1.png)

![dimensional](../evidencias/dimensional2.png)

![dimensional](../evidencias/dimensional3.png)

O modelo relacional e dimensional geraram os seguintes diagramas, respectivamente:

![relacional](../evidencias/relacional.png)
![dimensional](../evidencias/dimensional.sqlite.png)
