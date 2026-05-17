# Exercício 3: Função para retornar maior e menor número
def maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor

# Teste
numeros = [10, 3, 25, -4, 7]
resultado = maior_menor(numeros)
print(f"Maior: {resultado[0]}, Menor: {resultado[1]}")
