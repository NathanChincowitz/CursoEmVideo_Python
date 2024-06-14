'''
faça um program que leia 5 valores numericos e guarde-os em uma lista 
no final mostre qual foi o maior e o menor valor digitado e as suas respectivas posiçoes na lista (precisa mostrar se aparecer o mesmo numero em mais de uma posição)
'''
lista = []
maior = menor = 0
for i in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
 


        
print(f'o maior valor encontrado foi {maior}, ele esta localizado nas chaves: ', end=' ')
for indice, valor in enumerate(lista):
    if valor == maior:
        print(f'{indice}....', end=' ')
        
print('\n')
print(f'o menor valor encontrado foi {menor}, ele esta localizado nas chaves: ', end=' ')
for indice, valor in enumerate(lista):
    if valor == menor:
        print(f'{indice}....', end='')

