'''Faça um programa que leia um número inteiro  e msotre na tela seu sucessor e seu antecessor.'''

n   = int(input('digite um valor: '))
ant = n - 1
sus = n + 2
colors = {'cor1' :'\033[36m',
          'cor2' :'\033[34m',
          'fecha':'\033[m'
          }

print(f'seu antecessor é {colors["cor1"]}{ant}{colors["fecha"]} e seu sucessor é {colors["cor2"]}{sus}{colors["fecha"]}')
