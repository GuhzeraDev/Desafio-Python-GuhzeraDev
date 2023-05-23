'''

Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8

'''

quantidade = int(input('Escolhe quantos numeros deseja ver na sequencia Fibonacci: '))
cont = 0
num0 = 0
num1 = 1
numero = 0

print('{} > {} > '.format(num0, num1), end='')
while cont != quantidade:
    cont += 1
    numero = num0 + num1
    print(numero, end=' > ')
    num0 = num1
    num1 = numero
print('Acabou')

