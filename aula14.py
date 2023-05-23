'''
A condição while pode ser entendida como enquanto, usando a logica enquanto não acontecer a condição x continuarei
por exemplo para fazer um personagem andar ate pegar uma maça como não sabemos quantos passos podemos usar:
while not maça
    passo
pega

podemos notar que neste exemplo enquanto ele não identificar a maça ele ficara no loop de passo ai assim que achar ela
saira do laço e pega ela.

segue exercicio da aula
'''


'''maça = False
chao = True
buraco = False
moeda = True

while not maça:
    if chao == True:
        print('passo')
    if buraco == True:
        print('pula')
    if moeda == True:
        print('pegar moeda')
print('pega maça')'''

'''///////////////////////////////////'''

'''c = 1
while c < 11:
    print(c)
    c = c + 1
print('fim')'''

'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')'''

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')

