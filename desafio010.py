'''crie um programa que leia quanto dinheiro uma pessoa tem na carteuira
e mostre quantos dolares ela pode comprar
considere
us$1,00 = R$3,27'''

n = float(input('digite quantos reais voce possui: R$'))
dollar = 3.27
print(f'voce pode comprar {n//dollar} dolares')