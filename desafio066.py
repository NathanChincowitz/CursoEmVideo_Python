'''
crie um programa que liea varios numeros inteiros pelo teclado
o programa só vai parar quando o usuario digiar o valor 999
que é a condição de parada. no final
mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando a flag)
'''

c = t = n = 0

while True:
    n = int(input('digite um valor para somar: '))
    if n == 999:
        break
    t += n
    c += 1
print(f'foram digitados {c} valores, e sua soma é {t}')