'''
crie um programa que simule o funcionamento de um caixa eletronico
no inicio pergunte ao usuario qual sera o valor a ser sacado (numero inteiro)
e o programa vai informar quantas cedulas de cada valor serao entregues
considere que o caixa possui cedulas de 50, 20, 10 e 1 real
'''
#solução segundo o do professor

while True:
    cedula = 50
    total_cedulas = 0
    valor = int(input('digite um valor para sacar: R$'))
    total = valor
    while True:
        if total >= cedula:
            total -= cedula
            total_cedulas += 1
        else:
            print(f'Total de {total_cedulas} cedulas de R${cedula:.2f}')
            total_cedulas = 0
            if cedula == 50:
                cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 1
            if total == 0:
                break
            
    continuar = ' '
    while continuar not in '12':        
        continuar = (input('''
    [1] Sacar Novo Valor
    [2] Sair
                        
    Selecione: ''')).strip()[0]
    if continuar == '2':
        break
