
'''
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

termo = int(input('Digite o primeiro termo para começar o PA: '))
razao = int(input('Digite a razão da sua PA: '))
cont = 1
numero = termo

while cont <= 10:

    print('{} '.format(numero), end='> ')
    numero = numero + razao
    cont += 1
print('Acabou')
