n = 0

while True:
    m = 1
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    while m < 11:
        print(f'{n} x {m} = {n * m}')
        m += 1
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!!')
