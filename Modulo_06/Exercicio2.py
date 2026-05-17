import json

# Dicionário de clientes
clientes = {
    "cliente1": {"nome": "Ana", "idade": 25},
    "cliente2": {"nome": "Carlos", "idade": 30}
}

# Salvar em JSON
with open("clientes.json", "w") as arquivo:
    json.dump(clientes, arquivo)

# Ler JSON
with open("clientes.json", "r") as arquivo:
    dados = json.load(arquivo)
    print(dados)
