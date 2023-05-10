'''
Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.

Aula Anterior

'''


salario = float(input('Qual e o seu salario? '))

if salario > 1250:
    novo = (salario * 10) / 100
else:
    novo = (salario * 15) / 100

print('Seu aumento é de {:.2f} e o novo salario e de {:.2f} '.format(novo, novo + salario))
