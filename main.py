import calculadora

def entradas ():
    valor1 = input("Digite o primeiro valor ")
    valor1 = calculadora.validadorDeValores (valor1)

    valor2 = input("Digite o segundo valor ")
    valor2 = calculadora.validadorDeValores (valor2)

    operador = input("Digite o operador (x,+,-,÷)")

    return valor1 , valor2, operador

valor1, valor2, operador = entradas()
calculadora.calcular(valor1,valor2,operador)



   