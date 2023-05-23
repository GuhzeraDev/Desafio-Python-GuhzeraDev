'''
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''


from random import randint

cont = 0
numAle = randint(0, 10)
pergunta = 0

print('Tente adivinhar o numero aleatorio gerado entra 0 e 10:')

while pergunta != numAle:
    if cont < 1:
        pergunta = int(input('Tente acertar: '))
    else:
        pergunta = int(input('Você errou, tente novamente: '))
    cont += 1
print('Parabens você acertou na sua {}º tentativa'.format(cont))
