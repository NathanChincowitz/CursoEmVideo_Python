'''
crie um programa que leia dois valores e mostre um menu na tela
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
seu programa devera realizar a operação solicitada em cada caso
'''
cmd = 4
n1  = 0
n2  = 0

while cmd != 5:
    if cmd == 1:
        s = n1+n2
        print(f'a soma de {n1} mais {n2} resulta em {s}')
    if cmd == 2:
        m = n1*n2
        print(f'a multiplicaçao de {n1} vezes {n2} resulta em {m}')
    if cmd == 3:
        if n1 >= n2:
            maior = n1
        else: maior = n2
        print(f'o maior numero entre {n1} e {n2} é {maior}')
    if cmd == 4:
        n1 = int(input('digite o primeiro valor: '))
        n2 = int(input('digite o segundo valor: '))
    if cmd == 5: cmd = 5
    cmd = int(input('''
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
DIGITE O COMANDO DESEJADO: '''))

print('programa encerrado')