import json
import requests
import pandas as pd
import boto3
import apikey

def main():

    profile_name = "AdministratorAccess-982081049737"  # Replace with your actual profile name
    session = boto3.Session(profile_name=profile_name)
    
    S3_CLIENT = session.client('s3')
    BUCKET = 'data-lake-amanda'
    
    #chave api
    API_KEY = apikey.api_key
        
    #le o filmes já salvos no bucket
    objeto = S3_CLIENT.get_object(Bucket=BUCKET, Key='Raw/Local/CSV/Movies/2024/10/16/movies.csv')
    filmes_imdb = pd.read_csv(objeto['Body'], sep='|', low_memory=False)  #low_memory por conta do warning
    filmes_imdb = filmes_imdb.drop_duplicates(subset=['id']) #exclui do df os filmes duplicados para otimiazação
    
    #pega filmes a partir dos anos 2000
    filmes_imdb['anoLancamento'] = filmes_imdb['anoLancamento'].replace('\\N', '0')
    imdb_filtro = filmes_imdb[
        (filmes_imdb.genero.str.contains("Crime|War", regex=True)) & 
        (filmes_imdb.anoLancamento.astype(int) >= 2000)
    ]
    
    #lista para salvar os filmes
    movies_lista = []
    
    #For que pega o id do filme para comparar com o arquivo já salvo, se for um filme novo coleta mais informações
    for filme in imdb_filtro.values:
        id_imdb = filme[0] #pega ID
        
        #Procura o filme
        url = f"https://api.themoviedb.org/3/find/{id_imdb}?api_key={API_KEY}&language=pt-BR&external_source=imdb_id"
        response = requests.get(url)
        data = response.json()
        
        try:
            id_tmdb = data['movie_results'][0]['id']
            
            url = f"https://api.themoviedb.org/3/movie/{id_tmdb}?api_key={API_KEY}&language=pt-BR"
            response = requests.get(url)
            tmdb = response.json()
            
            #Adiciona as infos
            movies_lista.append(tmdb)
            
            #Checa se chegou a 100 filmes, como solicitado na documentação
            if len(movies_lista) >= 100:
                break
                
        except (IndexError, KeyError):
            continue
    

    if movies_lista:
        #Converte para JSON
        json_data = json.dumps(movies_lista, ensure_ascii=False, indent=4)
        
        #Caminho para salvar no bucket
        file_path = 'Raw/TMDB/JSON/2024/10/26/filmes.json'
        
        #Upload para o bucket
        S3_CLIENT.put_object(Body=json_data, Bucket=BUCKET, Key=file_path)

if __name__ == "__main__":
    main()
