'''
crie um programa que leia varios numeros inteiros pelo teclado. o programa só vai parar quando o usuario digitar o valor 999
que é a condição de parada, no final mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o comando para parar)
'''
c = n = s = 0

while n != 999:
    n = int(input('digite um valor, para parar a soma digite[999]: '))
    if n != 999:
        s += n
        c += 1
print(f'voce digitou {c} valores, e a some entre eles é de {s}')