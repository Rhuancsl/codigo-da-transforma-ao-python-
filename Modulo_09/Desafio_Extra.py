def sistema_login():
    usuario_correto = "admin"
    senha_correta = "1234"
    tentativas = 3

    while tentativas > 0:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == usuario_correto and senha == senha_correta:
            print("Login realizado com sucesso!")
            return True
        else:
            tentativas -= 1
            print(f"Credenciais inválidas. Tentativas restantes: {tentativas}")

    print("Acesso bloqueado. Número de tentativas excedido.")
    return False

# Exemplo de uso
sistema_login()
