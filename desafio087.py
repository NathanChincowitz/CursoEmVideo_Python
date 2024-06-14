'''
aprimore o desafio anterios mostrando no final:
a) a soma de todos os valores pares digitados
b) a soma dos valores da terceira coluna
c) o maior valor da segunda coluna
'''
matriz = [0,0,0], [0,0,0], [0,0,0]
par = maior = 0
for l in range(0,3):
  for c in range(0,3):
    matriz[l][c] = int(input(f'Digite o valor para a posição ({l},{c}): '))

#somando todos os pares dentro dela
for i in range(0,3):
    for ver in matriz[i]:
        if ver % 2 == 0:
            par += ver

#somando so valores da terceira coluna
terceira = matriz[0][2] + matriz[1][2] + matriz[2][2]

#maior valor da segunda coluna
for i in range(0,3):
    if matriz[i][1] >= maior:
        maior = matriz[i][1]
    


print('A matriz digitada foi:')
for l in range(0,3):
  for c in range(0,3):
    print(end=f'[{matriz[l][c]:^5}]')
  print()

print(f'A soma de todos os valores pares digitados é: {par}')
print(f'a soma dos valores da terceira coluna é: {terceira}')
print(f'o maior valor digitado na segunda coluna foi: {maior}')
