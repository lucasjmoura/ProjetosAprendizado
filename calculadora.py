def calculadora(valor1, valor2, operador):
    valor1 = int(valor1)
    valor2 = int(valor2)
    operador = str(operador)

    if (operador == "+"):
        return valor1 + valor2
    else:
        if (operador == "-"):
            return  valor1 - valor2
        else:
            if (operador == "x"):
                return valor1 * valor2
            else:
                if (operador == "÷"):
                    return valor1 // valor2
                else:
                    return "error"
while True:
    print("\nDigite o primeiro valor")
    valor1 = int(input(""))

    print("Digite o segundo valor")
    valor2 = int(input(""))

    print("Digite o operador (x,+,-,÷)")
    ope = str(input(""))

    resultado = calculadora(valor1,valor2,ope)
    print("O resultado é ", resultado)