import random
import math

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)  # número aleatório entre 1 e 100
    tentativas = 0
    acertou = False

    print("🎲 Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while not acertou:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas.")
            acertou = True
        else:
            # diferença absoluta usando math
            diferenca = math.fabs(numero_secreto - palpite)
            if palpite < numero_secreto:
                print(f"O número é maior! Diferença: {diferenca}")
            else:
                print(f"O número é menor! Diferença: {diferenca}")

# Executa o jogo
jogo_adivinhacao()
