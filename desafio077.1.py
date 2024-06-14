'''
crie um programa que tenha uma tupla com varias palavras (nao usar acentos).
depois disso, voce deve mostrar, para cada palavra, quais sao as suas vogais
'''
#minha solução
#primeira versao
'''tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for i in range(0,(len(tupla))):
    print(f'Na palavra {(tupla[i]).upper()}, estão as vogais:', end=' ')
    for v in range(0,(len(tupla[i]))):
        vogal = tupla[i]
        if 'a' == vogal[v]:
            print('a', end =' ')
        if 'e' == vogal[v]:
            print('e', end =' ')
        if 'i' == vogal[v]:
            print('i', end =' ')
        if 'o' == vogal[v]:
            print('o', end =' ')
        if 'u' == vogal[v]:
            print('u', end =' ')
    print('\n')
'''
#segunda versao
tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for i in tupla:
    print(f'Na palavra {i.upper()}, estão as vogais:', end=' ')
    for v in i:
        if 'a' == v:
            print('a', end =' ')
        if 'e' == v:
            print('e', end =' ')
        if 'i' == v:
            print('i', end =' ')
        if 'o' == v:
            print('o', end =' ')
        if 'u' == v:
            print('u', end =' ')
    print('\n')