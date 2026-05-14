from funcoes import calculadora_gorjeta, calcular_total_com_gorjeta

valor = float(input("Digite o valor da conta: "))
porcentagem = float(input("Digite a porcentagem de gorjeta: "))

gorjeta = calculadora_gorjeta(valor, porcentagem)
total = calcular_total_com_gorjeta(valor, porcentagem)
print(f"A gorjeta é de: {gorjeta:.2f}")
print(f"O total a pagar é de: {total:.2f}")