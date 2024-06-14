'''
cire um programa que leia o nome completo de uma pesoa e mostre:
o nome com todas as letras maiusculas
o nome com todas as letras minusculas
quantas letras tem sem considerar espaços
quantas letras tem o primeiro nome
'''

nome = (input('digite seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count (' '))

dividido = nome.split()
#print(len(''.join(dividido)))

print(len((dividido[0])))