cedula50 = 0
cedula20 = 0
cedula10 = 0
cedula1 = 0
print('-=-' * 15)
print('Bem vindo ao banco do Guh')
print('-=-' * 15)

valor = int(input('Quanto deseja sacar? '))
while True:
    cedula50 = valor // 50
    resto = valor % 50
    cedula20 = resto // 20
    resto = resto % 20
    cedula10 = resto // 10
    resto = resto % 10
    cedula1 = resto // 1
    break

print(f'''Para sacar o valor de {valor} foram ultilizadas:
{cedula50} notas de R$50
{cedula20} notas de R$20
{cedula10} notas de R$10
{cedula1} notas de R$1
''')
print('Volte sempre ao Banco do Guh! Tenha um otimo dia!')

