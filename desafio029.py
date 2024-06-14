'''
escreva um programa que leia a velocidade de um carro
se ele ultrapassar 80km/h
mostre uma mensagem dizendo que ele foi multado
a multa vai custar R$7,00 por cada Km/h acima do limite
'''

v = int(input('digite a velocidade do carro: '))
if v <= 80:
    print('voce esta dento do limite.')
else:
    multa = (v-80)*7
    print(f'a velocidade maxima é 80km/h voce estava a {v}km/h, devera pagar uma multa de R${multa:.2f}')