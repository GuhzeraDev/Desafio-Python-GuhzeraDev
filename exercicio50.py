'''
Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

num = 0
tab = []
for c in range(1, 7):
    n = int(input('Digite o {}º numero: '.format(c)))
    if n % 2 == 0:
        #tab.append(n)
        tab.insert(len(tab)+1, n)
        num += n

print('A soma de todos os numeros pares que você digitou que são {} é de {}'.format(tab, num))