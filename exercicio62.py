'''

Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.

'''



termo = int(input('Digite o primeiro termo para começar o PA: '))
razao = int(input('Digite a razão da sua PA: '))
cont = 1
numero = termo
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} '.format(numero), end='> ')
        numero = numero + razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
