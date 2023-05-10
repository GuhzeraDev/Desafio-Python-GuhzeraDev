'''
Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou
não com o nome “SANTO”.
'''


cidade = str(input('Qual cidade você nasceu: ')).strip()
#ciseparada = cidade.lower().split()
#print('Essa cidade começa com Santo? > {} '.format(ciseparada[0] in 'santo'))
print('Essa cidade começa com Santo? > {} '.format(cidade[:5] == 'santo'))