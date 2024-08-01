#!/bin/bash
####################################################################################################################
#                                                                                                                  #
#  processamento_de_vendas.sh - Script que cria as pastas, relatórios, arquivos e compacta os arquivos gerados     #
#  Autora: Amanda Beatriz                                                                                          #
#  Descrição: Script que cria as pastas de vendas e backup, cria o arquivo de relatório relativo e                 #
#  compacta os arquivo de backup dos dados                                                                         #
#  Data: 31/07/2024                                                                                                #
#                                                                                                                  #
####################################################################################################################
clear
mkdir vendas
cp dados_de_vendas.csv vendas
cd vendas/
cat dados_de_vendas.csv | cut -d"," -f5 >> auxiliar.txt
#um arquivo auxiliar temporário é criado para receber apenas as datas das vendas, que são delimitadas no quinto campo do arquivo
ANTIGA=$(cat auxiliar.txt | sort -k3 -t "/" -g | cat auxiliar.txt | sort -k3 -t "/" -g | sort -k2 -t "/" -g | grep -v "data" | head -n 1)
#criação de variável, para melhor legibilidade, que armazena a data mais antiga a partir da ordenação do ano e mês
#a exclusão da palavra "data" é feita para não ser considerada na ordenação
RECENTE=$(cat auxiliar.txt | sort -k3 -t "/" -g | cat auxiliar.txt | sort -k3 -t "/" -g | sort -k2 -t "/" -g | grep -v "data" | tail -n 1)
#a mesma ordenação é feita da mesma forma, mas dessa vez pega a última linha da ordenação
ITENS=$(wc -l dados_de_vendas.csv | cut -c 1,2)
#uma varíavel armazena o número de linhas, que indicam o número de itens vendidos
#o cut pega apenas os dois primeiros caracteres para ser usado na contabilização posterior
RESULTADO=$(expr $ITENS - 1)
#o número de linhas é contabilizado - 1 por conta da primeira linha que é apenas de instrução
rm auxiliar.txt
#exclusão do arquivo temporário
mv dados_de_vendas.csv "dados-$(date +%Y%m%d).csv"
#renomeação do arquivo usando o comando date para atendar os critérios de data
mkdir backup
cp "dados-$(date +%Y%m%d).csv" backup
cd backup/
mv "dados-$(date +%Y%m%d).csv" "backup-dados-$(date +%Y%m%d).csv"
touch "relatorio$(date +%d).txt"
#criação do arquivo que irá receber os dados do relatório
#uso do comando date para criação de relatórios diferentes, considerando que o processo é realizado apenas uma vez por dia
echo "$(date +%Y/%m/%d) $(date +%H:%M.)" >> "relatorio$(date +%d).txt"
#concatenação da data do sistema no relatório atual
echo $ANTIGA >> "relatorio$(date +%d).txt"
echo $RECENTE >> "relatorio$(date +%d).txt"
echo $RESULTADO >> "relatorio$(date +%d).txt"
#concatenação das variáveis geradas anteriormente no relatório
head -n 10 "backup-dados-$(date +%Y%m%d).csv" >> "relatorio$(date +%d).txt"
#primeiras 10 linhas do arquivo de backup é concatenado
zip "backup-dados-$(date +%Y%m%d).zip" "backup-dados-$(date +%Y%m%d).csv"
rm "backup-dados-$(date +%Y%m%d).csv"
cd ../..
rm dados_de_vendas.csv
