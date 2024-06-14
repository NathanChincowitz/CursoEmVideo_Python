'''
ex 28: escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5
peça para o usuaio tentar descobrir qual foi o numero escolhido pelo computador

o programa devera escrever na tela se o usuario venceu ou perdeu
_______
melhore o jogo do desafio 028 onde o computador vai 'pensar' em um numero de 0 a 10. Só que agora o jogador vai tentar adivinha ate acertar, mostrando no final quantos palpites foram necessarios para vener
'''
from random import randint
cpu = randint(0,10)
user = ''
round = 0

while cpu != user:
    user = int(input('tente advinhar o numero que a maquinan pensou: '))
    if user > cpu: print('menos, tente novamente.')
    if user < cpu: print('mais, tente novamente.')
    round += 1
print(f'voce acertou, levaram {round} tentativas para acertar')