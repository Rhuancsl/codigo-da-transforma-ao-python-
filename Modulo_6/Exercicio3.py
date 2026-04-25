import csv

# Criar e salvar notas em CSV
with open("notas.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Aluno", "Nota1", "Nota2", "Nota3"])
    escritor.writerow(["Rhuan", 8, 7, 9])
    escritor.writerow(["Ana", 6, 5, 7])

# Ler CSV
with open("notas.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
