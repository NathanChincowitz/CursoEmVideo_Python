'''
faça um programa que leia um numero inteiro e diga se ele é ou nao um numero primo
'''

n = int(input('digite um numero para verificr se ele é primo: '))
c = 0

for i in range(1,n+1):
    if n % i == 0:
        c += 1
if c != 2:
    print(f'{n} nao é primo')
elif c == 2:
    print(f'{n} é um numero primo')