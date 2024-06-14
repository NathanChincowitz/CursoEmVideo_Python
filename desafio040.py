'''
crie um programa que leia duas notas de um aluno e calcule sua media mostrando uma mensagem no final de acordo com a media atingida
- media abaixo de 5 reprovado
- media entre 5 e 6,9 recuperação
- media 7 ou mais aprovado
'''

n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))

m = (n1 + n2)/2
print(f'com as notas {n1:.2f} e {n2:.2f} sua media foi {m:.2f}')
if m < 5:
    print(f'foi abaixo da media. REPROVADO!')
elif m >= 7:
    print(f'parabens! APROVADO!')
elif m <=7:
    print(f'ainda nao foi suficiente. RECUPERAÇÃO!')