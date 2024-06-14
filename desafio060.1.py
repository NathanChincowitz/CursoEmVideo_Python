'''
faça esse exercicio com while, e laço for:
faça um programa que leia um numero qualquer e mostre o seu fatorial
ex: 5!=5x4x3x2x1=120
'''

#LAÇO FOR:
n = int(input('digite um valor para calcular o fatorial: '))
fact = 1
for i in range(n, 1, -1):
    fact *= i
    print(fact)