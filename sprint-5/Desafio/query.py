import boto3

# Crie um cliente S3
s3_client = boto3.client('s3')

# Parâmetros da consulta
bucket_name = 'bucket-entrada-imigrantes'
object_key = 'entrada.csv'
expression = """
    SELECT 
        AVG(CAST(YEAR(data_nascimento) AS INTEGER)) AS media_ano_nascimento,
        COUNT(*) AS total_registros
    FROM S3Object
    WHERE 
        cidade = 'Rio de Janeiro' AND 
        status = 'Nada consta'
    GROUP BY cidade
    HAVING 
        media_ano_nascimento > 1800 AND 
        COUNT(*) > 5
"""
expression_type = 'SQL'
input_serialization = {
    'CSV': {
        'FileHeaderInfo': 'USE'
    }
}
output_serialization = {
    'CSV': {}
}

# Execute a consulta
response = s3_client.select_object_content(
    Bucket=bucket_name,
    Key=object_key,
    Expression=expression,
    ExpressionType=expression_type,
    InputSerialization=input_serialization,
    OutputSerialization=output_serialization,
)

# Processar a resposta
for event in response['Payload']:
    if 'Records' in event:
        print(event['Records']['Payload'].decode('utf-8'))

