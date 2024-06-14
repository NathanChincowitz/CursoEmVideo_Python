'''
crie um programna que vai ler varios numeros e colocar em uma lista 
depois disso crie duas listas extras que vao conter apenas os valores pares e os valores impares digitados, respectivamente
ao final, mostre o conteudo das tres listas geradas
'''
lista_inicial = []

while True:
    try:
        lista_inicial.append(int(input('Para cancelar digite nao numericos. Digite um numero: ')))
    except ValueError:
        break

impar = []
par = []
for n in sorted(lista_inicial):
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(end='Os numeros digitados foram: ')
for n in sorted(lista_inicial):
    print(n,end='...')

print('\n',end='Os numeros ímpares são: ')
for i in impar:
    print(i,end='...')

print('\n',end='Os numeros pares sao: ')
for p in par:
    print(p,end='...')
