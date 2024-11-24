import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import pyspark.sql.functions as F
from pyspark.sql.types import IntegerType, DoubleType, StringType, LongType

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Nome do bucket
bucket_name = 'data-lake-amanda'

# Lista com 63 títulos baseados ou inspirados em fatos reais
midia_fatos_reais = [
    "My Brothers Keeper", "Kokain - Das Tagebuch der Inga L.", "Nacido para matar", "Prostitute Killer", "I Am DB Cooper",
    "Great Escapes with Morgan Freeman", "Beyond Reasonable Doubt", "FBI: The Untold Stories", "Exhibit A: Secrets of Forensic Science",
    "Cruise Ship Killers", "Kokoda", "Pandora's Box: Unleashing Evil", "Harbor Island", "Belle Epoque", "Ischeznuvshaya", "Unsolved",
    "Out of the Blue", "I Killed My BFF", "The Real Story with Maria Elena Salinas", "Women's Murder Club", "999: Killer On The Line",
    "Mastermind of Murder", "The Vanished", "Myra", "La Banda Grossi", "Never Forget", "The Little Things", "La Funcionaria Asesina",
    "Fissure", "Blitz Patrollie", "Bluff", "Smokin' Aces", "The World We Knew", "İtirazım Var", "Murder Under the Friday Night Lights",
    "Testament of Youth", "Revenge of the Green Dragons", "Cocaine Trade Exposed: The Invisibles", "American Vandal", "True Crime with Aphrodite Jones",
    "Bad Blood", "Papi - Ek Satya Katha", "The Taking of Pelham 1 2 3", "Cold Case Files", "Ek Thi Begum", "Fatal Frontier: Evil in Alaska",
    "Botoks", "Shoot the Messenger", "Estocolmo", "Bride Killa", "Al filo de la ley", "Skazana", "Pocivali u miru", "La mafia uccide solo d'estate",
    "Married with Secrets", "El marginal", "El Capo", "Criminal: UK", "The Jury Speaks", "Gumrah: End of Innocence", "Where Murder Lies",
    "Fatal Vows", "Cybergeddon"
]

# Carregar os dataframes usando GlueContext
df_tmdb = glueContext.create_dynamic_frame.from_catalog(database="sprint9", table_name="tmdb").toDF()
df_local = glueContext.create_dynamic_frame.from_catalog(database="sprint9", table_name="local").toDF()

# Verificar se as colunas existem e adicionar colunas ausentes com valores nulos para todas as colunas que não existem nos dois tipos de parquet
if 'original_name' not in df_tmdb.columns:
    df_tmdb = df_tmdb.withColumn('original_name', F.lit(None).cast(StringType()))
if 'first_air_date' not in df_tmdb.columns:
    df_tmdb = df_tmdb.withColumn('first_air_date', F.lit(None).cast(StringType()))

# Adicionar a coluna 'fatos_reais' ao df_tmdb
df_tmdb = df_tmdb.withColumn('fatos_reais',
    F.when((F.col('original_name').isin(midia_fatos_reais)) | (F.col('original_title').isin(midia_fatos_reais)) | (F.col('title').isin(midia_fatos_reais)), 1).otherwise(0))

# Adicionar a coluna 'fatos_reais' ao df_local
df_local = df_local.withColumn('fatos_reais',
    F.when(F.col('titulopincipal').isin(midia_fatos_reais), 1).otherwise(0))

# Seleção das colunas
df_tmdb = df_tmdb.select(
    F.col('budget').alias('orcamento'),
    F.col('id').cast(StringType()),
    F.col('original_language').alias('idioma_original'),
    'original_title', #vai ser excluída
    F.col('popularity').alias('popularidade'),
    'release_date', #vai ser excluída
    F.col('vote_average').alias('nota_media'),
    F.col('vote_count').alias('numero_votos'),
    F.col('revenue').alias('receita'),
    'original_name', #vai ser excluída
    'first_air_date', #vai ser excluída
    'fatos_reais'
)

df_local = df_local.select(
    F.col('id'),
    F.col('titulopincipal').alias('titulo'),
    F.col('anolancamento').alias('ano_lancamento'),
    F.col('notamedia').alias('nota_media').cast(DoubleType()),
    F.col('numerovotos').alias('numero_votos').cast(LongType()),
    'fatos_reais'
)

# Criar a coluna 'titulo' para o tmdb combinando 'original_name' e 'original_title'
df_tmdb = df_tmdb.withColumn('titulo', F.coalesce(F.col('original_name'), F.col('original_title')))
df_tmdb = df_tmdb.drop('original_name', 'original_title')

# Criar a coluna 'ano_lancamento' para o tmdb combinando 'release_date' e 'first_air_date'
df_tmdb = df_tmdb.withColumn('ano_lancamento', F.coalesce(F.col('release_date'), F.col('first_air_date')))
df_tmdb = df_tmdb.drop('release_date', 'first_air_date')

# Selecionar os quatro primeiros caracteres de 'ano_lancamento' e transformar em int
df_tmdb = df_tmdb.withColumn('ano_lancamento', F.col('ano_lancamento').substr(1, 4).cast(IntegerType()))

# Remover tuplas que não possuem 'titulo' ou 'idioma_original' se 'fatos_reais' for igual a 0
df_tmdb = df_tmdb.filter(~((F.col('fatos_reais') == 0) & (F.col('titulo').isNull() | F.col('idioma_original').isNull())))
df_local = df_local.filter(~((F.col('fatos_reais') == 0) & (F.col('titulo').isNull())))

# Selecionar mídias aleatórias que não tem fatos reais
df_tmdb_zeros = df_tmdb.filter(F.col('fatos_reais') == 0).orderBy(F.rand()).limit(30)
df_local_zeros = df_local.filter(F.col('fatos_reais') == 0).orderBy(F.rand()).limit(10)

# Selecionar todas as mídias com fatos reais
df_tmdb_uns = df_tmdb.filter(F.col('fatos_reais') == 1)
df_local_uns = df_local.filter(F.col('fatos_reais') == 1)
print(df_tmdb_uns.count())
print(df_local_uns.count())

# Unir os resultados
df_tmdb = df_tmdb_uns.union(df_tmdb_zeros)
df_local = df_local_uns.union(df_local_zeros)

# Adicionar colunas para combinar com df_tmdb
df_local = df_local.withColumn('orcamento', F.lit(None).cast(LongType()))
df_local = df_local.withColumn('receita', F.lit(None).cast(LongType()))
df_local = df_local.withColumn('popularidade', F.lit(None).cast(DoubleType()))
df_local = df_local.withColumn('idioma_original', F.lit(None).cast(StringType()))

# Unir os dataframes
df = df_tmdb.unionByName(df_local)

# Criar a tabela fato
fato_midia = df.select(
    'id',
    'fatos_reais',
    'popularidade'
)

# Criar dimensões
dim_info = df.select(
    'id',
    'idioma_original',
    'titulo',
    'ano_lancamento'
)

dim_avaliacao = df.select(
    'id',
    'nota_media',
    'numero_votos'
)

dim_receita = df.select(
    'id',
    'orcamento',
    'receita'
)

# Salvar as tabelas no S3
fato_midia.write.parquet(f"s3a://{bucket_name}/Refined/fato_midia/")
dim_info.write.parquet(f"s3a://{bucket_name}/Refined/dim_info/")
dim_avaliacao.write.parquet(f"s3a://{bucket_name}/Refined/dim_avaliacao/")
dim_receita.write.parquet(f"s3a://{bucket_name}/Refined/dim_receita/")

job.commit()
