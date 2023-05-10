'''
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date
nasc = int(input('Digite o ano que nasceu: '))
atual = date.today().year
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {} '.format(nasc, idade, atual))

if idade < 18:
    print('Você ainda ira se alistar no exercito daqui a {} anos'.format(18 - idade))
elif idade == 18:
    print('Está na hora de se alistar no exercito')
else:
    print('Você está atrasado há {} anos para se alistar no exercito'.format(idade - 18))

