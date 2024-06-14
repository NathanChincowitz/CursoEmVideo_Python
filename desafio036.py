'''
escreva um programa para aprovar o emprestimo bancario para a compra de uma casa
o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar

calcule o valor da prestação mensal
sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado
'''


print('Insira os dados necessários para calcularmos o empréstimo!')

casa    = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite seu salário atual: R$'))
meses   = int(input('Insira o tempo desejado em meses: '))

if casa / meses <= .3 * salario:
    print('seu financiamento foi aceito!!')

else:
    print('seu financiamento foi negado!')