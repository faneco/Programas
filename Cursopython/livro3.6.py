media = float(0.0)
for i in range(1, 3+1):
	notas = float(input('Digite %d nota: ' %(i)))
	media += notas
media /= 3
if media > 70:
	print ('Aluno Aprovado media %.2f' %(media))
else:
	print ('Aluno reprovado media %.2f' %(media))