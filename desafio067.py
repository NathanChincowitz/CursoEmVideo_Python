'''
faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario.
o programa sera interrompido quando o numero solicitado for negativo.
'''
n = t = 0

while True:
    n = int(input('digite um valor para gerar sua tabuada(para parar o programa digite um numero negativo): '))
    if n < 0: break
    
    for c in range(1,11):
        t = n * c
        print(f'{c} X {n} = {t}')
print('programa encerrado')