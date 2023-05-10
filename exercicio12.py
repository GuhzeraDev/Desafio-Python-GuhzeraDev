'''
Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo
preço, com 5% de desconto.
'''


pergunta1 = float(input('Qual é o preço do produto? R$'))
desconto = pergunta1 - pergunta1 * 0.05

print('O produto que custava R${:.2f}, na promoção com 5% de deconto vai custar R${:.2f}'.format(pergunta1, desconto))
