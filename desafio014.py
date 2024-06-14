'''Escreva um programa que converta uma temperatura digitando em graus Celsius
e converta para graus Fahrenheit.'''

C = float(input('digite o valor em celcius: '))
F = C * 9 / 5 + 32
print(f'{C}°C são {F}°F')