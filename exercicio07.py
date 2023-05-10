'''
Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre
 a sua média.
'''


num1 = float(input('Digite a nota 1: '))
num2 = float(input('Digite a nota 2: '))

media = (num1 + num2) / 2

print('A media desse aluno é de: {}'.format(media))