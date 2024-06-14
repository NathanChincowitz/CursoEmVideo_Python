'''
faça um programa que mostre na tela um contagem reggressiva para o estouro de fogos de artificio, indo de 10 ate 0, com uma pausa de 1 segundo entre eles
'''
from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BOOOM BOM BOOOOOOOOOM BOOOOOOOOOOOOOOOOOOOOOOOOOM PA PA PA PAAA')