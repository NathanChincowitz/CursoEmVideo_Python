'''
elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento

- a vista dinheiro/cheque 10% desconto
- a vista cartao 5% desconto
- em ate 2x no cartao preço normal
- 3x ou mais no cartao 20% de juros
'''

valor = float(input('digite o valor do produto: R$'))
pagamento = int(input('''
Informe o meio de pagamento:
[1] para a vista dinheiro/cheque desconto 10%
[2] para a vista cartao desconto 5%
[3] em ate 2x no cartao preço normal
[4] caso 3x ou mais no cartao juros 20%
digite a opção: '''))

if pagamento == 1:
   n = valor*.9 # -10%
   print(f'o produto saira por R${n:.2f} á vista no dinheiro/cheque!')
elif pagamento == 2:
    n = valor*.95 # -5%
    print(f'o produto sairá por R${n:.2f} á vista no credito!')
elif pagamento == 3:
                  # valor normal
    print(f'o produto sairá por R${valor:.2f} em ate 2x no credito!')
elif pagamento == 4:
    n = valor*1.2 # +20%
    print(f'o produto sairá por R${n:.2f} em 3x ou mais vezes no credito!')
else:
    print('opção não válida!')
