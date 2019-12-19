import main
def calcular(valor1, valor2, operador):
    valor1 = valor1
    valor2 = valor2
    operador = operador

    if (operador == "+"):
        return valor1 + valor2
    elif (operador == "-"):
       return  valor1 - valor2
    elif (operador == "x"):
       return valor1 * valor2
    elif (operador == "÷"):
        return valor1 // valor2
    else:
        return "opa! Preciso de um operador"

def validadorDeValores (valor):
    valor = valor
    if (valor != int or valor != float):
        return "Opa só aceitamos números"
    else:
        return valor

def deNovo():
   calculoDeNovo = input("Você gostaria de continuar calculando? \n ""S"" para SIM ""N"" para Não ")

   if calculoDeNovo.upper() == 'S':
       valor1, valor2, operador = main.entradas()
       calcular(valor1, valor2, operador)
   elif calculoDeNovo.upper() == 'N':
       print('Tudo bem até a proxima!')
   else:
       deNovo()