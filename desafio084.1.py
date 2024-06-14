'''
faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista.
no final, mostre:
a) quantas pessoas foram cadastradas
b) uma listagem com as pessoas mais pesadas
c) uma listagem com as pessoas mais leves
'''
lista = []
dados = []

while True:
    dados.append(input('Digite o nome: '))
    dados.append(int(input('Digite o peso: ')))
    if lista == [] or dados[1] >= lista[-1][1]:
        lista.append(dados[:])
    else:
        pos = 0
        while pos < len(lista):
            if dados[1] <= lista[pos][1]:
                lista.insert(pos, dados[:])
                break
            pos += 1
            
#    print('lista', lista)
    dados.clear()

    if input('deseja adicionar mais pessoas?[S/N]: ') in 'Nn':
        break
    
print(f'''
Foram cadastradas {len(lista)} pessoas.
As pessoas mais pesadas são {lista[-2][0]} e {lista[-1][0]}, com {lista[-2][1]}Kg e {lista[-1][1]}Kg respectivamente.

E as mais leves são {lista[0][0]} e {lista[1][0]}, com {lista[0][1]}Kg e {lista[1][1]}Kg respectivamente.
      ''')