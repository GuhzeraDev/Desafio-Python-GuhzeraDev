'''
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
'''

from random import randint
n = 0
cont = 0
escolha = 'P'

print('=-='*10)
print('Vamos jogar par ou impar')
print('=-='*10)
while True:
    n = int(input('Diga um valor: '))
    escolha = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    ale = randint(0, 10)
    soma = n + ale
    print(f'Você colocou {n} e eu coloquei {ale} dando {soma} que é ', end='')
    print('Deu par' if soma % 2 == 0 else 'Deu Impar')
    if soma % 2 == 0:
        if escolha == 'P':
            print('Você venceu vamos mais uma vez.')
        else:
            print('Eu ganhei!!')
            break
    else:
        if escolha == 'I':
            print('Você venceu vamos mais uma vez.')
        else:
            print('Eu ganhei!!')
            break
    cont += 1
print(f'Você ganhou {cont} vezes antes de perder!!')



