'''
faça esse exercicio com while, e laço for:
faça um programa que leia um numero qualquer e mostre o seu fatorial
ex: 5!=5x4x3x2x1=120
'''

#WHILE: 
n = int(input('digite um valor para calcular o fatorial: '))
fact = 1
while n != 1:
    fact *= n
    n -= 1
    print(fact)