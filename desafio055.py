'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''
min = 0
max = 0
for i in range(1,6):
    peso = float(input(f'digite o peso da {i}° pessoa: '))
    if i == 1:  #verificando se é a primeira rodada para dar um valor diferente de 0 para o minimo
        max = peso
        min = peso
    else:
        if peso > max: max = peso
        if peso < min: min = peso
print(f'a pessoa mais leve pesa {min:.2f}, e a pessoa mais pesada pesa {max:.2f}')