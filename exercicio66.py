n = cont = soma = 0

while True:
    n = int(input('Digite um valor (999 para parar) '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram digitados {cont} valores e a soma deles é {soma}')
