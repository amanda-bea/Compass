#código utilizando dentro do shell PySpark

sc = SparkContext.getOrCreate()

texto = sc.textFile("README.md")
contagem = texto.flatMap(lambda linha: linha.split(" ")).map(lambda palavra: (palavra, 1)).reduceByKey(lambda a, b: a + b)
results = contagem.collect()

for palavra, contangem in results:
    print(f"{palavra} :{contangem}")
