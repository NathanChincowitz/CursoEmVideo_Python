'''
crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "santo".
'''

cidade = input('digite o nome da sua cidade: ').lower().strip()

santo = cidade.split()
print('santo' in santo[0])