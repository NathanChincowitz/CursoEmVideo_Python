'''
faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F', casso eseteja errado peça a digitação novamente ate ter um valor correto
'''
sexo = ' '
sexo = str(input('digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('informe uma opção válida, digite seu sexo [M/F]: ')).strip().upper()[0]

print(f'voce selecionou {sexo}')