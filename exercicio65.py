'''

Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

'''

cont = int(0)
resposta = 'S'
num = int(0)
maior = int(0)
menor = int(0)

while resposta in 'Ss':
    pergunta = int(input('Digite um numero: '))
    num += pergunta
    cont += 1
    if cont == 1:
        maior = pergunta
        menor = pergunta
    else:
        if pergunta > maior:
            maior = pergunta
        if pergunta < menor:
            menor = pergunta
    resposta = str(input('Você deseja digitar mais numeros? [S/N] : ')).upper().strip()[0]

media = num / cont
print('A média dos {} numeros digitados é {} o maior numero é {} e o menor é {} '.format(cont, media, maior, menor))

