"""
Anunciado: Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
Pergunte o valor da casa, o salario e em quanto tempo pretende pagar,
A prestação mensal não pode ultrapassar 30% do salario ou então o emprestimo sera negado.
"""


vcasa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual seu salario? '))
qanos = float(input('Em quantos anos pretende pagar? ')) * 12
parcela = vcasa / qanos

limite = (salario * 30) / 100

if parcela <= limite:
    print('Emprestimo aprovado, a parcela sera de {:.2f} por mês'.format(parcela))
else:
    print('Emprestimo negado, o valor da parcela de {:.2f} excede 30% do seu salario que é {}'.format(parcela, limite))

