'''
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta
viagens mais longas.
'''


pergunta = float(input('Quantos Km tera sua viajem? '))
'''if pergunta <= 200:
    print('O valor da passagem é de R${:.2f} '.format(pergunta * 0.50))
else:
    print('O valor da passagem é de R${:.2f} '.format(pergunta * 0.45))'''

preço = pergunta * 0.50 if pergunta <= 200 else pergunta * 0.45
print('O valor da passagem é de R${:.2f} '.format(preço))
