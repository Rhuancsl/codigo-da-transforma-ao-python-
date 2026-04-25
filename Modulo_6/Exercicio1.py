# Criar e escrever em um arquivo .txt
with open("dados.txt", "w") as arquivo:
    arquivo.write("Nome: Rhuan\nIdade: 17\nCurso: Programação")

# Ler o arquivo .txt
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
