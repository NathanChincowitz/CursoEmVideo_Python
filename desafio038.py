'''
escreva um programa que leia dois numeros interios e compare-os mostrando na tela uma mensagem
- o primeiro valor é maior
- o segundo valor é maior
- nao existe valor maisor, os dois sao iguais
'''

n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo: '))

if n1 > n2:
    print('o primeiro valor é maior')

elif n1 < n2:
    print('o segundo valor é maior')

else:
    print('os valores sao iguais')