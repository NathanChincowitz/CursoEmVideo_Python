'''
crie um programa que leia a idade de varias pessoas
a cada pessoa cadastrada, o programa devera perguntar se o usuario quer ou nao consitnuar
no final mostre:
a) quantas pessoas tem mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres tem menos de 20 anos.
'''

age = w = m = older = 0

while True:
    s = ' '
    input('digite o nome: ')
    while s not in 'MF':
        s = input('informe o sexo: M/F: ').strip().upper()[0]
    age = int(input('informe a idade: '))
    
    if age >= 18:
        older+=1
    
    if s == 'M':
        m+=1
    
    if s == 'F' and age < 20:
        w+=1
        
    while continuar not in 'SN':
        continuar = input('deseja continuar? S/N: ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'foram cadastrados {older} pessoas com mais de 18 anos, {m} homens e {w} mulheres com menos de 20 anos.')