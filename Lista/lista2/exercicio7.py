tamanho = input('Digite tamanho na area em (M2): ')
valor = 0
if tamanho % 18 != 0:
	valor = (tamanho  / 18) + 1
else: 
	valor = tamanho / 18

pagar = 80 * valor
print ('Quantidade de latas: %d' %valor)
print ('Valor a pagar R$ %.2f' %pagar)
