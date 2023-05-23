'''
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date

menor = 0
maior = 0
anoAtual = date.today().year

for c in range(1, 8):
    nascimento = int(input('Pessoa {} digite o ano que você nasceu: '.format(c)))
    idade = anoAtual - nascimento
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('São menores de 21 anos {} pessoas e {} pessoas são maiores que 21 anos'.format(menor, maior))
