'''
desenvolova um programa uqe leia seis numeros inteiros e mostre a soma apenas daquelas que forem pares. se o valor digitado for impar desconsidere-o
'''
s = 0
c = 0
for i in range(1,7):
    n = int(input(f'digite o {i}° valor: '))
    if n % 2 == 0:
        s += n
        c += 1
print(f'voce informou {c} valores pares, e sua some é {s}')