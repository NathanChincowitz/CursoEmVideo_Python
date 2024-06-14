'''
crie um programa que leia o ano de nascimento de sete pressoas no final mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores (21 anos)
'''
from datetime import datetime

hoje = datetime.today().year
c = 0

for i in range(1,8):
    n = int(input(f'{i}° pessoa nasceu em: '))
    if (hoje - n) >= 21:
        c += 1
print(f'{c} pessoas atingiram a maioriadae')