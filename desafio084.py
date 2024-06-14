'''
faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista.
no final, mostre:
a) quantas pessoas foram cadastradas
b) uma listagem com as pessoas mais pesadas
c) uma listagem com as pessoas mais leves
'''
#solução do professor
dados = []
lista = []
mai = men = 0

while True:
    dados.append(input('Digite o nome: '))
    dados.append(float(input('Digite o peso: ')))
    if len(lista) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    lista.append(dados[:])
    dados.clear()

    if input('deseja adicionar mais pessoas?[S/N]: ') in 'Nn':
        break


print(f'Foram cadastradas {len(lista)} pessoas. ')
print(f'O maior peso foi de {mai}Kg e o menor de {men}Kg')
print(end=f'As pessoas com maior peso foram: ')
for n in lista:
    if n[1] == mai:
        print(n[0], end='...')
print(end=f'\nAs pessoas com menor peso foram: ')
for n in lista:
    if n[1] == men:
        print(n[0], end='...')
