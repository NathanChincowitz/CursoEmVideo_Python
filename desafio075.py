'''
desenvolva um programa que leia quatro valores pelo teclado e guarde os numa tupla
no final mostre:
a) quantas vezes apareceu o valor 9
b) em que posição foi digitado o primeiro valor 3
c) quais foram os numeros pares
'''

pares = 0

tupla = (int(input('digite o primeiro valor: ')),
         int(input('digite mais um valor: ')),
         int(input('digite outro valor: ')),
         int(input('digite o ultimo valor: ')))

aparições_nove = tupla.count(9)
print(f'\nO numero nove apareceu {aparições_nove} vezes.\n')

if 3 in tupla:
    posição_tres = (tupla.index(3)) + 1
    print(f'O primeiro número 3 apareceu na {posição_tres}° posição.\n')
else:
    print('O número três apareceu 0 vezes.\n')


print('Números pares digitados:', end=' ')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')