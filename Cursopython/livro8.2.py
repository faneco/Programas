def multiplo(a, b):
	return (a % b == 0)

def true_ou_false(a, b):
	if multiplo(a, b):
		return 'True'
	else:
		return 'False'

print (true_ou_false(28, 14))