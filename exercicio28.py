'''
Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''


from random import randint
from time import sleep

num = randint(0, 5)
print('-=-' * 20)
print('Irei pensar em um numero aleatoriamente entre 0 e 5 ')
print('-=-' * 20)
pergunta = int(input('Tente adivinhar o numero gerado: '))
print('-=-' * 20)
print('Processando...........')
print('-=-' * 20)
sleep(3)
print('Parabens você acertou o numero escolhido foi {} '.format(num) if pergunta == num else
      'Você errou o numero escolhido foi {}'.format(num))
print('-=-' * 20)