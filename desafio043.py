'''
desenvolva uma logica que leia o peso e a altura de uma pessoa calcule seu imc e mostre seu status de acordo com a tabela abaixo
- abaixo de 18,5 abaixo do peso
- entre 18,5 e 25 peso idial
- 25 ate 30 sobremeso
- 30 ate 40 obesidade
- acima de 40 obesidade morbida

IMC = kg/m2
'''

kg = float(input('digite seu peso em kg: '))
m  = float(input('digite sua altura em metros: '))

imc = kg/m**2

if imc < 18.5:
    print(f'seu imc é de {imc:.1f} e esta abaixo do peso ideal')
elif imc < 25:
    print(f'seu imc é de {imc:.1f} e esta na faixa de peso ideal')
elif imc < 30:
    print(f'seu imc é de {imc:.1f} e esta com sobrepeso')
elif imc < 40:
    print(f'seu imc é de {imc:.1f} e esta com obesidade')
else:
    print(f'seu imc é de {imc:.1f} e esta com obesidade')