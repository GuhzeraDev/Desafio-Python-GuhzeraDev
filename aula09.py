"""Em uma string ou frase temos a seguinte regra apos declara-la em uma variavel como nesse exemplo a
variavel frase usamos os 2 pontos da seguinte forma: frase[2<<em que caracter da frase começa a mostrar
lembrando que começa em 0 : 9 << Ate qual caracter vai -1 e em ambos se deixar em branco e do começo e fim
respectivamente : 2 << de quanto em quanto pula -1 nesse exemplo do 2 ele pulara 1 caracter]
"""
frase = 'Frase de teste em manipulação de texto'
print('Exemplo 1')
print(frase[2:9:2])
print('Exemplo 2')
print(frase[0::3])
print('Exemplo 3')
print(frase[:4])  #caso o ultimo não seja informado ele não pula nenhum caracter

"""Alguns metodos para analisar as frases:
o len e usado para medir o tamanha da frase como o exemplo a seguir
tambem temos para a mesma função o count que é usado para contar quantas vezes aparece
a letra passada como parametro ex: frase.count('e') onde posso passar tambem junto com o fatiamento
frase.count('e',5<< de onde ate,12<< onde termina -1)
ps: ele entende o maiusculo e minusculo como 
diferentes caracteres
"""
#len e para contar quantos caracteres
print(len(frase))
#count para contar quantas vezes aparece a letra na frase podendo ser combado com o fatiamento
print('count da letra e:')
print(frase.count('e'))
print('count da letra e fatiando do 0 ao 15:')
print(frase.count('e', 0, 15))
#find (encontrar) que justamente mostra em que posição encontrou um conjunto de
# 'letras' / caso não for encontrado ele retornara -1
print('Find:')
print(frase.find('teste'))
#in é um booleano que retornara se existe 'True' ou não 'False' aquela palavra
#na sua frase

"""Passamos daqui para frente para transformação começando com:
replace que substitui o primeiro parametro passado pelo segundo trocando assim a palavra na frase
"""
print('Replace')
print(frase.replace('texto', 'string'))

#upper deixa a frase em maiusculo
print('Upper')
print(frase.upper())

#lower deixa a frase em minusculo
print('Lower')
print(frase.lower())

#capitalize vai jogar tudo pra minusculo porem a primeira maiusculo
#title faz o capitalize palavra por palavra para a primeira letra de cada palavra
#strip Remove os espaços inuteis do começo e fim de uma frase tendo as variaveis
#rstrip indicando o lado right (direita) ou
#lstrip indicando o lado left (esquerda).

#Divisão de strings
#split Divide as palavras das frases como se virasem cada uma uma frase e colocandoos em uma lista sendo
#respectivamente a 1º palavra o spliter 1 a 2° o spliter 2 .....

#'-'.join(frase) junta uma frase splitada usando o que esta entre '' como o separador na hora da junção











