num = input('Digite a velocidade: ')
if num > 110:
	valor =  (num -110) * 5
	print ('vc foi multado: R$ %.2d' %valor)
else:
	print ('vc esta no limite')