'''
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
'''


peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('De acordo com seu IMC de {:.1f} você esta: Abaixo do peso '.format(imc))
elif 18.5 <= imc <= 25:
    print('De acordo com seu IMC de {:.1f} você esta: No peso ideal '.format(imc))
elif 25 <= imc <= 30:
    print('De acordo com seu IMC de {:.1f} você esta: Em Sobrepeso '.format(imc))
elif 30 <= imc <= 40:
    print('De acordo com seu IMC de {:.1f} você esta: Em Obesidade '.format(imc))
else:
    print('De acordo com seu IMC de {:.1f} você esta: Em Obesidade Morbida '.format(imc))