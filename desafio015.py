'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

d = float(input('por quantos dias foi alugado?: '))
km = float(input('quantos km foram percorridos com o veículo?: '))

total = d * 60 + (.15 * km)
print(f'o valor total fica em R${total:.2f}')