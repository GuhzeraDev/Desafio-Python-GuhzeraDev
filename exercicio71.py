'''
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

'''

'''
print('Banco Teste')
valor = int(input('Digite o valor que quer sacar R$: '))
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
'''

cedula50 = 0
cedula20 = 0
cedula10 = 0
cedula1 = 0
print('-=-' * 15)
print('Bem vindo ao banco do Guh')
print('-=-' * 15)

valor = int(input('Quanto deseja sacar? '))
while True:
    cedula50 = valor // 50
    resto = valor % 50
    cedula20 = resto // 20
    resto = resto % 20
    cedula10 = resto // 10
    resto = resto % 10
    cedula1 = resto // 1
    break

print(f'Para sacar o valor de {valor} foram ultilizadas: ')
if cedula50 > 0:
    print(f'{cedula50} notas de R$50')
if cedula20 > 0:
    print(f'{cedula20} notas de R$20')
if cedula10 > 0:
    print(f'{cedula10} notas de R$10')
if cedula1 > 0:
    print(f'{cedula1} notas de R$1')
print('Volte sempre ao Banco do Guh! Tenha um otimo dia!')

