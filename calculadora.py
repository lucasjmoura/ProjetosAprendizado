#Biblioteca de parâmetros e funções específicos do sistema
import sys

#classe calculadora, com todas as funções pertinentes a mesma
class calculadora():
    
    #Apresentação do programa e suas funções
	def apresentacao():
		print("Este programa desenpenha a função de uma calculadora simples com quatro operacões: Multiplicação, Divisão, Adição e Divisão. \nVamos nessa? \n(""S"" para SIM ""N"" para Não)")
		calculadora.deNovo()
		
	#função para gerenciar modulo
	def main():
		print ("Digite o primeiro valor ")
		valor1 = calculadora.validarValor()
		
		
		print ("Digite o segundo valor ")
		valor2 = calculadora.validarValor()
		
		print ("Escolha um dos operador: \nMulitplicação = * \nSoma = + \nSubtração = - \nDivisão = /")
		operador = calculadora.validarOperador()
		
		calculadora.calcular(valor1,valor2,operador)
		
		print ("Você gostaria de continuar calculando? \n ""S"" para SIM ""N"" para Não")
		calculadora.deNovo()
    
    #função calcular para realizar os calculos dos valores escolhidos pelo usuario e sua operação
	def calcular(valor1, valor2, operador):
	    valor1 = valor1
	    valor2 = valor2
	    operador = operador
	    
	    if (operador == "+"):
	    	resultado = valor1 + valor2
	    	return print (valor1," + ", valor2," = ",resultado)
	    	#return calculadora.deNovo()
	    elif (operador == "-"):
	    	resultado = valor1- valor2
	    	return print (valor1," - ",valor2," = ",resultado)
	    	#return calculadora.deNovo()
	    elif (operador == "*"):
	    	resultado = valor1 * valor2
	    	return print (valor1," * ",valor2," = ",resultado)
	    	#return calculadora.deNovo()
	    else:
	  	  resultado = valor1 // valor2
	  	  return print (valor1," / ",valor2," = ",resultado)
	  	  #return calculadora.deNovo()
	
    #função que recebe os valores e os valida
	def validarValor():
		try:
			valor = input("")
			return float(valor)
		except ValueError:
			print ("ops acho só aceitamos numeros, tente novamente")
			return calculadora.validarValor()		
	
    #função que recebe os operadores e os valida
	def validarOperador():
		operadores = ["*","-","÷","/"]
		try:
			operador = input ("")
			operadores.index(operador)
			return operador
		except ValueError:
			print ("Ops acho que você digitou errado, tente novamente")
			return calculadora.validarOperador()
			
    #funação de controle para o usuario sair do programa ou continuar calculando
	def deNovo():
	   calculoDeNovo = input("")
	   if calculoDeNovo.upper() == 'S':
	   	print("Então vamos lá")
	   	return calculadora.main()
	   elif calculoDeNovo.upper() == 'N':
	      print('Tudo bem até a proxima!')
	      return sys.exit()
	   else:
	   	print("Opa só aceitamos ""N"" ou ""S""")
	   	return  calculadora.deNovo()
    
 
 
if (__name__ == '__main__'):
	calculadora.apresentacao()
	calculadora.main()