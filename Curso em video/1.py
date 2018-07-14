nome = input('Digite o nome: ').strip()

print (nome.lower())
print (nome.upper())

d = nome.replace(' ', '')
print ('total de letra %s' %(len(d)))

primeiro = (nome.split())
print ('Primeiro nome tem %s letra'%(len(primeiro[0])))