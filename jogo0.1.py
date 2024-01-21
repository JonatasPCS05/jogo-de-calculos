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

vidas = 3
acertos = 0
resposta1 = 0
while resposta1 != 3 and vidas != 0:
	print("\n========================================\n")
	print("                 Nivel 1\n")
	print("[] + 7 = 10\n")
	resposta1= int(input(""))
	if resposta1 == 3:
		print("parabéns você passou do nivel 1\n")
		enter = input("Aperte enter para continuar")
		acertos = 1
	else:
		print("Você errou\n")
		enter = input("Aperte enter para continuar")
		vidas = vidas - 1
parar_programa ()

resposta2 = 0
while resposta2 != 6 and vidas != 0:
	print("\n========================================\n")
	print("                 Nivel 2\n")
	print("[] x 8 = 48\n")
	resposta2 = int(input(""))
	if resposta2 == 6:
		print("parabéns você passou do nivel 2\n")
		enter = input("Aperte enter para continuar")
		acertos = 2
	else:
		print("Você errou\n")
		enter = input("Aperte enter para continuar")
		vidas = vidas - 1
parar_programa ()
print("Teste")