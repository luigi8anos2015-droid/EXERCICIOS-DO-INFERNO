import random
 
def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
 
    while True:
        try:
            palpite = int(input("Tente adivinhar o número (1-100): "))
            tentativas += 1
            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"parabéns! voce acertou o numero {numero_secreto} em {tentativas} tentativas.")
                break
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro entre 1 e 100.")