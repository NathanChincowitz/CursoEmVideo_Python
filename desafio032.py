'''
faça um programa que leia um ano qualquer e mostre se ele é bissexto

"São bissextos todos os anos múltiplos de 400, exceto se for múltiplo de 100, mas não de 400"
'''
from datetime import date
n = int(input('digite um ano para verificar se ele é bissexto! coloque 0 para verificar o ano atual:  '))

#if int(n/4) == n/4:
if n == 0:
    n = date.today().year
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print(f'{n} é um ano bisexto!')

else:
    print(f'{n} não é ano bisexto!')