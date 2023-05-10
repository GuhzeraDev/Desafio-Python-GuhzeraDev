# vendo tipo e usando is...
v1 = input('Digite algo: ')
print('O tipo do que foi digitado é: {}'.format(type(v1)))

print('Ele é numerico? {}'.format(v1.isnumeric()))
print('Ele e alphabetico {}'.format(v1.isalpha()))
print('Ele e alphanumerico {}'.format(v1.isalnum()))
print('Ele esta escrito todo em maiusculo? {}'.format(v1.isupper()))
