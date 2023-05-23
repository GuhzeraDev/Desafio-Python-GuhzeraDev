'''
Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos
de três e que se encontram no intervalo de 1 até 500
'''


num = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        num += c

print('A soma de todos os {} numeros impares e divisiveis por 3 de 0 a 500 é {}'.format(cont, num))