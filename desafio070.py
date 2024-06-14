'''
crie um programa que leia o nome de varios produtos.
o programa devera perguntar se o usuario vai continuar
no final mostre
a) qual é o total gasto na compra
b) quantos produtos custam mais de R$1000
c) qual é o nome do produto mais barato
'''

produto = cheapperSTR = ''
expensive = valor = total = cheapperFLOAT = 0


while True:
    continuar = ' '
    
    produto = input('digite o nome do produto: ').strip().capitalize()
    
    valor = float(input('digite o valor do produto: R$'))
    print('total', total, 'valor', valor)
    total += valor
    print('total', total, 'valor', valor)
    if valor >= 1000:
        expensive += 1

    elif cheapperFLOAT == 0:
        cheapperFLOAT = valor
        cheapperSTR = produto
        
    elif cheapperFLOAT < valor:
        cheapperFLOAT = valor
        cheapperSTR = produto

    while continuar not in 'SN':
        continuar = input('deseja continuar? S/N: ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'''
O total gasto foi de R${total:.2f}
{expensive} produtos custaram mais de R$1000,00
O nome do produto mais barato é {cheapperSTR}
      ''')