import boto3
import pandas as pd

#função para extrair susbtring com ano da data usando comparações e conversão
def extrair_ano(datachegada):
    if '/' in datachegada:
        return int(datachegada[6:10])
    else:
        return int(datachegada[0:4])

arquivo = 'entrada.csv'
bucket = 'entrada-imigrantes'
resultado = 'resultado.csv'

s3 = boto3.session.Session(profile_name='AdministratorAccess-982081049737').client('s3')

s3.upload_file(arquivo, bucket, arquivo)

#lendo o CSV com ';' como separador
df = pd.read_csv(arquivo, sep=';') 

#filtragem com base nos sobrenomes
df_filtrado = df[
    (df['Sobrenome'].str.lower().isin(['marques'])) |
    (df['Sobrenome'].str.lower().isin(['carvalho', 'de carvalho'])) |
    (df['Sobrenome'].str.lower().isin(['jesus', 'de jesus']))
]

#aplicação da função de extrair data
df_filtrado['ano'] = df_filtrado['datachegada'].apply(extrair_ano)

#função de agregação para encontrar data mais antiga e recente do df
ano_max = df_filtrado['ano'].max()
ano_min = df_filtrado['ano'].min()

#conversão das datas encontradas para o formato de data
data_max = pd.to_datetime(str(ano_max) + '-01-01')
data_min = pd.to_datetime(str(ano_min) + '-01-01')

#resultado da query
diferenca = data_max - data_min
diferenca_em_anos = diferenca.days // 365

session = boto3.Session(profile_name='AdministratorAccess-982081049737') #perfil setado após erros de login
s3 = session.client('s3')

#salvando o resultado no CSV com ';' como separador
with open(resultado, 'w') as file:
    file.write(str(diferenca_em_anos) + '\n')

s3.upload_file(resultado, bucket, resultado)
