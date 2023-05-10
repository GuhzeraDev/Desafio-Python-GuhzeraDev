'''
Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''


velocidade = float(input('Qual a velocidade atual do carro? KM/h: '))
if velocidade > 80:
    valor = velocidade - 80
    multa = valor * 7
    print('Você ultrapassou o limite de 80Km em {:.0f} Km recebendo assim de multa a quantia \n de '
          'R${:.2f} , tendo como base R$7,00 por Km ultrapassado'.format(valor, multa))
print('Tenha um bom dia !! Dirija com segurança')
