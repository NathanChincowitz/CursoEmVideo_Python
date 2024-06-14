'''
crie um programa que tenha uma tupla totalmente preeenchida com uma contagem por extenso de zero ate vinte
seu programa devera ler um numero pelo teclado(entre 0 e 20)
e mostra-lo por extenso
'''

num_extenso = ('zero', 'um', 'dois', 'três', 'quadro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        num = int(input('digite um numero de 0 a 20: '))
        if num in range(0,21):
            break

    print(f'O numero {num} por extenso se escreve: {num_extenso[num]}')
    
    continuar = input('deseja continuar?[S/N]: ').strip().upper()[0]
    if continuar in 'N':
        break
