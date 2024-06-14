'''
desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se elas podem oui nao formar um triangulo

"a soma de dois lados é sempre menor que o terceiro lado"
'''
n1 = float(input('digite o primeiro valor: '))
n2 = float(input('digite o segundo valor: '))
n3 = float(input('digite o terceiro valor: '))

lista = sorted([n1,n2,n3])
a = int(lista[0])
b = int(lista[1])
c = int(lista[2])

if a + b > c:
    print(f'é possivel formar um triângulo com os valores {lista}')
else:
    print(f'{lista} não é possivel formar um triângulo.')
if a * a + b * b == c * c:
    print('inclusive ele tambem é um triangulo retangulo')