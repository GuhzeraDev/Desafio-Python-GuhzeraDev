'''
Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e
diga ao usuário se elas podem ou não formar um triângulo.
'''


num1 = int(input('Digite a medida da primeira reta: '))
num2 = int(input('Digite a medida da segunda reta: '))
num3 = int(input('Digite a medida da terceira reta: '))

if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    print('Pode sim fazer um triangulo')
else:
    print('Não pode fazer um triangulo')

"""if (num2 - num3) < num1 < num2 + num3:
    if (num1 - num3) < num2 < num1 + num3:
        if (num1 - num2) < num3 < num1 + num2:
            print('Pode sim fazer um triangulo')
        else:print('Não pode ser um triangulo')
    else:print('Não pode ser um triangulo')
else:print('Não pode ser um triangulo')"""
