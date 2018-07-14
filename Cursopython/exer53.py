nome = input('Digite o nome: ').strip()
palavra = nome.split()
junto = ''.join(palavra)
inverso = ''
for i in range(len(junto)-1, -1, -1):
	inverso += junto[i]
print (junto, inverso)