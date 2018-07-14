nome = raw_input('Digite o nick: ')
senha = raw_input('Digite a senha: ')
while nome == senha:
	print ('senha nao pode ser igual nome')
	senha = raw_input('Digite a senha: ')