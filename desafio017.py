'''faça um programa que leia o comprimento do cateto oposto 
e do cateto adjacente de um triangulo retangulo, calcule o comprimento da hipotenusa'''
from math import hypot
a = float(input('digite o valor de A: '))
b = float(input('digite o valor de B: '))

'''
cod que fiz antes de saber da existencia do hypot
h = (a**2+b**2)**(1/2)'''
h = hypot(a, b)

print(f'com tetetos {a} e {b} a hipotenusa dele triangulo retangulo é {h:.2f} ')
