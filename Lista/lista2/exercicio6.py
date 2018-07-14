horas = input('Digite horas trabalhada: ')
valor = input ('Digite valor das horas: ')

salario = valor * horas
ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
liquido = salario - (ir + inss + sindicato)

print ('Salrio R$ %.2f' %salario) 
print ('desconto IR: R$ %.2f' %ir)
print ('INSS R$: %.2f' %inss)
print ('sindicato %.2f' %sindicato)
print ('Liquido %.2f' %liquido)
