
valorCasa = int(input('Digite o valor da casa: '))
salario = int(input('Informe seu salario: '))
quantoAnos = int(input('Informe quantos anos deseja fazer as parcela: '))

porcentagem = (salario / 100) * 30
quantoAnos *= 12
valor = valorCasa / quantoAnos 

print ('Para pagar um casa no valor %d as parcela vai ficar %.2f' %(valorCasa, valor))

if valor > porcentagem:
	print ('Empretimo negado')
else:
	print ('Empretimo aprovado')