'''
escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
para salarios superiores a 1250 calcule um aumento de 10%
para inferiores ou iguais o aumento é de 15%
'''
n = float(input('digite o valor do salario: R$'))

if n <= 1250:
    aumento = n*1.15
else:
    aumento = n*1.1
    
print(f'com salario de R${n:.2f} o aumento vai para R${aumento:.2f}')