from random import randint

def parar_programa ():
	if vidas == 0:
		print("\n========================================")
		print("\033[1;37;41m Vidas = {} \033[m                \033[1;30;46m Acertos = {} \033[m".format(vidas, acertos))
		print("\n             \033[1;33;40mVocê perdeu!\033[m\n")
		print("\nVocê chegou no nível {}\nObrigado por ter jogado {}!\n".format(nivel - 1,nome))
		exit()
def operadores1235 ():
	print("\n========================================")
	print("\033[1;37;41m Vidas = {} \033[m                \033[1;30;46m Acertos = {} \033[m".format(vidas, acertos))
	print("\n               \033[1;33;40mNivel  {}\033[m\n".format(nivel))
	print("{} {} [] = {}\n".format(numero2,operador,resultado))
def operadores46 ():
	print("\n========================================")
	print("\033[1;37;41m Vidas = {} \033[m                \033[1;30;46m Acertos = {} \033[m".format(vidas, acertos))
	print("\n               \033[1;33;40mNivel  {}\033[m\n".format(nivel))
	print("{} {} [] = {}\n".format(resultado,operador,numero2))

print("""\033[0;33;40m========================================\n\033[m
\033[1;31;40mSeja bem vindo ao jogo dos cálculos!\n
O jogo é bem símples, basta você digitar
os números logo após aparecer o cálculo
de forma que as contas fiquem corretas\033[m\n
\033[0;33;40m========================================\n\033[m""")
nome = input("Digite seu nome para iniciar: ")
print("\n\033[0;33;40m========================================\033[m\n")

print("""Qual operação você deseja fazer?
  [ 1 ] Soma
  [ 2 ] Subtração
  [ 3 ] Multiplicação
  [ 4 ] Divisão
  [ 5 ] Potenciação
  [ 6 ] Radiciação
  [ 7 ] Aleatório""")
modo_de_jogo = int(input("Digite o numero da operação: "))
print("\n\033[0;33;40m========================================\033[m\n")
print("""Qual será a dificuldade do jogo?
  [ 1 ] Fácil (1 vida)
  [ 2 ] Fácil (3 vidas)
  [ 3 ] Médio (1 vida)
  [ 4 ] Medio (3 vidas)
  [ 5 ] Difício (1 vida)
  [ 6 ] Difício (3 vidas)""")
dificuldade = int(input("Digite o número da dificuldade: "))

if dificuldade == 2 or dificuldade == 4 or dificuldade == 6:
	vidas = 3
else:
	vidas = 1
acertos = 0
resposta = 0
nivel = 1
while vidas != 0:
	if dificuldade == 1 or dificuldade == 2:
		numero1 = randint(1,10)
		numero2 = randint(1,10)
	elif dificuldade == 3 or dificuldade == 4:
		numero1 = randint(1,100)
		numero2 = randint(1,100)
	elif dificuldade == 5 or dificuldade == 6:
		numero1 = randint(1,1000)
		numero2 = randint(1,1000)
	else:
		exit ()
	if modo_de_jogo == 7:
		sorteio_operador = randint(1,4)
	else:
		sorteio_operador = modo_de_jogo
	if sorteio_operador == 1:
		operador = "+"
		resultado = numero1 + numero2
		operadores1235 ()
	elif sorteio_operador == 2:
		operador = "-"
		resultado = numero2 - numero1
		operadores1235 ()
	elif sorteio_operador == 3:
		operador = "*"
		resultado = numero1 * numero2
		operadores1235 ()
	elif sorteio_operador == 4:
		operador = "/"
		resultado = numero1 * numero2
		operadores46 ()
	elif sorteio_operador == 5:
		operador = "^"
		resultado = numero2 ** numero1
		operadores1235 ()
	elif sorteio_operador == 6:
		operador = "√"
		resultado = numero1
		numero1 = numero2 ** resultado
		operadores46 ()
	else:
		exit()
	resposta = int(input(""))
	if resposta == numero1:
		print("parabéns você passou do nivel {}\n".format(nivel))
		acertos = acertos + 1
	else:
		print("Você errou, a resposta era {}\n".format(numero1))
		vidas = vidas - 1
	enter = input("Aperte enter para continuar")
	nivel = nivel + 1
parar_programa ()