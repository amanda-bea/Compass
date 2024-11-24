import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from datetime import datetime

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Locais usados
bucket_name = 'data-lake-amanda'
prefix_filmes = 'Raw/TMDB/JSON/2024/10/26/media_filmes'
prefix_series = 'Raw/TMDB/JSON/2024/10/26/media_series'
prefix_novof = 'Raw/TMDB/JSON/2024/10/26/novo_filmes'

# Obter data para saída
data_atual = datetime.now()
ano = data_atual.year
mes = data_atual.month
dia = data_atual.day

# Saída usadas
saida1 = f"s3a://{bucket_name}/Trusted/TMDB/PARQUET/Movies/{ano}/{mes}/{dia}/filmes.parquet"
saida2 = f"s3a://{bucket_name}/Trusted/TMDB/PARQUET/Series/{ano}/{mes}/{dia}/series.parquet"

# Set para ler múltiplas linhas
df_filmesa = spark.read.option("multiline", "true").json(f"s3a://{bucket_name}/{prefix_filmes}*")
df_novos_filmes = spark.read.option("multiline", "true").json(f"s3a://{bucket_name}/{prefix_novof}*")

df_filmes = df_filmesa.union(df_novos_filmes)

# Explodir filmes usando o spark
df_filmes_explodido = df_filmes.selectExpr("explode(filmes) as filme")

# Filtro das colunas necessárias para minha análise
df_filmes_final = df_filmes_explodido.select(
    col("filme.budget"),
    col("filme.id"),
    col("filme.original_language"),
    col("filme.original_title"),
    col("filme.overview"),
    col("filme.popularity"),
    col("filme.release_date"),
    col("filme.title"),
    col("filme.vote_average"),
    col("filme.vote_count"),
    col("filme.revenue")
)

# Mesmo processo para séries
df_series = spark.read.option("multiline", "true").json(f"s3a://{bucket_name}/{prefix_series}*")
df_series_explodido = df_series.selectExpr("explode(series) as serie")

df_series_final = df_series_explodido.select(
    col("serie.id"),
    col("serie.original_language"),
    col("serie.original_name"),
    col("serie.overview"),
    col("serie.popularity"),
    col("serie.first_air_date"),
    col("serie.vote_average"),
    col("serie.vote_count")
)

# Upload dos arquivos gerados
df_filmes_final.write.parquet(saida1)
df_series_final.write.parquet(saida2)

job.commit()
