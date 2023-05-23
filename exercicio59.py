'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''

num1 = int(input('Escolhe o primeiro numero: '))
num2 = int(input('Escolha o segundo numero: '))
escolha = 0


while escolha != 5:
    escolha = int(input('''Escolha uma ação do menu:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    Ação nº: '''))

    if escolha == 1:
        print('A soma dos numeros {} e {} tem como resultado {}'.format(num1, num2, num1 + num2))
    elif escolha == 2:
        print('A multiplicação dos numeros {} e {} tem como resultado {}'.format(num1, num2, num1 * num2))
    elif escolha == 3:
        if num1 > num2:
            print('O maior dos numeros {} e {} é o {}'.format(num1, num2, num1))
        else:
            print('O maior dos numeros {} e {} é o {}'.format(num1, num2, num2))
    elif escolha == 4:
        num1 = int(input('Escolhe o novo primeiro numero: '))
        num2 = int(input('Escolha o novo segundo numero: '))
    else:
        print('Insira uma ação valida.')
    print('=-=' * 10)
print('Você saiu do programa')

