'''
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros
'''

valor = float(input('Digite o valor do produto: '))
forma = int(input('''Digite a forma de pagamente de acordo com a tabela a seguir:
                  1 - À vista dinheiro/cheque 
                  2 - À vista no cartão 
                  3 - Em ate 2x no cartão 
                  4 - Em 3x ou mais no cartão 
                  Digite a opção aqui : '''))
if forma == 1:
    print('O valor de pagamento pagando a vista no dinheiro/cheque e de {:.2f} '.format(valor - valor*10/100))
elif forma == 2:
    print('O valor de pagamento pagando a vista no cartão e de {:.2f} '.format(valor - valor*5/100))
elif forma == 3:
    print('O valor de pagamento pagando em ate 2x no cartão e de {:.2f} '.format(valor))
elif forma == 4:
    print('O valor de pagamento pagando em 3x ou mais e de {:.2f} '.format(valor + valor*20/100))
else:
    print('Escolha uma opção valida .... ')