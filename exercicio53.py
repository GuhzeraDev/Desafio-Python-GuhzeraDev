'''
Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um
palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
'''

palavra = str(input('Fale uma palavra: ')).strip().upper().split()

palavrasem = ''.join(palavra)
inverso = ''


for letra in range(len(palavrasem) - 1, -1, -1):
    inverso += palavrasem[letra]
if inverso == palavrasem:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')
print('A palavra invertida fica: {}'.format(inverso))

'''if palavrasem == palavrasem[::-1]:
    print('Logo sua palavra e um palindromo')
else:
    print('Logo sua palavra não é um palindromo')'''
