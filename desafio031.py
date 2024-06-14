'''
desenvolva um programa que pergunte a distancia de uma viagem em km
calcule o preço cobrando R$0,50 por km para viagens ate 200km
e R$0.45 para viagens mais longas
'''

km = float(input('digite a distancia em Km da viagem desejada: '))

#custo = km * 0.50 if km <= 200 else km * 0.45

if km <=  200:
    custo = km * 0.50
else:
    custo = km * 0.45
print(f'o custo da viajem de {km}km sera de R${custo:.2f}')