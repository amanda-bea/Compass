from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import col, rand, when, floor

## Etapa 1
spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt")
df_nomes.show(5)

## Etapa 2
df_nomes.printSchema()

df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
df_nomes.show(10)

## Etapa 3
df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(rand() * 3 < 1, "Fundamental")
    .when(rand() * 3 < 2, "Médio")
    .otherwise("Superior")
)

## Etapa 4
paises = ["Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", "Equador", 
        "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela", "Guiana Francesa"]

#sql não funciona com acentos
df_nomes = df_nomes.withColumn(
    "Pais",
    when(rand() * 13 < 1, paises[0])
    .when(rand() * 13 < 2, paises[1])
    .when(rand() * 13 < 3, paises[2])
    .when(rand() * 13 < 4, paises[3])
    .when(rand() * 13 < 5, paises[4])
    .when(rand() * 13 < 6, paises[5])
    .when(rand() * 13 < 7, paises[6])
    .when(rand() * 13 < 8, paises[7])
    .when(rand() * 13 < 9, paises[8])
    .when(rand() * 13 < 10, paises[9])
    .when(rand() * 13 < 11, paises[10])
    .when(rand() * 13 < 12, paises[11])
    .otherwise(paises[12])
)


## Etapa 5
df_nomes = df_nomes.withColumn(
    "AnoNascimento",
    (floor(rand() * 65 + 1945 + 1).cast("int")) #diferença de anos + 1945 arredondado
) #round não funciona

df_nomes.show(10)

## Etapa 6
print("DF SELECT:")

df_select = df_nomes.filter((col("AnoNascimento") > 2000)) #com select
df_select.show(10)

## Etapa 7
df_nomes.createOrReplaceTempView("pessoas")
spark.sql("select Nomes, AnoNascimento from pessoas where AnoNascimento > 2000").show(10) #com SQL
df_nomes.show(10)

## Etapa 8
print("Número de pessoas da geração Millenial:")
millenials = df_nomes.filter((col("AnoNascimento") > 1980) & (col("AnoNascimento") < 1994)).count()
print(millenials)
#apresentar diretamente da erro

## Etapa 9
spark.sql("select count(*) from pessoas where AnoNascimento > 1980 and AnoNascimento < 1994").show()

#quantidade de pessoas de cada país das gerações abaixo: 
#(armazenar em novo dataframe, mostrar em ordem crescente de pais, geração e quantidade)

#Baby Boomers - 1944 a 1964
#Geração X - 1965 1979
#Millenials - 1980 a 1994
#Geração Z - 1995 a 2015


## Etapa 10
spark.sql(
    """select
        Pais,
        case
            when AnoNascimento between 1945 and 1964 then 'Baby Boomers'
            when AnoNascimento between 1965 and 1979 then 'Geração X'
            when AnoNascimento between 1980 and 1994 then 'Millenials'
            when AnoNascimento between 1995 and 2015 then 'Geração Y'
        end as Geracao,
        count(*) as Quantidade
    from pessoas
    group by Pais, Geracao
    order by Pais, Geracao, Quantidade"""
).show()

