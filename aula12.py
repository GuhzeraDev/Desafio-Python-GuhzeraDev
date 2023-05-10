#Condições aninhadas: São estruturas condicionais dentro de estruturas condicionais

nome = str(input('Digite seu nome: ')).strip()

if nome.lower() == 'gustavo':
    print('Que nome bonito')
elif nome.lower() == 'ana' or nome.lower() == 'maria' or nome.lower() == 'paulo':
    print('Seu nome e muito popular no brasil')
elif nome in 'ana jessica gabriela vitoria':
    print('Que nome feminino bonito')
else:
    print('Seu nome é bem normal')

print('Muito prazer em te conhecer {} '.format(nome))