'''faça um programa que leia a largura e a altura de uma parede
em metros, calcule a sua area e a quantidade de tinta necessaria para pintala 
sabendo que cada litro de tinta pinta uma area de 2m²'''

l = float(input('digite a largura da sua parede em metros: '))
h = float(input('digite a altura da sua parede em metros'))
area = l*h
total = area / 2
print(f'precisara de {total} litros')