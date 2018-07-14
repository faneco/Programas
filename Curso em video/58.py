from random import randint

x = 0

numero = randint(0, 10)
Acertou = False
while not Acertou:
	tentativa = int(input('Qual é o seu palpite: '))
	x +=1
	if numero == tentativa:
		Acertou = True
	if numero > tentativa:
		print ('mais... tente mais um vez')
	else:
		print ('menos... tente mais um vez')
	
print ('Acertou com %d tentativas. Parabéns!' %(x))