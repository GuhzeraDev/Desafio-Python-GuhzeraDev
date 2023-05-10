'''
Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
 primitivo e todas as informações possíveis sobre ele.
'''

a = input('Digite algo: ')

print('O tipo desse valor é : {} ', type(a))
print('Só tem espaços? ', a.isspace())
print('É numerico? ', a.isnumeric())
print('È alfabeto? ', a.isalpha())
print('È alphanumerico? ', a.isalnum())
print('Esta maiuscula? ', a.isupper())
print('Esta minuscula? ', a.islower())
print('Esta capitalizada? ', a.istitle())