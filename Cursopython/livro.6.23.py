l = [15, 7, 27, 39]

p = int(input('Digite o valor a procurar: '))
v = int(input('Digite o valor da procurar: '))
achou = False
acho = False
x = 0
y = 0


while x < len(l):
	if l[x] == p:
		achou = True
		break
	x += 1

while y < len(l):
	if l[y] == v:
		acho = True
		break
	y += 1

if x < y:
	print ('X Foi achado primeiro ')
else:
	print ('y Foi achado primeiro ')

if achou:
	print ('%d achado na posição %d' %(p, x))
else:
	print ('%d não achado' %(p))

if acho:
	print ('%d achado na posição %d' %(v, y))
else:
	print ('%d não achado' %(v))
