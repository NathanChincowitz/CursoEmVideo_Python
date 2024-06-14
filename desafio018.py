'''faça um programa que leia o angulo qualquer 
e mostre na tela o valor do seno cosseno 
e tangente desse angulo'''
import math
angulo = float(input('digite o valor do angulo: '))
sen = math.sin(math.radians(angulo))
print(f'o angulo {angulo} tem o seno de {sen:.2f}')
cos = math.cos(math.radians(angulo))
print(f'o angulo {angulo} tem o cosseno de {cos:.2f}')
tan = math.tan(math.radians(angulo))
print(f'o angulo {angulo} tem a tangente de {tan:.2f}')