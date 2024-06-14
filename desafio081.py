'''
crie um program que vai ler varios numeros e colocar em uma lista
depois disso, mostre:
a) quantos numeros foram digitados
b) a lista de valores ordenada de forma decrescente
c) se o valor 5 foi digitado e esta ou nao na lista
'''
lista = []
while True:
    number_input = (input('Para cancelar digite um NÃO númerico. Digite um valor para adicionar:'))
    # primeira vez testando o try, usando ele para verificar se o valor digitado é ou nao numerico para entao terminar o programa;
    try:
        int(number_input)
    except ValueError:
        break
    
    lista.append(int(number_input))
#apos ver a solução percebi que poderia ter simplificado esse inicio para:
#while True:
#    try:
#        lista.append(int(input('Para cancelar digite um NÃO númerico. Digite um valor para adicionar:')))
#    except ValueError:
#        break
#_________________________________________________________________________________________________________

#usando um laço for para reverter o sorted
lista2 = []
for n in sorted(lista):
    lista2.insert(0,n)

print(f'Foram digitados {len(lista2)} numeros na lista.')
if 5 in lista2:
    print('a lista em ordem descrescente fica: ', end='')
    for n in lista2:
        if n == 5:
            print(f'\033[1;31m{n}\033[m',end='...')
        else:
            print(n,end='...')
else:
    print(end='a lista em ordem descrescente fica: ')
    for n in lista2:
        print(n,end='...')