total = 0
menor = 99999999
nomeBarato = ''
caro = 0

while True:

    nome = str(input('Digite o nome do produto: ')).strip()
    preço = int(input('Qual o preço deste produto? R$'))
    total += preço
    if preço > 1000:
        caro += 1
    if preço < menor:
        menor = preço
        nomeBarato = nome

    pergunta = str(input('Vai continuar [S/N]: ')).upper().strip()
    if pergunta == 'N':
        break
print(f'''(A) O total gasto na compra foi R${total}.
(B) {caro} produtos custam mais de R$1000.
(C) O produto mais barato é o {nomeBarato} que custa R${menor}
''')