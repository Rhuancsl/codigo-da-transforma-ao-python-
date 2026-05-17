import requests

API_KEY = "SUA_CHAVE_AQUI"
cidade = "São Paulo"
url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"

try:
    resposta = requests.get(url, timeout=5)  # timeout de 5 segundos
    resposta.raise_for_status()
    dados = resposta.json()
    print("Dados recebidos com sucesso!")
except requests.exceptions.Timeout:
    print("Erro: tempo de resposta excedido.")
except requests.exceptions.HTTPError as e:
    print("Erro HTTP:", e)
except requests.exceptions.RequestException as e:
    print("Erro de conexão:", e)
