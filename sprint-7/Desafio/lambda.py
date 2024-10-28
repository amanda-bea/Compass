import json 
import requests 
import pandas as pd 
import boto3 
import os 

def lambda_handler(event, context): 
    S3_CLIENT = boto3.client('s3') 
    BUCKET = 'data-lake-amanda'
    
    API_KEY = os.getenv('API_KEY')
        
    # Lê os IDs dos filmes já salvos no bucket
    objeto_filmes = S3_CLIENT.get_object(Bucket=BUCKET, Key='Raw/Local/CSV/Movies/2024/10/16/movies.csv') 
    filmes_imdb = pd.read_csv(objeto_filmes['Body'], sep='|', low_memory=False) 
    ids_filmes_existentes = set(filmes_imdb['id'].drop_duplicates())

    # Lê os IDs das séries já salvas no bucket
    objeto_series = S3_CLIENT.get_object(Bucket=BUCKET, Key='Raw/Local/CSV/Series/2024/10/16/series.csv') 
    series_imdb = pd.read_csv(objeto_series['Body'], sep='|', low_memory=False) 
    ids_series_existentes = set(series_imdb['id'].drop_duplicates())

    filmes_lista = [] 
    series_lista = []
    
    generos_interesse = {"War", "Crime", "war", "crime"}
    
    contador_filmes = 0
    contador_series = 0

    # Processa filmes
    for id_imdb in ids_filmes_existentes: 
        url = f"https://api.themoviedb.org/3/find/{id_imdb}?api_key={API_KEY}&language=pt-BR&external_source=imdb_id" 
        response = requests.get(url) 
        data = response.json()

        if data['movie_results']: 
            id_tmdb = data['movie_results'][0]['id'] 
            if id_tmdb not in ids_filmes_existentes: 
                url = f"https://api.themoviedb.org/3/movie/{id_tmdb}?api_key={API_KEY}&language=pt-BR" 
                response = requests.get(url) 
                tmdb = response.json()

                # Verifica o ano de lançamento do filme
                ano_lancamento = tmdb.get('release_date', '')[:4] 
                # Verifica se o filme é do gênero desejado
                generos_filme = {genre['name'] for genre in tmdb.get('genres', [])}
                if ano_lancamento and int(ano_lancamento) >= 2000 and generos_filme.intersection(generos_interesse):
                    filmes_lista.append(tmdb)

            # Checa se chegou a 20 filmes
            if len(filmes_lista) >= 20: 
                # Salva em um arquivo e faz o upload
                json_data = { "filmes": filmes_lista, "series": series_lista } 
                contador_filmes += 1
                save_path = f'Raw/TMDB/JSON/2024/10/26/media_filmes_{contador_filmes}.json' 
                S3_CLIENT.put_object(Body=json.dumps(json_data, ensure_ascii=False, indent=4), Bucket=BUCKET, Key=save_path) 
                filmes_lista = []  # Reinicia a lista de filmes

    # Processa séries
    for id_imdb in ids_series_existentes: 
        url = f"https://api.themoviedb.org/3/find/{id_imdb}?api_key={API_KEY}&language=pt-BR&external_source=imdb_id" 
        response = requests.get(url) 
        data = response.json()
        
        if data['tv_results']: 
            id_tmdb = data['tv_results'][0]['id'] 
            if id_tmdb not in ids_series_existentes: 
                url = f"https://api.themoviedb.org/3/tv/{id_tmdb}?api_key={API_KEY}&language=pt-BR" 
                response = requests.get(url) 
                tmdb = response.json()

                ano_lancamento = tmdb.get('first_air_date', '')[:4] 

                generos_serie = {genre['name'] for genre in tmdb.get('genres', [])}
                if ano_lancamento and int(ano_lancamento) >= 2000 and generos_serie.intersection(generos_interesse):
                    series_lista.append(tmdb)

            
            if len(series_lista) >= 20: 
                # Salva em um arquivo e faz o upload
                json_data = { "filmes": filmes_lista, "series": series_lista } 
                contador_series += 1
                save_path = f'Raw/TMDB/JSON/2024/10/26/media_series_{contador_series}.json' 
                S3_CLIENT.put_object(Body=json.dumps(json_data, ensure_ascii=False, indent=4), Bucket=BUCKET, Key=save_path) 
                series_lista = []  # Reinicia a lista de séries

    if filmes_lista or series_lista:
        json_data = { "filmes": filmes_lista, "series": series_lista } 
        contador_filmes += 1  
        save_path = f'Raw/TMDB/JSON/2024/10/26/media_filmes_{contador_filmes}.json' 
        S3_CLIENT.put_object(Body=json.dumps(json_data, ensure_ascii=False, indent=4), Bucket=BUCKET, Key=save_path)

    return {'statusCode': 200}
