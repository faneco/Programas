arq = open('alice.txt')
texto = arq.read() #ler o arquivo
texto = texto.lower() # deixa tudo minusculo
import string
for c in string.punctuation:
    texto = texto.replace(c, ' ') # tira os caracter
texto = texto.split() # ['a', 'b']

dic = {}
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1
print ('Alice aparece %s vezes' %dic['alice'])
arq.close()