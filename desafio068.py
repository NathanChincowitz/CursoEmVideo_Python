'''
faça um programa que jogue par ou impar com o computador
o jogo sera interrompido quano o jogador PERDER,
mostrando o total de vitorias consecutivas que ele constou no final do jogo
- digite um valor
- escolha P/I
'''
from random import randint, choice
wins = 0

while True:
    user2 = continuar = ' '
#gerando valor para maquina
    cpu = randint(0,10)
    print('Vamos jogar par ou ímpar')
#coletando valor do usuario, numero escolhido e se escolheu par ou impar
    user1 = int(input('digite um numero de 0 a 10: '))
    while user2 not in 'PI':
        user2 = str(input('agora escolha entre par ou impar [digite P ou I]: ')).strip().upper()[0]

    soma = (cpu + user1)%2
    
    if soma == 0:
        result = 'P'
    else:
        result = 'I'
        
#identificar vencedor
    if result == user2:
        print('Parabens voce ganhou!')
        wins += 1
    else:
        print('voce perdeu!')        
        print(f'voce ganhou {wins} vezes seguidas')
        wins = 0

#condição para fechar o jogo
    while continuar not in 'NS':
        continuar = input('deseja continuar? S/N: ').strip().upper()[0]
    if continuar == 'N':
        break

