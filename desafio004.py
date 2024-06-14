'''
faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possiveis sobre ele
'''

a = input('digite algo: ')

#variaveis de cor para falso e true
true  = '\033[1;32mSim!\033[m'
false = '\033[1;31mNão!\033[m'

#determinando as cores para falso e true
space = true if a.isspace()   == True else false
num   = true if a.isnumeric() == True else false
alf   = true if a.isalpha()   == True else false
alfnu = true if a.isalnum()   == True else false
up    = true if a.isupper()   == True else false
low   = true if a.islower()   == True else false
title = true if a.istitle()   == True else false

print(f'''
o tipo primitio desse valor é {type(a)}
só tem espaços? {space}
é númerico? {num}
é alfabetico? {alf}
é alfanumerico? {alfnu}
esta em maiúsculas? {up}
esta em minúsculas? {low}
esta captalizada? {title}
      ''')
