import requests

API_KEY = "SUA_CHAVE_TMDB"
filme = "Inception"
url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={filme}&language=pt-BR"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()

    if dados["results"]:
        filme_info = dados["results"][0]
        titulo = filme_info["title"]
        genero_ids = filme_info["genre_ids"]
        sinopse = filme_info["overview"]

        print(f"Título: {titulo}")
        print(f"Gêneros (IDs): {genero_ids}")
        print(f"Sinopse: {sinopse}")
    else:
        print("Nenhum filme encontrado.")
except requests.exceptions.RequestException as e:
    print("Erro ao buscar filme:", e)
