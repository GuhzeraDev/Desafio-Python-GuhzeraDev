'''
Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''

num1 = int(input('Insira um numero: '))

dobro = num1 * 2
triplo = num1 * 3
raiz = num1 ** 0.5

print('Seu numero é o {} o seu dobro é {} o triplo {} e sua raiz é {:.2f}'.format(num1,dobro,triplo,raiz))