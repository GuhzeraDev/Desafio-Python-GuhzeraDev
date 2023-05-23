'''

Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

'''


total = 0
contador = 0
pergunta = int(input('Digite 999 para parar: '))

while pergunta != 999:
    contador += 1
    total += pergunta
    pergunta = int(input('Digite 999 para parar: '))
print('Você digitou {} numeros e a soma de todos os digitados foi {} '.format(contador, total))