class SaldoInsuficienteError(Exception):
    def __init__(self, mensagem="Saldo insuficiente para realizar o saque."):
        super().__init__(mensagem)

class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError()
        self.saldo -= valor
        return f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}"

# Exemplo de uso
conta = ContaBancaria(100)
try:
    print(conta.sacar(150))
except SaldoInsuficienteError as e:
    print(e)