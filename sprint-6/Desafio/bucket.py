import boto3
import os
from datetime import datetime

aws_access_key_id = "ASIA6JKEXSSE4BS7ZFAX"
aws_secret_access_key = "j/oYJbkDPcWsbR3SdXzkbbSJMHmPtOl+IxP3cT9T"
aws_session_token = "IQoJb3JpZ2luX2VjEKz//////////wEaCXVzLWVhc3QtMSJGMEQCIBQp5U1OhTvvr+vtyWx8cL3J+S53u7ioiHHo1iTBCA/qAiAu8UoLWSdpHaX7SC6J1iniuhtRk8epVHefcMdOiPeZpCqdAwgVEAAaDDk4MjA4MTA0OTczNyIMf3eXXw6GE7RzZUyHKvoCCLAGFeX57w5hzH8wPDvSJb9KFKDrXH3295HS4wcS8ByQ2XGzBTaJ4wdc2s5n/hKNNHmmYcVtewSJN+tb1rPsNzwYxI18Q7AqA2YGn5Qruuaj3O88wa2dhAfwZM/8e1LBSmrgfcjWtvbf3eE9apVR3pybaCH/PaW1ZbfsI/4eVXN5CQzycusFrqXzvOeL4Amm0MO2RQcH1p6iprJEGp9ynCrSqi1ipQzXmYskU74CiJ1x1o3h8JrmufvlELOI/rnAA3fbc7inazPQy0Gmn7ABe1RMZMujl/c4HuXMNaXiLznCw8aZ7OwwQRtHFxKdK6VzxmayiwytW9WBSwcr79X9Mx+AnShNUJHoMU1zXTG23H0jnPbMyq3oBAVTCB8DL3jX3djxQLy2Cc+Rx0AFo0kds4DmNoPo0I7GFJVoxdPSpnuEI/piGPAtqiHm2SOMr1MFr7Zx/gm/N+FyHo2GA9BKZvRVa5oWN8MwNJqUm4jRrJMuBwkCbGHvCX6lMJXUvrgGOqcBM9MnC5g0dT0p5GKZvu3hSWsQWd1yUPSN2cPNEISy5VIY2hu3dpwt8U0FwVP6NAY0HxE1Qrdl24wjC/1pGGWthXXogfQFC2f1nBc+zvpPPmHoSSn5sFL34j8Pn99C78Fii3ZEC8iAzfj/+QEAEUUJqNo9+H8co2Mxh7eVnLMtfOHWfSxMY1lDuXVGg3VX4bdnr1W4WjFW9NXEDORyoMhRVvRTPHJ9JEE="

bucket_name = "data-lake-amanda"
raw_zone = "Raw"
local = "Local"
csv = "CSV"
movies = "Movies"
series = "Series"
current_date = datetime.now().strftime("%Y/%m/%d")
movies_file_path = os.path.abspath("movies.csv")
series_file_path = os.path.abspath("series.csv")

session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token
)

# Cria o cliente S3
s3 = session.client("s3")

# Faz o upload dos arquivos
s3.upload_file(movies_file_path,
               bucket_name,
               os.path.join(raw_zone, local, csv, movies, current_date, "movies.csv"))
s3.upload_file(series_file_path,
               bucket_name,
               os.path.join(raw_zone, local, csv, series, current_date, "series.csv"))
