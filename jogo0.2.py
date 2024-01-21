from random import randint
print("========================================\n")
print("Seja bem vindo ao jogo dos cálculos!\n")
print("O jogo é bem símples, basta você digitar")
print("os números logo após aparecer o cálculo")
print("para que as contas fiquem corretas\n")
print("========================================\n")
nome = input("Digite seu nome para iniciar: ")

def parar_programa ():
	if vidas == 0:
		print("\nVidas = 0, você perdeu!\nVocê teve {} acertos".format(acertos))
		exit()

vidas = 1
acertos = 0
resposta = 0
nivel = 1
while vidas != 0:
	n1 = randint(1,10)
	n2 = randint(1,10)
	sorteio_operador = randint(1,3)
	if sorteio_operador == 1:
		operador = "+"
		res = n1 + n2
	if sorteio_operador == 2:
		operador = "-"
		res = n1 - n2
	if sorteio_operador == 3:
		operador = "*"
		res = n1 * n2
	print("\n========================================\n")
	print("                 Nivel {}\n".format(nivel))
	print("[] {} {} = {}\n".format(operador,n2,res))
	resposta = int(input(""))
	if resposta == n1:
		print("parabéns você passou do nivel {}\n".format(nivel))
		enter = input("Aperte enter para continuar")
		acertos = acertos + 1
	else:
		print("Você errou\n")
		enter = input("Aperte enter para continuar")
		vidas = vidas - 1
	nivel = nivel + 1
parar_programa ()