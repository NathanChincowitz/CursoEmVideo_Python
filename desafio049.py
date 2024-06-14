'''009 Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

refaça o desafio 009, mostrando a tabuada de um numero que o usaurio escolher, só que agora utilizando o laço for
'''

n = int(input('digite um valor para fazermos tabuada: '))
for i in range(1,11):
    m = n * i
    print(n,'x',i,'=',m)
