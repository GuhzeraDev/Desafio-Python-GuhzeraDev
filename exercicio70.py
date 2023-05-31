'''
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.

'''

total = menor = caro = 0
nomeBarato = ''

while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preço = float(input('Qual o preço deste produto? R$'))
    if total == 0 or preço < menor:
        menor = preço
        nomeBarato = nome
    total += preço
    if preço > 1000:
        caro += 1
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Vai continuar [S/N]: ')).upper().strip()[0]
    if pergunta == 'N':
        break
print(f'''(A) O total gasto na compra foi R${total:.2f}
(B) {caro} produtos custam mais de R$1000
(C) O produto mais barato é o {nomeBarato} que custa R${menor:.2f}
''')
