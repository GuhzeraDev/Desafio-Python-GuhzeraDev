#Para estrutura condicional famosos if else e elif podemos fazer do modo simples
idade = int(input('Quantos anos você tem? '))

if idade >= 18:
    print('Você já e de maior')
else:
    print('Você é de menor')

#Porem podemos usar o if simplificado escrevendo em menas linhas
#Parecido com o "Ternario" em outras linguagens

tempo = int(input('Quantos anos tem seu carro? '))

#print('Carro novo') if tempo <= 3 else print('Carro velho')
#ou ate mais simplificado sendo colocado dentro do print
print('Carro novo' if tempo <= 3 else 'Carro velho')