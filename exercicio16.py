'''
Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e
mostre na tela a sua porção Inteira.
'''

import math
#from math import trunc
num1 = float(input('Escreva um numero : '))

print('A porção inteira do seu numero é: {} '.format(math.trunc(num1)))
