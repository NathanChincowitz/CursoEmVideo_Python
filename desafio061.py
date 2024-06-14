'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
_____
refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressao usando a estrutura WHILE.
'''
n = int(input('digite o primeiro valor: '))
r = int(input('digite a razao: '))
c = 0
while c<=10:
    n += r
    c += 1
    print(n,end=' ')