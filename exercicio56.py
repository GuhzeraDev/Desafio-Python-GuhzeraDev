'''
Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e
quantas mulheres têm menos de 20 anos.
'''

maisVelho = 0
nomeVelho = ''
mulherMenor = 0
somaIdade = 0

for c in range(1, 5):
    nome = str(input('Pessoa {} digite seu nome: '.format(c))).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [m/f]: ')).strip().lower()
    somaIdade += idade
    if sexo == 'm' and idade > maisVelho:
        maisVelho = idade
        nomeVelho = nome
    if sexo == 'f' and idade < 20:
        mulherMenor += 1

mediaIdade = somaIdade / 4

print('''A média de idade do grupo e de {} 
         O Homen mais velho é o {} com {} anos
         e {} mulheres tem idade menor que 20 anos'''.format(mediaIdade, maisVelho, nomeVelho, mulherMenor))

