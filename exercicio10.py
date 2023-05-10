'''
Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
mostre quantos dólares ela pode comprar.
'''


saldo = float(input('Quanto dinheiro você tem na carteira?  '))
dolar = 3.27
converter = saldo/dolar

print('Com seu saldo de {:.2f} reais consegue comprar {:.2f} dolares no dia de hoje.'.format(saldo,converter))
