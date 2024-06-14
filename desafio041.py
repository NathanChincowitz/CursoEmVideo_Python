'''
a confederação nacianal de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade
- ate 9 anos mirim
- ate 14 anos infantil
- ate 19 anos junior
- ate 25 anos senior
- acima master
'''
from datetime import date

hoje = int(date.today().year) #data de hoje

idade = int(input('digite seu ano de nascimento: ')) #idade do atleta

mirim    = hoje - 9
infantil = hoje - 14
junior   = hoje - 19
senior   = hoje - 25

if idade >= mirim:
    print('o atleta esta na categoria mirim!')
elif idade >= infantil:
    print('o atleta esta na categoria infantil!')
elif idade >= junior:
    print('o atleta esta na categoria junior!')
elif idade >= senior:
    print('o atleta esta na categoria senior!')
else:
    print('o atleta esta na categoria master!')