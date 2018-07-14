num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro:"))

if num1 > num2:
    maior = num1
else:
    maior = num2
while True:
    if maior % num1 == 0 and maior % num2 == 0:
        print(maior)
        break
    else:
        maior += 1

'''
Vamos determinar o MMC entre os números 12, 18 e 24

12 = (12, 24, 36, 48, 60, 72, 84, 96, ...)
18 = (18, 36, 54, 72, 90, 108, ...)
24 = (24, 48, 72, 96, 120, 144, ...)
'''