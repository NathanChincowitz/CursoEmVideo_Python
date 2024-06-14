'''faça um algoritmo que leia o salario de um funcionario
e mostre seu novo salario com 15% de aumento'''
salario = float(input('digite o salario atual: '))

newsalario = salario + (salario*.15)

print(f'o novo salario do funcionario é : R${newsalario}')