def calculadora_gorjeta(valor, porcentagem):
    gorjeta = valor * (porcentagem / 100)
    return gorjeta
def calcular_total_com_gorjeta(valor, porcentagem):
    gorjeta = calculadora_gorjeta(valor, porcentagem)
    total = valor + gorjeta
    return total