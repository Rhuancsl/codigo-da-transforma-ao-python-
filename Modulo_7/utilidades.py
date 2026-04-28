print("calculadora simples")

while True:
    print("digite o primeiro numero:")
    numero = input()
    print("digite o segundo numero:")
    numero2 = input()
    print("digite a operaçao +, -, *, /:")
    operaçao = input()
    print("operaçao desejada foi:", operaçao)

    if operaçao == "+":
        resultado = float(numero) + float(numero2)
        print("o resultado da soma é:", resultado)

    elif operaçao == "-":
        resultado = float(numero) - float(numero2)
        print("o resultado da subtraçao é:", resultado)

    elif operaçao == "*":
        resultado = float(numero) * float(numero2)
        print("o resultado da multiplicaçao é:", resultado)

    elif operaçao == "/":
        resultado = float(numero) / float(numero2)
        print("o resultado da divisao é:", resultado)

    else:
        print("operação inválida. Por favor, escolha uma opção válida.")

    print("opçoes disponiveis:")
    print("1 - recomeçar a calculadora")
    print("2 - sair da calculadora")
    escolha = input("digite sua escolha: ")

    if escolha == "1":
        print("recomeçando a calculadora...\n")
        continue
    elif escolha == "2":
        print("saindo da calculadora...")
        break
    else:
        print("opção inválida. Por favor, escolha uma opção válida.")