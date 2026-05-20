def caixa_eletronico(): 
    cedulas = [100, 50, 20, 10, 5, 2] 
 
    try: 
        valor = int(input("Digite o valor do saque: ")) 
 
        if valor <= 0: 
            print("Erro: O valor deve ser positivo.")
        elif valor % 2 != 0: 
            print("Erro: O valor deve ser múltiplo de 2.")
        else: 
            print("Cédulas entregues:")
            ''' O operador // é usado para obter a parte inteira da divisão, ou seja, quantas vezes a cedula cabe no valor restante.
            O operador % é usado para obter o resto da divisão, ou seja, o valor que ainda precisa ser sacado após entregar as cedulas.
            O loop percorre a lista de cedulas, calcula quantas cedulas de cada valor são necessárias e atualiza o valor restante até que o saque seja completo.'''
            for cedula in cedulas: 
                quantidade = valor // cedula
                if quantidade > 0:
                    print(f"{quantidade} cédulas de R$ {cedula}")
                    valor = valor % cedula 
 
    except ValueError: 
        print("Erro: Digite um valor numérico válido.") 
 
caixa_eletronico()