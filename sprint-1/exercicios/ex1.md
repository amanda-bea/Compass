```shell

#!/bin/bash

#processamento_de_vendas.sh - Script que cria as pastas, relatórios, arquivos e compacta os arquivos gerados
#Autora: Amanda Beatriz
#Descrição: Script que cria as pastas de vendas e backup, cria o arquivo de relatório relativo e compacta os arquivo de backup dos dados
#Data:31-07-2024                                                          

clear
mkdir vendas
cp dados_de_vendas.csv vendas
cd vendas/
RECENTE=$(cat dados_de_vendas.csv | tail -n 1 | cut -d"," -f5)
ANTIGA=$(cat dados_de_vendas.csv | head -n 2 | tail -n 1 | cut -d"," -f5)
ITENS=$(wc -l dados_de_vendas.csv | cut -c 1,2)
RESULTADO=$(expr $ITENS - 1)
mv dados_de_vendas.csv "dados-$(date +%Y%m%d).csv"
mkdir backup
cp "dados-$(date +%Y%m%d).csv" backup
cd backup/
mv "dados-$(date +%Y%m%d).csv" "backup-dados-$(date +%Y%m%d).csv"
touch "relatorio$(date +%d).txt"
echo "$(date +%Y/%m/%d) $(date +%H:%M.)" >> "relatorio$(date +%d).txt"
echo $ANTIGA >> "relatorio$(date +%d).txt"
echo $RECENTE >> "relatorio$(date +%d).txt"
echo $RESULTADO >> "relatorio$(date +%d).txt"
head -n 10 "backup-dados-$(date +%Y%m%d).csv" >> "relatorio$(date +%d).txt"
zip "backup-dados-$(date +%Y%m%d).zip" "backup-dados-$(date +%Y%m%d).csv"
rm "backup-dados-$(date +%Y%m%d).csv"
cd ../..
rm dados_de_vendas.csv
```