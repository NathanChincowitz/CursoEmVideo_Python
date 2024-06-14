'''
faça um progrma que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
'''

nome = input('\033[35mDigite seu nome: \033[m').title().strip()

print(f'\033[1;32mOlá {nome}, seja muito bem vindo!!\033[m')