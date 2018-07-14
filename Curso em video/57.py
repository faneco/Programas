sexo = input('Informe seu sexo [M/F]: ').upper()[0]
while sexo not in 'MF':
	sexo = input('Dados inválidos> Por favor, informe sexo:').upper()[0]
print ('Sexo %s registrado com sucesso' %(sexo))
