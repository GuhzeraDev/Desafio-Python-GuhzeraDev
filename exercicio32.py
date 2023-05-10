'''
Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''

from datetime import date
ano = int(input('Qual e o ano escolhido? Caso queira analisar o ano atual escreva 0 :  '))
if ano == 0:
    ano = date.today().year
print('O ano {} é bissexto'.format(ano) if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
else print('O ano {} não é bissexto'.format(ano)))
