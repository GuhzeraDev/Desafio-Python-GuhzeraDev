'''
Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

num = int(input('Escoha um numero: '))
cont = 0
for c in range(1, num + 1, +1):
    if num % c == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, cont))
if cont == 2 :
    print('E por isso È primo ')
else:
    print('E por isso NÂO È PRIMO')
