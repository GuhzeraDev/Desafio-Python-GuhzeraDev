"""Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você."""

from random import randint
from time import sleep
pcescolha = randint(1,3)

perg = int(input('''Ola vamos jogar jokenpo??
                 Para jogarmos vamos adotar as seguintes opções: 
                 Digite 1 Para escolher Pedra 
                 Digite 2 Para escolher Papel 
                 Digite 3 Para escolher Tesoura 
                 Digite aqui a sua escolha: '''))
print('Pedraaaaa')
sleep(1)
print('Papeeeel')
sleep(1)
print('Tesoura')
sleep(1)

if perg == pcescolha:
    if perg == 1:
        print('Eu e você escolhemos pedra nimguem ganhou!!')
    elif perg == 2:
        print('Eu e você escolhemos papel nimguem ganhou!!')
    elif perg == 3:
        print('Eu e você escolhemos tesoura nimguem ganhou!!')
elif perg == 1:
    if pcescolha == 2:
        print('Eu escolhi papel e você escolheu pedra eu ganhei!!')
    else:
        print('Eu escolhi tesoura e você escolheu pedra você ganhou!!')
elif perg == 2:
    if pcescolha == 1:
        print('Eu escolhi pedra e você escolheu papel você ganhou!!')
    else:
        print('Eu escolhi tesoura e você escolheu papel eu ganhei!!')
elif perg == 3:
    if pcescolha == 1:
        print('Eu escolhi pedra e você escolheu tesoura eu ganhei!!')
    else:
        print('Eu escolhi papel e você escolheu tesoura você ganhou!!')
else:
    print('Digite um numero valido... você me fez cantar o pedra papel tesoura e digitou algo que não podia affs ')

