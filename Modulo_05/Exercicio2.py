# Exercício 2: Função para calcular média e verificar aprovação
def calcular_media(notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        print(f"Média: {media:.2f} - Aluno aprovado!")
    else:
        print(f"Média: {media:.2f} - Aluno reprovado!")

# Teste
calcular_media([8, 7, 6])  # média 7.0 → aprovado
calcular_media([5, 6, 4])  # média 5.0 → reprovado
