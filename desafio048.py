'''
faça um poriograma que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no inversalo de 1 a 500
'''
s = 0
c = 0
for i in range(1,501,2):
    if i % 3 == 0:
        c += 1
        s += i
print(f'a soma dos {c} valores, resulta em {s}')