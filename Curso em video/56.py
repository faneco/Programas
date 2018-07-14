listaIdade = []
listaNome = []

media = 0
mulher = 0


for i in range(1, 5):
	print ('%d - PESSOA' %(i))
	nome = input('Nome: ')
	idade = float(input('Idade: '))
	sexo = input('Sexo M/F: ').lower().strip()
	media += idade
	if sexo == 'm':
		listaNome.append(nome)
		listaIdade.append(idade)
	if idade <= 20 and sexo == 'f':
		mulher += 1

maior = 0
posição = 0
for e, x in enumerate(listaIdade):
	if x > maior and sexo == 'm':
		maior = x
		posição = e



print ('Media de idade do grupo é de %.2f anos' %(media / 4))	
print ('Tem %d mulher menor que 20 anos' %(mulher))
print ('A idade do maior homem %d o seu nome %s' 
	%(maior, listaNome[posição]))