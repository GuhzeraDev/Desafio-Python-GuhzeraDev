adulto = 0
homen = 0
mulher = 0
idade = 0
sexo = 'M'

while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [H/M]: ')).upper().strip()

    if idade > 18:
        adulto += 1
    if sexo == 'H':
        homen += 1
    if sexo == 'M' and idade < 20:
        mulher += 1
    pergunta = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if pergunta == 'N':
        break

print(f'''(A) {adulto} pessoas tem mais de 18 anos.
(B) {homen} pessoas cadastradas são homens
(C) {mulher} pessoas cadastradas são mulheres e tem menos de 20 anos
''')