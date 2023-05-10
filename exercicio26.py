'''
Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas
vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição
ela aparece a última vez.
'''


frase = str(input('Digite um frase: ')).strip().lower()

contagem = frase.count('a')
position = frase.find('a') + 1
rposition = frase.rfind('a') + 1
print('Na sua frase foram encontradas {} vezes a letra "a" sendo a primeiro na posição {} e a ultima'
      'na posição {} .'.format(contagem, position, rposition))
