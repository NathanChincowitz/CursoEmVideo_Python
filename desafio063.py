'''
escreva um programa que leia um numero N inteiro qualquer e mostre na tela os N primeiros elementos de uma sequencia fibonacci
'''

n1 = 0
n2 = 1
n3 = 0
c = 3
termos = int(input('digite o numero de termos que deseja printar a sequencia: '))
print(f'{n1} {n2}',end=' ')
while c <= termos:
#    if c == termos:
#        termos = int(input('digite o numero de termos que deseja printar a sequencia: '))
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    c += 1
    print(n3, end=' ')
print('''
o programa se encerrou''')