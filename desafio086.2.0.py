'''
crie um programa que crie uma matriz de simensão 3x3 e preencha com valores lidos pelo teclado
0
1
2
0  1  2
no final, mostre a matriz na tela, com formataçao correta
'''
#SOLUÇÃO DO PROFESSOR: utilizando somente uma lists

matriz = [0,0,0], [0,0,0], [0,0,0]
for l in range(0,3):
  for c in range(0,3):
    matriz[l][c] = int(input(f'Digite o valor para a posição ({l},{c}): '))

for l in range(0,3):
  for c in range(0,3):
    print(end=f'[{matriz[l][c]:^5}]')
  print()