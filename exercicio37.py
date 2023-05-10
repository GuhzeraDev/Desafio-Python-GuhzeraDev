"""
Anunciado: Escreva um programa que leia um numero inteiro qualquer e converta na opão escolhida por ele
sendo binario,octal ou hexadecimal.
"""


num = int(input('Digite um numero: '))
escolha = int(input('''Escolha a opção de conversão 
1-Binario 
2-Octa 
3-Hexadecimal
: '''))

if escolha == 1:
    print('Seu numero convertido em Binario é: {}'.format(bin(num)[2:]))
elif escolha == 2:
    print('Seu numero convertido em Octa é: {}'.format(oct(num)[2:]))
elif escolha == 3:
    print('Seu numero convertido em Hexadecimal é: {}'.format(hex(num)[2:]))
else:
    print('Numero digitado invalido')
