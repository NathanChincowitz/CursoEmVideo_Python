'''
crie um programa que leia dois números e msotre a soma entre eles.
'''
from time import sleep
print('\033[1;31mVamos somar dois números!\033[m')
sleep(1)

n1 = int(input('Digite o \033[1;32mprimeiro\033[m número: '))
n2 = int(input('Digite o \033[1;33msegundo\033[m número: '))

print('\033[7;40mCalculando...\033[m')
sleep(1)
s = n1+n2
print(f'A some de \033[1;32m{n1}\033[m + \033[1;33m{n2}\033[m é igual a \033[1;4;36;45m {s} \033[m!!!')