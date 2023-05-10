'''
Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
'''


nome = str(input('Qual e o seu nome: ')).strip()

divide = nome.split()
print('Primeiro nome é: {} '.format(divide[0]))
print('Ultimo nome é:  {} '.format(divide[len(divide) - 1]))