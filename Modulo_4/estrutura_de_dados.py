print("Bem-vindo, usuário! Essa plataforma funciona para agendamento de tarefas.")
print("Aqui estão as opções disponíveis:")
print("1. criar tarefa")
print("2. visualizar tarefas agendadas")
print("3. organizar tarefas de forma alfabetica")
print("4. sair")

print("opcao disponiveis: 1, 2, 3, 4")

tarefa = ""
opcao = int(input("digite a opção desejada: "))

if opcao == 1:
    tarefa = input("digite a tarefa que deseja agendar:")
    print("tarefa agendada com sucesso!")
    print("tarefa criada foi:", tarefa)

elif opcao == 2:
    print("visualizar tarefas agendadas:")
    print("tarefa agendada:", tarefa)

elif opcao == 3:
    print("organizar tarefas de forma alfabetica:")
    tarefa_ordenada = sorted([tarefa])
    print(tarefa_ordenada)

elif opcao == 4:
    print("opcao 4")
    print("saindo do programa. até logo!")