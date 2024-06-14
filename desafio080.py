'''
crie um programa onde o usuario possa digitar cinco valores numericos e cadastreos em uma lista
ja na posição correta de inserção (sem utilizar o sort())
no final mostre a lista ordenada na tela
'''

lista = []

for i in range(0,5):
    
    valor_inserido = int(input('Digite um valor para adicionar a lista: '))
    
    if lista == [] or valor_inserido >= lista[-1]:
        lista.append(valor_inserido)
    else:
        pos = 0
        while pos < len(lista):
            if valor_inserido <= lista[pos]:
                lista.insert(pos, valor_inserido)
                break
            pos += 1
print(lista)