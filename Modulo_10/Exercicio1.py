import requests

API_KEY = "SUA_CHAVE_AQUI"  # substitua pela sua chave do OpenWeatherMap
cidade = "São Paulo"
url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()  # lança erro se status != 200
    dados = resposta.json()
    print(dados)
except requests.exceptions.RequestException as e:
    print("Erro na requisição:", e)
