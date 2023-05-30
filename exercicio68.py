from random import randint
n = 0
cont = 0
escolha = 'P'


print('=-='*10)
print('Vamos jogar par ou impar')
print('=-='*10)
while True:
    n = int(input('Diga um valor: '))
    escolha = str(input('Par ou Impar? [P/I] ')).upper().strip()
    ale = randint(0, 10)
    soma = n + ale
    print(f'Você colocou {n} e eu coloquei {ale} dando {soma} que é ', end='')
    if soma % 2 == 0:
        print('Par')
        if escolha == 'P':
            print('Você venceu vamos mais uma vez.')
        else:
            print('Eu ganhei!!')
            break
    else:
        print('Impar')
        if escolha == 'I':
            print('Você venceu vamos mais uma vez.')
        else:
            print('Eu ganhei!!')
            break
    cont += 1
print(f'Você ganhou {cont} vezes antes de perder!!')
