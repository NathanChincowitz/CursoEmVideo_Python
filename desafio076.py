'''
crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preçõs, na sequencia
no final, mostre uma listagem de preços, organizando os dados em forma tabular.
(
    lsitagem de preços
   lapis 1,75
   borracha 2,00
   caderno 15,90
   estojo 25,00
   transferidor 9,99
   mochila 120,00
   canetas 22,30
   livro 34,90 
)
'''

listagem_de_precos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
                      'Estojo', 25.00, 'Transferidor', 9.99, 'Mochila', 120.00,
                      'Canetas', 22.30, 'Livro', 34.90)

print('-' * 40)
print(f'{"Listagem de Preços":^40}')
print('-' * 40)
for i in range(0,(len(listagem_de_precos)),2):
    if i % 2 == 0:
        print(f'{listagem_de_precos[i]:.<30}', end='')
    print(f' R${listagem_de_precos[i+1]:>7.2f}')
print('-' * 40)