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
RECENTE=$(cat dados_de_vendas.csv | tail -n 1 | cut -d"," -f5)
#criação de variável, para melhor legibilidade, que armazena a data mais recente
#o comando tail pega a última linha do arquivo, o cut divide a linha em campos para separar apenas a data
ANTIGA=$(cat dados_de_vendas.csv | head -n 2 | tail -n 1 | cut -d"," -f5)
#dessa vez pega a as duas primeiras linhas, e em sequida apenas a última linha das duas, já que a primeira linha do arquivo é de instrução
ITENS=$(wc -l dados_de_vendas.csv | cut -c 1,2)
#uma varíavel armazena o número de linhas, que indicam o número de itens vendidos
#o cut pega apenas os dois primeiros caracteres para ser usado na contabilização posterior
RESULTADO=$(expr $ITENS - 1)
#o número de linhas é contabilizado - 1 por conta da primeira linha que é apenas de instrução
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
#primeiras 10 linhas do arquivo de backup são concatenadas no relatório usando o head
zip "backup-dados-$(date +%Y%m%d).zip" "backup-dados-$(date +%Y%m%d).csv"
#coamando zip para compactar o arquivo de backup
rm "backup-dados-$(date +%Y%m%d).csv"
cd ../..
rm dados_de_vendas.csv