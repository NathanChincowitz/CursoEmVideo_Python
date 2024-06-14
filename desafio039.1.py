'''
faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade
- se ele ainda vai se alistar ao serviço militar
- se é hora de se alisatar
- se ja passou do tempo do alistamento

seu programa tambem deverar mostrar o tempo que falta ou o tempo que passou do prazo
'''
from datetime import date


idade   = int(input('digite seu ano de nascimento: ')) #idade do homem
dezoito = int(date.today().year) - 18                  #18 anos baseado no ano atual

if idade == dezoito:
    print('esta na hora de se alistar')
    
elif idade > dezoito:
    print(f'ainda não é hora, faltam {idade-dezoito} anos para o alistamento obrigatorio')
    
else:
    print(f'seu tempo de alistamento foi a {dezoito-idade} anos atras')