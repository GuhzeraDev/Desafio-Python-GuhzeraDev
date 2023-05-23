'''
Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão.
'''


termo = int(input('Digite o primeiro termo para começar o PA: '))
razao = int(input('Digite a razão da sua PA: '))
decimo = termo + (10 - 1) * razao

for c in range(termo, decimo + razao, razao):
    print('{} '.format(c), end='> ')
print('Acabou')



'''
tab = []
for c in range(1, 10):
    termo = termo + razao
    #tab.insert(len(tab)+1, termo)
    tab.append(termo)
print('Os 10 primeiros numeros do seu PA são: {}'.format(tab))
'''