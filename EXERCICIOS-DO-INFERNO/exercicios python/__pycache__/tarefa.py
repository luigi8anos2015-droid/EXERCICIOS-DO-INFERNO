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
            tarefa = input("Digite a tarefa: ").strip()
            if tarefa:
                tarefas.append(tarefa)
                print("Tarefa adicionada com sucesso!")
            else:
                print("Erro: a tarefa não pode estar vazia.")

        elif escolha == '2':
            if tarefas:
                print("\nTarefas:")
                for numero, tarefa in enumerate(tarefas, 1):
                    print(f"{numero}. {tarefa}")
            else:
                print("Nenhuma tarefa cadastrada.")

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
            print("Saindo... Até mais!")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    gerenciador_tarefas()