'''
crie um programa que crie uma matriz de simensão 3x3 e preencha com valores lidos pelo teclado
0
1
2
0  1  2
no final, mostre a matriz na tela, com formataçao correta
'''
#MINHA PRIMEIRA SOLUÇÃO
linha_0 = []
linha_1 = []
linha_2 = []
cont = 0
for i in range(0,9):
  if cont <= 2:
    linha_0.append(int(input(f'digite um valor para a posição 0,{cont}: ')))
  elif cont <= 5:
    linha_1.append(int(input(f'digite um valor para a posição 1,{cont-3}: ')))
  else:
    linha_2.append(int(input(f'digite um valor para a posição 2,{cont-6}: ')))
  cont += 1

print(f'''
0: {linha_0}
1: {linha_1}
2: {linha_2}
    0  1  2      
''')