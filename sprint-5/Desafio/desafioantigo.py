import boto3

#Após alteração no desafio:
arquivo = 'entrada.csv'
bucket = 'entrada-imigrantes'
resultado = 'resultado.csv'

s3 = boto3.client('s3')

s3.upload_file(arquivo, bucket, arquivo)


session = boto3.Session(profile_name='AdministratorAccess-982081049737') #perfil setado após erros de login
s3 = session.client('s3')
bucket_name = 'entrada-imigrantes' #nome do bucket criado
file_key = 'entrada.csv' #nome do arquivo analisado


query = """
SELECT 
    CAST(MAX(
        CASE 
            WHEN datachegada LIKE '%/%' THEN 
                CAST(SUBSTRING(datachegada, 7) AS INT)
            ELSE 
                CAST(SUBSTRING(datachegada, 1, 4) AS INT)
        END
    ) AS INT) - 
    CAST(MIN(
        CASE 
            WHEN datachegada LIKE '%/%' THEN 
                CAST(SUBSTRING(datachegada, 7) AS INT)
            ELSE 
                CAST(SUBSTRING(datachegada, 1, 4) AS INT)
        END
    ) AS INT) AS diferenca_anos
FROM S3Object
WHERE Sobrenome = 'de Jesus' OR Sobrenome = 'de Carvalho' OR Sobrenome = 'Carvalho' OR Sobrenome = 'Marques'
"""


try:
    response = s3.select_object_content(
        Bucket=bucket_name,
        Key=file_key,
        Expression=query,
        ExpressionType='SQL',
        InputSerialization={
            'CSV': {
                'FileHeaderInfo': 'USE', 
                'RecordDelimiter': '\n',   
                'FieldDelimiter': ';'  #delimitador do meu CSV   
            }
        },
        OutputSerialization={
            'CSV': {}
        }
    )

    results = []

    for event in response['Payload']:
        if 'Records' in event:
            results.append(event['Records']['Payload'].decode('utf-8').strip())
    for result in results:
        print(result)

    #Alteração do desafio:
    with open('resultado.csv', 'w') as file:
        for result in results:
            file.write(result + '\n')

    s3.upload_file(resultado, bucket, resultado)       

except Exception as e:
    print(f"Ocorreu um erro: {e}") #identificador de erros
