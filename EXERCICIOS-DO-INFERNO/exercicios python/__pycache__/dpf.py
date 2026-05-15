def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")

    if not cpf.isdigit():
        print("CPF deve conter apenas números.")
        return False

    if len(cpf) != 11:
        print("CPF deve conter 11 dígitos.")
        return False

    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    print(f"CPF válido: {cpf_formatado}")
    return True

cpf = input("Digite seu CPF: ")
validar_cpf(cpf)