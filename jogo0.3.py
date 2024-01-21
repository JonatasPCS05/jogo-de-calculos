from random import randint

def parar_programa ():
	if vidas == 0:
		print("\nVidas = 0, você perdeu!\nVocê teve {} acertos".format(acertos))
		exit()
def operadores123 ():
	print("\n========================================")
	print("\033[1;37;41m Vidas = {} \033[m                \033[1;30;46m Acertos = {} \033[m".format(vidas, acertos))
	print("                 \033[1;33;40mNivel {}\033[m\n".format(nivel))
	print("{} {} [] = {}\n".format(n2,operador,res))
def operadores4 ():
	print("\n========================================")
	print("\033[1;37;41m Vidas = {} \033[m                \033[1;30;46m Acertos = {} \033[m".format(vidas, acertos))
	print("                 \033[1;33;40mNivel {}\033[m\n".format(nivel))
	print("{} {} [] = {}\n".format(res,operador,n2))

print("""\033[0;33;40m========================================\n\033[m
\033[1;31;40mSeja bem vindo ao jogo dos cálculos!\n
O jogo é bem símples, basta você digitar
os números logo após aparecer o cálculo
para que as contas fiquem corretas\033[m\n
\033[0;33;40m========================================\n\033[m""")
nome = input("Digite seu nome para iniciar: ")

print("""Qual operação você deseja fazer?
  [ 1 ] Soma
  [ 2 ] Subtração
  [ 3 ] Multiplicação
  [ 4 ] Divisão
  [ 5 ] Aleatório""")
modo_de_jogo = int(input("Digite o numero da operação: "))

vidas = 1
acertos = 0
resposta = 0
nivel = 1
while vidas != 0:
	n1 = randint(1,10)
	n2 = randint(1,10)
	if modo_de_jogo == 5:
		sorteio_operador = randint(1,4)
	else:
		sorteio_operador = modo_de_jogo
	if sorteio_operador == 1:
		operador = "+"
		res = n1 + n2
		operadores123 ()
	elif sorteio_operador == 2:
		operador = "-"
		res = n2 - n1
		operadores123 ()
	elif sorteio_operador == 3:
		operador = "*"
		res = n1 * n2
		operadores123 ()
	elif sorteio_operador == 4:
		operador = "/"
		res = n1 * n2
		operadores4 ()
	else:
		exit()
	resposta = int(input(""))
	if resposta == n1:
		print("parabéns você passou do nivel {}\n".format(nivel))
		acertos = acertos + 1
	else:
		print("Você errou\n")
		vidas = vidas - 1
	enter = input("Aperte enter para continuar")
	nivel = nivel + 1
parar_programa ()