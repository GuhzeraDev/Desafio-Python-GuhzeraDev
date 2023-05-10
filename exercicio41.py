'''
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano d
e nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
'''


from datetime import date
nascimento = int(input('Digite o ano que você nasceu: '))
atual = date.today().year
idade = atual - nascimento

print('Você tem atualmente {} anos'.format(idade))

if idade <= 9:
    print('Você foi classificado como mirim')
elif idade <= 14:
    print('Você foi classificado como infantil')
elif idade <= 19:
    print('Você foi classificado como junior')
elif idade <= 25:
    print('Você foi classificado como sênior')
else:
    print('Você foi classificado como master')