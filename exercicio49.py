'''
Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
'''


n = int(input('Escolha um numero para saber a tabuada: '))

for c in range(1, 11):
    print('{} * {} = {}'.format(n, c, n * c))
