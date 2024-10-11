import boto3

# Crie um cliente S3
s3_client = boto3.client('s3')

# Parâmetros da consulta
bucket_name = 'entrada-imigrantes'
object_key = 'entrada.csv'
expression = """
SELECT * FROM S3Object WHERE sobrenome = 'de Jesus'
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

