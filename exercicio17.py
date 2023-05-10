'''
Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''

#import math
from math import hypot
cat1 = float(input('Informe o cateto oposto: '))
cat2 = float(input('Informe o cateto adjacente: '))
hyp = hypot(cat1, cat2)
'''print('A hipotenusa deste triangulo retangulo é: {:.2f}'.format(math.sqrt(cat1*cat1 + cat2*cat2)))'''

print('A hipotenusa deste triangulo retangulo é: {:.2f}'.format(hyp))
