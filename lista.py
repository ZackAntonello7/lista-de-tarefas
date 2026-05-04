tarefas = []

while True:
    print("\n=== LISTA DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")

    elif opcao == "2":
        print("\nTarefas:")
        for i, tarefa in enumerate(tarefas):
            print(i, "-", tarefa)

    elif opcao == "3":
        numero = int(input("Digite o número da tarefa para remover: "))
        if numero < len(tarefas):
            tarefas.pop(numero)
            print("Tarefa removida!")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")