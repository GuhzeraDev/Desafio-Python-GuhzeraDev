'''
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo
 de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
'''


num1 = int(input('Digite a medida da primeira reta: '))
num2 = int(input('Digite a medida da segunda reta: '))
num3 = int(input('Digite a medida da terceira reta: '))

print('Pode sim fazer um triangulo que será ', end='')

if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    if num1 == num2 == num3:
        print('equilatero')
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print('isósceles')
    else:
        print('escaleno')
else:
    print('Não pode fazer um triangulo')

"""if (num2 - num3) < num1 < num2 + num3:
    if (num1 - num3) < num2 < num1 + num3:
        if (num1 - num2) < num3 < num1 + num2:
            print('Pode sim fazer um triangulo')
        else:print('Não pode ser um triangulo')
    else:print('Não pode ser um triangulo')
else:print('Não pode ser um triangulo')"""
