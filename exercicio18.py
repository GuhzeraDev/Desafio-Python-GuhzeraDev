'''
Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.
'''

import math
num1 = int(input('Informe um numero: '))
numc = math.radians(num1)

seno = math.sin(numc)
cosseno = math.cos(numc)
tangente = math.tan(numc)

print('O seno do seu numero é {:.2f} o cosseno é: {:.2f} e a tangente é: {:.2f} '.format(seno,cosseno,tangente))