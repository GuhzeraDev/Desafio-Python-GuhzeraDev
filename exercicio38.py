"""
Anunciado: Escreva um programa que leia dois numeros interiros e os compare mostrando
na tela uma mensagem dizendo:
O primeiro valor é maior
ou
O segundo valor é maior
ou
Não existe valor maior os dois numeros são iguais.
"""


num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 > num2:
    print('O primeiro numero é o maior')
elif num1 < num2:
    print('O segundo numero é o maior')
else:
    print('Nenhum é maior os dois são iguais')
