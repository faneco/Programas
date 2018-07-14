'''escre uma expressão para determinar se uma pessoa deve ou não
pagar imposto . Considere que pagam imposto pessoas cujo salário é
maior que R%1200,00'''

salario = float(input('Digite o salario: '))

if salario > 1200:
	print ('voce tem que pagar imposto')
else:
	print ('voce nao precisa pagar imposto')