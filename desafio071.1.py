'''
crie um programa que simule o funcionamento de um caixa eletronico
no inicio pergunte ao usuario qual sera o valor a ser sacado (numero inteiro)
e o programa vai informar quantas cedulas de cada valor serao entregues
considere que o caixa possui cedulas de 50, 20, 10 e 1 real
'''

total = cinquenta = cinquenta_troco = vinte = vinte_troco = dez = dez_troco = um = continaur = 0

while True:
    total = int(input('digite um valor para sacar: R$'))
    
    cinquenta = total // 50
    cinquenta_troco = cinquenta * 50

    vinte = (total - cinquenta_troco) // 20
    vinte_troco = vinte * 20

    dez = (total - cinquenta_troco - vinte_troco) // 10
    dez_troco = dez * 10

    um = (total - cinquenta_troco - vinte_troco - dez) // 1

    print(f'''
    {cinquenta} notas de R$50
    {vinte} notas de R$20
    {dez} notas de R$10
    {um} notas de R$01
    ''')

    continuar = int(input('''
    [1] Sacar Novo Valor
    [2] Sair
                          
    Selecione: '''))
    if continuar == 2:
        break
    