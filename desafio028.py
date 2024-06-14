'''
escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5
peça para o usuaio tentar descobrir qual foi o numero escolhido pelo computador

o programa devera escrever na tela se o usuario venceu ou perdeu
'''
from random import randrange, randint
from time import sleep
n2 = randint(0, 5)
print('-+-' *20)
print('vou pensar em número, tente adivinhar')
print('-+-' *20)
n1 = int(input('escolha um nnumero de 0 a 5: '))

if n1 > 5 or n1 < 0:
    n1 = int(input('digite um numero que esteja entre 0 e 5: '))
    
#n2 = randrange(6)
sleep(3)
if n1 == n2:
    print(f'parabens, voce acertou o numero era mesmo {n2}!')
else:
    print(f'errou, o numero escolhido pela maquina foi {n2}')