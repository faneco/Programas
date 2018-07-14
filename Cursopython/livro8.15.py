l = [1, [2, 3, 4,[5, 6, 7]]]

for i in l:
	if type(i) == int:
		print (i)
	else:
		print ('lista1')
		for y in i:
			if type(y) == int:
				print (y)
			else:
				print ('lista2')
				for z in y:
					print (z)