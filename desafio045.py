'''
faça um programa que faça o computador jogar jokenpo com voce
pedra papel tesoura
'''
import random
pc = random.choices([1,2,3])
if pc == [1]:
    pc = 'Pedra'
elif pc == [2]:
    pc = 'Papel'
elif pc == [3]:
    pc = 'Tesoura'

n = input('''
Pedra
Papel
Tesoura
Escolha sua jogada: ''').strip().title()

if pc == n:
    print(f'empate! ambos escolheram {n}')
elif (pc == 'Pedra' and n == 'Papel') or (pc == 'Papel' and n == 'Tesoura') or (pc == 'Tesoura' and n == 'Pedra'):
    print(f'voce escolheu {n} e o computador escolheu {pc}, voce ganhou!')
elif (pc == 'Pedra' and n == 'Tesoura') or (pc == 'Tesoura' and n == 'Papel') or (pc == 'Papel' and n == 'Pedra'):
    print(f'voce escolheu {n} e o computador escolheu {pc}, voce perdeu!')