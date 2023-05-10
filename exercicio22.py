'''
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.
'''


nome = str(input('Digite seu nome completo: ')).strip()
separado = nome.split()

print('Nome digitado {} '.format(nome))
print('Nome digitado com todas as letras maiusculas {} '.format(nome.upper()))
print('Nome digitado com todas as letras minusculas {} '.format(nome.lower()))
print('Quantidade de letras sem considerar os espaços {} '.format(len(nome) - nome.count(' ')))
#print('O primeiro nome tem {} letras'.format(nome.find(' ')))
print('O primeiro nome é {} '.format(separado[0]))