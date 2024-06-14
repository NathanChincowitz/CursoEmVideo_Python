'''
crie um programa que vai gerar cinco numeros aleatorios e colocar em uma num.
depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estao na num
'''
from random import randint

num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), )

print('Os numeros gerados foram: ',end='')
for i in num:
    print(i, end=' ')
print('\nO menor valor é: ', sorted(num)[0])
print('O maior valor é: ', sorted(num)[-1])

#metodo feito pelo professor
#print(f'o maior valor foi {max(num)}')
#print(f'o menor valor foi {min(num)}')