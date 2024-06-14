'''
crie um programa que leia varios numeros inteiros pelo teclado. no final da execução mostre a media entre todos os valores e qual foi o maior e o menor valores lidos. 
o programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores
'''
max = 0
min = 0
c = 0
s = 0
continuar = 'S'

while continuar in 'Ss':
    n = int(input('digite um valor para somar: '))
    if c == 0: #com a mesma ideia do ex 55, verificando se é a primeira rodada para dar um valor diferente de 0 para o minimo
        min = n
        max = n
    if n > max:
        max = n
    if n < min:
        min = n
    s += n
    c += 1
    continuar = str(input('adicionar mais um numero?[S/N]: '))
m = s / c
print(f'foram digitados {c} valroes, a media da soma é {m:.2f}, o maior valor é {max} e o menor valor é {min}')