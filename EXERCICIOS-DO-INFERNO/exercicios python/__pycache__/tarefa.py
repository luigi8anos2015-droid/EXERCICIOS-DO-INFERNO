import os
os.system('cls' if os.name == 'nt' else 'clear')

def gerenciador_tarefas():
    tarefas = []
    while True:
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            tarefa= input("Digite a tarefa: ")
            tarefas.append(tarefa)
            if tarefa.append(tarefas):
                print("Tarefa adicionada com sucesso!")
            else:
                print("Erro, a tarefa nao pode estar vazia")
        elif escolha == '2':
            if tarefas:
                print("\ntarefas:")
                for i in enumerate(tarefas,1):
                    print(f"{i[0]}. {i[1]}")
                else:
                    print("Nenhuma tarefa cadastrada.")
        elif escolha == '3':
            if not tarefas:
                print("Error, nenhuma tarefa para remover")
                continue
            try:
                indice= int(input("Digite o número da tarefa a ser removida: "))
                if 0 < indice <= len(tarefas):
                    tarefa_removida = tarefas.pop(indice - 1)
                    print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
                else:
                    print("Erro: Número da tarefa inválido.")
            except ValueError:
                print("Erro: Por favor, digite um número válido.")
        elif escolha == '4':
            print("Saindo do gerenciador de tarefas. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
if __name__ == "__main__":
    gerenciador_tarefas()