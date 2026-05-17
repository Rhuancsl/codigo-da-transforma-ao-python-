def calculadora(a, b, operacao):
    try:
        if operacao == "divisao":
            return a / b
        elif operacao == "soma":
            return a + b
        elif operacao == "subtracao":
            return a - b
        elif operacao == "multiplicacao":
            return a * b
        else:
            return "Operação inválida"
    except ZeroDivisionError:
        return "Erro: divisão por zero não é permitida."

# Exemplo de uso
print(calculadora(10, 0, "divisao"))
print(calculadora(10, 5, "soma"))
print(calculadora(10, 5, "subtracao"))
print(calculadora(10, 5, "multiplicacao"))