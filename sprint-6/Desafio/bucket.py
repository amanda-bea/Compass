import boto3
import os
from datetime import datetime

aws_access_key_id = "APIKEY"
aws_secret_access_key = "APISECRETACCESS"
bucket_name = "midia-bucket"
raw_zone = "Raw"
local = "Local"
csv = "CSV"
movies = "Movies"
series = "Series"
current_date = datetime.now().strftime("%Y/%m/%d")
movies_file_path = os.path.abspath("movies.csv")
series_file_path = os.path.abspath("series.csv")

s3 = boto3.client("s3",
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)

s3.upload_file(movies_file_path,
               bucket_name,
               os.path.join(raw_zone, local, csv, movies, current_date, "movies.csv"))
s3.upload_file(series_file_path,
               bucket_name,
               os.path.join(raw_zone, local, csv, series, current_date, "series.csv"))
