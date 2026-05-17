import requests

API_KEY = "SUA_CHAVE_AQUI"
cidade = "São Paulo"
url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"

resposta = requests.get(url)
dados = resposta.json()

temperatura = dados["main"]["temp"]
condicoes = dados["weather"][0]["description"]

print(f"Temperatura atual em {cidade}: {temperatura}°C")
print(f"Condições climáticas: {condicoes}")
