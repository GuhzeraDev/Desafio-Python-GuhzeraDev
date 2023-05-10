'''
Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu
 antecessor.
'''
pergunta = int(input('Insira um numero inteiro para saber seu sucessor e antecessor: '))

antecessor = pergunta - 1
sucessor = pergunta + 1

print('Seu numero é o {} tendo como sucessor {} e antecessor {} '.format(pergunta,sucessor,antecessor))