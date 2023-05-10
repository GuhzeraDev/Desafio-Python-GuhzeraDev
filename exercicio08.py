'''
Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em
centímetros e milímetros.
'''


n1 = float(input('Digite a quantidade de metros a ser convertido: '))

centimetro = n1 * 100
milimetro = n1 * 1000

print('{} metros convertidos são {:.0f} centimetros e {:.0f} milimetro'.format(n1,centimetro,milimetro))