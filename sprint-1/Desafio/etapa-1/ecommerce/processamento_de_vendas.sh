#!/bin/bash

clear
mkdir vendas
cp dados_de_vendas.csv vendas
cd vendas/
cat dados_de_vendas.csv | cut -d"," -f5 >> auxiliar.txt
ANTIGA=$(cat auxiliar.txt | sort -k3 -t "/" -g | cat auxiliar.txt | sort -k3 -t "/" -g | sort -k2 -t "/" -g | grep -v "data" | head -n 1)
RECENTE=$(cat auxiliar.txt | sort -k3 -t "/" -g | cat auxiliar.txt | sort -k3 -t "/" -g | sort -k2 -t "/" -g | grep -v "data" | tail -n 1)
ITENS=$(wc -l dados_de_vendas.csv | cut -c 1,2)
RESULTADO=$(expr $ITENS - 1)
rm auxiliar.txt
mv dados_de_vendas.csv "dados-$(date +%Y%m%d).csv"
mkdir backup
cp "dados-$(date +%Y%m%d).csv" backup
cd backup/
mv "dados-$(date +%Y%m%d).csv" "backup-dados-$(date +%Y%m%d).csv"
touch relatorio1.txt
echo "$(date +%Y/%m/%d) $(date +%H:%M.)" >> relatorio1.txt
echo $ANTIGA >> relatorio1.txt
echo $RECENTE >> relatorio1.txt
echo $RESULTADO >> relatorio1.txt
head -n 10 "backup-dados-$(date +%Y%m%d).csv" >> relatorio1.txt
zip "backup-dados-$(date +%Y%m%d).zip" "backup-dados-$(date +%Y%m%d).csv"
rm "backup-dados-$(date +%Y%m%d).csv"
cd ../..
rm dados_de_vendas.csv
