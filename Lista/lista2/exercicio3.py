n = input('Informe quantidade de quilos: ')

if n > 50:
	total = (n - 50) * 4
	excesso = (n - 50)

else: 
	total = excesso = 0
print ('excesso %d quilos permido' %excesso)
print ('total de multa R$ %.2f' %total)