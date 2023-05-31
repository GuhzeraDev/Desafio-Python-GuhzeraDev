'''
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''


n = 0

while True:
    m = 1
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    while m < 11:
        print(f'{n} x {m} = {n * m}')
        m += 1
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!!')
