'''
Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço
a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

Km = int(input('Quantos Km foram percorridos? Km: '))
dias = int(input('Quantos dias foi alugado? '))
conta = (60 * dias) + (Km * 0.15)

print('Levando em consideração que cobramos 60 por dia e R$0.15 por Km rodado o total a pargar é {:.2f} '.format(conta))