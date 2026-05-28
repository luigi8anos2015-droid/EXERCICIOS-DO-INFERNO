import random
import os


def mostrar_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bem-vindo ao dado RPG!, escolha umas dessas opções para rolar o dado:")
    print("[1] -- Rolar um dado de 20 lados (d20)"
          "\n[2] -- Rolar um dado de 6 lados (d6)"
          "\n[3] -- Rolar um dado de 8 lados (d8)")


def voltar_menu():
    input("Pressione Enter para voltar ao menu...")


def pedir_quantidade():
    while True:
        try:
            qtd = int(input("Quantos dados quer rolar? "))
            if qtd > 0:
                return qtd
            
        except ValueError:
            print("Digite um número válido.")


def rolar_dados(lados, quantidade):
    resultados = [random.randint(1, lados) for _ in range(quantidade)]
    print(f"Resultados: {resultados}")
    if quantidade > 1:
        print(f"Total: {sum(resultados)}")
    return resultados


def dado_rpg():
    escolha = input("Escolha uma opção: ")
    if escolha == '1':
        qtd = pedir_quantidade()
        resultados = rolar_dados(20, qtd)
        if qtd == 1:
            if resultados[0] == 20:
                print("Crítico! Você acertou em cheio!")
            elif resultados[0] == 1:
                print("Falha crítica! Você errou miseravelmente!")
    elif escolha == '2':
        qtd = pedir_quantidade()
        rolar_dados(6, qtd)
    elif escolha == '3':
        qtd = pedir_quantidade()
        rolar_dados(8, qtd)
    else:
        print("Opção inválida!")
    voltar_menu()


while True:
    mostrar_menu()
    dado_rpg()
