"""
Este módulo é uma projeto de aprendizado, no qual desenvolvemos uma calculadora basica com
quatro operações.

versão do projeto: 0.0.2

"""

#Biblioteca de parâmetros e funções específicos do sistema
import sys

# Função que recebe os valores e os converte para float e retorna para a proxima fase
def validar_valor(valor):
	valor = valor
	try:
		valor_convertido= float(valor)
		return valor_convertido
	except ValueError:
		return False

#valida o operador atraves de uma lista de funções recendo o operador e os valores para passar 
#como parametro
def valida_operador(c,a,b):
	operadores = {"+":adicao,"-":subtracao,"*":multiplicacao,"/":divisao}
	try:
		operadores[c](a,b)
	except KeyError:
		return False

'''
funções para efetuar os calculos juntamente com a função para finalizar ou continuar o programa
'''
def adicao(valor1, valor2):
	resultado = valor1 + valor2
	print (valor1," + ", valor2," = ",resultado)
	perguntar()
	

def subtracao(valor1, valor2):
	resultado = valor1 - valor2
	print (valor1," - ",valor2," = ",resultado)
	perguntar()
	 
def multiplicacao(valor1, valor2):
	resultado = valor1 * valor2
	print (valor1," * ",valor2," = ",resultado)
	perguntar()
	    
def divisao(valor1, valor2):
	try:
		resultado = valor1 / valor2
		print (valor1," / ",valor2," = ",resultado)
		perguntar()
	except ZeroDivisionError:
		print("ops nao dividimos por zero")
		perguntar()
		
#pergunta para o usuario se ele deseja iniciar o programa e valida sua resposta	
def calcular():
	x = True
	while x == True:
		calculoDeNovo = input("")
		if calculoDeNovo.upper() == 'S':
		   print("Então vamos lá")
		   x = False
		   validar_entradas()
		  # return main()
		elif calculoDeNovo.upper() == 'N':
			print('Tudo bem até a proxima!')
			return sys.exit()
		else:
		   print("Opa só aceitamos ""N"" ou ""S""")

#pergunta para o usuario se o mesmo quer finalizar o programa	   
def perguntar():
	print("Gostaria de calcular de novo?")
	calcular()

#função que valida as entradas
def validar_entradas():
	print("Para começarmoa digite os valores a ser calculado,\
    juntamente com o operador desejado como mostra o exemplo abaixo:\n ""45 + 89""")
    #while que valida os valores juntamente com o operador
	x = True
	while x == True:
		try:
			a,b,c=input("").split()
			x = False
		except ValueError:
			print("Ops, se atente ao espaço entre os valores e o operador")

    #chamada das funções que valida os valores e os retorna convertidos
	a = validar_valor(a)
	c = validar_valor (c)
	b = valida_operador(b,a,c)
	
    #laço que valida os valores individualmente caso, haja algum errado
	while a == False or b == False or c == False:
		if a == False:
			a=input("Ops acho que você digitou o primeiro valor errado ")
			a = validar_valor(a)
		elif c == False:
			c = input("Ops acho que você digitou o segundo valor errado ")
			c = validar_valor(c)
		elif b == False:
			b = input("Ops acho que você digitou o operador valor errado ")
			b = valida_operador(b,a,c)

#função main que faz a apresentação e chama a primeira função
def main():
    print("Olá, bem vindo a calcular, se trata de um\n projeto de aprendizado\
        onde desenvolvemos uma calculadora que realiza quatro operações básicas:\
        Multiplicação, Divisão, Adição e\ subtração.\nVamos nessa? \n(""S"" para SIM\
        ""N"" para Não)")
    #Função que os primeiros valores
    calcular()
				
if __name__ == '__main__':
    main()