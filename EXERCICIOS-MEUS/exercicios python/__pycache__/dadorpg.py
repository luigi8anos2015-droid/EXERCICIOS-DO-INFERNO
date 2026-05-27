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


def dado_rpg():
    escolha = input("Escolha uma opção: ")
    if escolha == '1':
        d20 = random.randint(1, 20)
        print(f"Você rolou um {d20}!")
        if d20 == 20:
            print("Crítico! Você acertou em cheio!")
        elif d20 == 1:
            print("Falha crítica! Você errou miseravelmente!")
    elif escolha == '2':
        d6 = random.randint(1, 6)
        print(f"Você rolou um {d6} no dado de 6 lados!")
    elif escolha == '3':
        d8 = random.randint(1, 8)
        print(f"Você rolou um {d8} no dado de 8 lados!")
    else:
        print("Opção inválida!")
    voltar_menu()


while True:
    mostrar_menu()
    dado_rpg()
