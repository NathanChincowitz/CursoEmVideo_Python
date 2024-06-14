'''
crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar

(fazer dividindo por dois e identificando se é float ou n)
'''
n = int(input('digite um numero inteiro: '))

#if int(n/2) == n/2:
if n%2 == 0:
    print(f'o numero {n} é par')
else:
    print(f'o numero {n} é impar')