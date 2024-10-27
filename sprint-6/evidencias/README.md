# Exercícios

## Lab AWS Athena
O laboratório do Athena começa com as configurações básicas dentro do console de escolha de arquivo em um bucket e criação da tabela pela interface que gerou o código abaixo:
![createtable](../evidencias/createtable.png)

Após isso foram realizados alguns cósigos fornecidos na Udemy para testes, depois do teste é solicitado a criação do código abaixo para a listagem dos nomes mais usados por década.
![query](../evidencias/athena_query.png)

E parte do resultado foi esse:
![resultado](../evidencias/athena_result.png)


## Lab AWS Lambda

O laboratório lambda foi um pouco mais complexo, após a etapa de criação da função no console usei o código fornecido na Udemy para implementar a função do lambda.
![code](../evidencias/lambda_code.png)

E o resultado após o test no lambda foi esse:
![result](../evidencias/lambda_result.png)

Para obter esse resultado foi necessário criar uma camada(layer) no Lambda para implemnetar a biblioteca pandas na minha função na AWS. Para isso segui os passos da criação de um container com o docker para salvar os arquivos a serem salvos na layer. Abaixo o arquivo Dockerfile criado e imagens da criação:

[dockerfile](../exercícios/Dockerfile)

![layer](../evidencias/layer_create.png)



# Desafio

Para a execução do desafio antes de tudo foi necessário criar um bucket pelo próprio consolde da AWS que nomeei de 'data-lake-amanda'.
![bucket](../evidencias/datalake.png)

Após isso foi necessário a criação do código [bucket.py](../Desafio/bucket.py) em que copio os arquivos CSV da minha máquina localmente. Porém o desafio era executar esse código em um container em que o csv são volumes, então precisei adaptar o código adicionando as chaves de acesso (única forma que consegui). Abaixo imagens da criação do container e utilização dos volumes:
![docker build](../evidencias/dockerbuild.png)
![volume](../evidencias/volume.png)

O resultado foi gerado na AWS, onde foram criadas a pastas da Raw Zone no S3, abaixo a navegação pelas pastas até a chegada nos arquivos CSV salvos:
![raw](./rawzone.png)
![movies e series](./movies_series.png)
E por fim o arquivo movies.csv como exemplo:
![csv](./csv.png)


# Certificados

## Ceritificados AWS

![Athena](../Certificados/athena_page-0001.jpg)
![EMR](../Certificados/emr_page-0001.jpg)
![Fundamentos 1](../Certificados/fundamentos1_page-0001.jpg)
![Fundamentos 2](../Certificados/fundamentos2_page-0001.jpg)
![Glue](../Certificados/glue_page-0001.jpg)
![QuickSight](../Certificados/quicksight_page-0001.jpg)
![Redshift](../Certificados/redshift_page-0001.jpg)
![Redshift](../Certificados/redshift2_page-0001.jpg)
![Serveless](../Certificados/serveless_page-0001.jpg)
