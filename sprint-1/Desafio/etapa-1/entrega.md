## Entregas e reexecução

A pasta etapa-1 contém a pasta ecommerce criada na preparação para o desafio,
à partir dela estão os scripts criados e a pasta vendas gerada pelo script processamento_de_vendas.

* processamento_de_vendas:
O script contém comentários que explicam a linhas menos "óbvias" do código
e a descrição (Script que cria as pastas de vendas e backup, cria o arquivo de relatório relativo e
compacta os arquivo de backup dos dados).

* consolidador_de_processamento_de_vendas:
O script apenas transfere os dados dos relatórios gerados no arquivo de relatório final.

* Evidências geradas:
[Evidências](https://github.com/amanda-bea/Compass/tree/main/sprint-1/evidencias)


### Para reexecução:
1. Desafio
    1. Criar arquivo executável:
        Dentro da pasta ecommerce no terminal, o usuário deve digitar comando **"./processamento_de_vendas"**. Para criá-lo, uma sequência de comandos baseado em linux devem ser seguidas para realizar o gerenciamento solicitado, com o auxílio de comandos como o date e variáveis que tornam o código mais legível. O relatório é gerado a partir de variáveis que armazenam os dados anteriormente e comandos baseados em linux.
    2. Agendar a execução do processamento:
        O agendamento é realizado com o auxílio do programa cron, que realiza comandos no período solicitado pelo usuário linux.
        Digitando o comando **"crontab -e"** no terminal o usuário pode escolher o horário, dia, frequência e o comando a ser executado. No nosso casso é necessário digitar, no editor de texto, **"27 15 * * 1-4 cd /home/amanda/Compass/sprint-1/Desafio/etapa-1/ecommerce/ && ./processamento_de_vendas.sh"**, considerando o agendamento no sistema local. Sem esquecer do comando **"chmod +x",** que dá a todos usuários a permissão de execução do script.
    3. Criar novo relatório:
       Após pelo menos 3 relatórios gerados, na mesma pasta ecommerce executar o comando **"./consolidador_de_processamento_de_vendas"**, que apenas faz a junção de todos os relatórios em um arquivo só, após isso poderá usar "cat relatorio_final.txt" para ler o relatório.
