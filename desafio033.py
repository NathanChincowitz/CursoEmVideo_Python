'''faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor'''
n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))
n3 = int(input('digite o terceiro valor: '))

lista = sorted([n1,n2,n3])

print(f"""
O menor numero é {lista[0]}
O maior numero é {lista[2]}
      """)
