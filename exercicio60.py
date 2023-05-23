'''
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120
'''

'''

for n in range(1, pergunta):
    print(f, end=' X ')




from math import factorial

pergunta = int(input('Qual numero você quer saber o fatorial? '))
f = factorial(pergunta)

print('O factorial de {} é {}.'.format(pergunta, f))
'''

n = int(input('Qual numero você quer saber o fatorial? '))
f = 1
c = n

print('Calculando {}! = '.format(n), end='')

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print(f)



