'''
desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- a media de idade do grupo
- qual o nome do homem mais velho
- quantas mulheres tem menos de 20

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
media    = 0
nOlder   = 0
strOlder = ''
mulheres = 0

for i in range(1,5):
    name = str(input(f'digite o nome da {i}° pessoa: ')).strip().title()
    age  = int(input(f'digite a idade da {i}° pessoa: '))
    sexo = str(input(f'informe o sexo da {i}° pessoa, M para masculino e F para feminino: ')).strip().title()
    media += age
    if sexo == 'M' and age > nOlder:
        strOlder = name
        nOlder   = age
    if sexo == 'F' and age < 20:
        mulheres += 1

media = media/i

print(f'''
A média de idade do grupo foi de {media} anos.
O homem mais velho, com {nOlder}, se chama {strOlder}.
O grupo possuí {mulheres} mulheres com menos de 20 anos.
''')