def validar_idade():
    try:
        idade = int(input("Digite sua idade: "))
        if idade <= 0:
            raise ValueError("A idade deve ser um número positivo.")
        print(f"Idade válida: {idade}")
    except ValueError as e:
        print(f"Erro: {e}")

# Exemplo de uso
validar_idade()
