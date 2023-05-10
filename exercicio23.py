'''
Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um
dos dígitos separados.
'''


numero = int(input('Digite um numero de 0 a 9999 : '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('Unidade: {} '.format(u))
print('Decimal: {} '.format(d))
print('Centena: {} '.format(c))
print('Milhar: {} '.format(m))


"""espacamento = ' '.join(numero)
separado = espacamento.split()

print('Unidade: {} '.format(separado[3]))
print('Decimal: {} '.format(separado[2]))
print('Centena: {} '.format(separado[1]))
print('Milhar: {} '.format(separado[0]))"""
