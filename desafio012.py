'''faça um algoritmo que leia o preço de um produto 
e mostre seu novo preço, com 5% de desconto'''
produto = float(input('digite o valor do produto: R$'))
desconto = float(input('digite o valor de desconto desejado: %'))

newproduto = produto - (produto*(desconto/100))
print(f'o novo valor é R${newproduto}')