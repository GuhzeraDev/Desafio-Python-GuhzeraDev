'''
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''
adulto = 0
homen = 0
mulher = 0

while True:
    print('-=-' * 20)
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
    if idade > 18:
        adulto += 1
    if sexo == 'M':
        homen += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if pergunta == 'N':
        break
print('-=-' * 20)
print(f'''(A) {adulto} pessoas tem mais de 18 anos.
(B) {homen} pessoas são homens
(C) {mulher} pessoas são mulheres e tem menos de 20 anos
''')
