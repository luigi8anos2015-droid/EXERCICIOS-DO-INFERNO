import os
os.system('cls' if os.name == 'nt' else 'clear')

def gerenciador_tarefas():
    tarefas = []

    while True:
        print("\n1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            tarefa = input("Digite a tarefa: ").strip()
            if tarefa:
                tarefas.append(tarefa)
                print("Tarefa adicionada com sucesso!")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Erro: a tarefa não pode estar vazia.")

        elif escolha == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            if tarefas:
                print("Tarefas registradas:")
                for numero, tarefa in enumerate(tarefas, 1):
                    print(f"{numero}. {tarefa}")
            else:
                print("Nenhuma tarefa cadastrada.")
            input("\nPressione Enter para voltar ao menu...")
                

        elif escolha == '3':
            if not tarefas:
                print("Erro: nenhuma tarefa para remover.")
                continue
            try:
                indice = int(input("Digite o número da tarefa a remover: "))
                if 0 < indice <= len(tarefas):
                    tarefa_removida = tarefas.pop(indice - 1)
                    print(f"Tarefa '{tarefa_removida}' removida!")
                else:
                    print("Erro: número inválido.")
            except ValueError:
                print("Erro: digite um número válido.")

        elif escolha == '4':
            os.system('cls')
            print("Saindo... Até mais!")

            break

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida.")
            print("error, coloque algo valido,pressione qualuquer tecla para continuar...")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    gerenciador_tarefas()