'''faca um programa que simule um lançamento de dados. 
lance o dado 100 vezes e armazene os resulado em um vetor. 
Depois, mostre quantas vezes cada valor foi conseguido.'''

import random

lista = []

for i in range (100):
	lista.append(random.randint(1, 6))

for i in range(1, 7):
	print ('a face %d aparece %d vezes' %(i, lista.count(i)))

