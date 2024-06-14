'''o mesmo professor do desafio anteior, quer sortear a ordem de apresentação
do trabalho dos alunos
faça um programa que leia o nome dos 4 e mostre a ordem sorteada'''

import random
n1 = input('digite o nome do primeiro aluno: ')
n2 = input('nome do segundo: ')
n3 = input('nome do terceiro: ')
n4 = input('nome do quarto: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'a ordem sorteada foi {lista}')