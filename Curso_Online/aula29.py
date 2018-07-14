alunos = int(input('Informe quantidade de alunos: '))

medias = []

for i in range(1, alunos+1):
	notas = 0
	for j in range(1, 5):
		notas += float(input('Digite nota %d de 4 do aluno %d de %d: '
		 %(j, i, alunos)))
	notas /= 4
	medias.append(notas)
	

	

num = 0
for media in medias:
	if media >= 7:
		num += 1
print ('numero de alunos maior que 7 e %d' %(num))




