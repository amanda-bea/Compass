import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, rand
from datetime import datetime

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Locais usados
bucket_name = 'data-lake-amanda'
prefix3 = 'Raw/Local/CSV/Movies/2024/10/16/movies.csv'
prefix4 = 'Raw/Local/CSV/Series/2024/10/16/series.csv'

# Obter a data atual para o caminho de saída
data_atual = datetime.now()
ano = data_atual.year
mes = data_atual.month
dia = data_atual.day

# Ler filmes CSV com | como separador e ativar o cabeçalho
df_filmes_csv = spark.read.option("sep", "|").option("header", "true").csv(f"s3a://{bucket_name}/{prefix3}")

# Filtrar os filmes dos anos 1980 até 1999 usando a coluna 'anoLancamento'
df_filmes_csv_filtrados = df_filmes_csv.filter((col("anoLancamento") >= 1980) & (col("anoLancamento") <= 1999))
df_filmes_csv_aleatorios = df_filmes_csv_filtrados.orderBy(rand()).limit(20)

saida3 = f"s3a://{bucket_name}/Trusted/Local/PARQUET/Movies/{ano}/{mes}/{dia}/filmes1.parquet"
df_filmes_csv_aleatorios.write.parquet(saida3)

# Ler séries CSV com | como separador e ativar o cabeçalho
df_series_csv = spark.read.option("sep", "|").option("header", "true").csv(f"s3a://{bucket_name}/{prefix4}")

# Filtrar as séries dos anos 1980 até 1999 usando a coluna 'anoLancamento'
df_series_csv_filtrados = df_series_csv.filter((col("anoLancamento") >= 1980) & (col("anoLancamento") <= 1999))
df_series_csv_aleatorios = df_series_csv_filtrados.orderBy(rand()).limit(20)

saida4 = f"s3a://{bucket_name}/Trusted/Local/PARQUET/Series/{ano}/{mes}/{dia}/series1.parquet"
df_series_csv_aleatorios.write.parquet(saida4)

job.commit()