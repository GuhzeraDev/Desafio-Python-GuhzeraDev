n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

soma = n1 + n2
subtrai = n1 - n2
multiplica = n1 * n2
divide = n1 / n2
divideint = n1 // n2
potencia = n1 ** n2
restodiv = n1 % n2

# quando usado o end pode-se adicionar uma frase que sera apresentada ao final alem de unir as 2 linhas
print('A soma dos numeros é {} a subtração é {}'.format(soma, subtrai), end=' >>> ')
print('A multiplicação é {} e a divisão é {:3f} e o resto da divisão é {}'.format(multiplica, divide, restodiv))
print('A potencia é {} e a divisão inteira é {}'.format(potencia, divideint))
