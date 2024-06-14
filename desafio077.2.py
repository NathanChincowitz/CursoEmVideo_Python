'''
crie um programa que tenha uma tupla com varias palavras (nao usar acentos).
depois disso, voce deve mostrar, para cada palavra, quais sao as suas vogais
'''
#solução do professor

tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for i in tupla:
    print(f'\nNa palavra {i.upper()}, estão as vogais:', end=' ')
    for v in i:
        if v.lower() in 'aeiou':
            print(v, end=' ')