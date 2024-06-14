'''um professor quer sortear um de seus 4 alunos para apagar o quadro
faça um programa que ajude ee, lendo o nome deles e escrevendo
o nome do escolhido'''
import random
n1 = input('digite o nome do primeiro aluno: ')
n2 = input('nome do segundo: ')
n3 = input('nome do terceiro: ')
n4 = input('nome do quarto: ')

'''lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f'o aluno esolhido foi: {escolhido})'''

print(f'o aluno escolhido foi: {random.choice([n1, n2, n3, n4])}')