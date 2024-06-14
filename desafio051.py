'''
desenvolva um programa que leia o primeiro termo e a razao de uma PA. no final, mostre os 10 primeiros termos dessa progressão.
'''

n1 = int(input('digite o primeiro termo da PA: '))
r  = int(input('digite a razão da PA: '))

for i in range(0,10):
   n1 += r
   print(n1-r, end=' ')