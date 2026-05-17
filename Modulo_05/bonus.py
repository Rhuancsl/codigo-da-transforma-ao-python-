print("Bem-vindo ao sistema de cálculo de notas do aluno!")
print("faça o login para acessar o sistema.")

# Credenciais válidas
usuario_correto = "admin"
senha_correta = "1234"

# Validação de login
while True:
    print("digite o seu nome de usuario:")
    nome = input()
    print("digite a sua senha:")
    senha = input()
    
    if nome == usuario_correto and senha == senha_correta:
        print(f"Bem-vindo, {nome}! Você fez login com sucesso.")
        break
    else:
        print("Usuário ou senha inválidos. Tente novamente.\n")

#aplicativo para solicitar e calcular notas do aluno e para aprova-lo ou reprova-lo#

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media
def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = calcular_media(nota1, nota2, nota3)
print(f"A média do aluno é: {media}")
situacao = verificar_situacao(media)
print(f"Situação do aluno: {situacao}")

