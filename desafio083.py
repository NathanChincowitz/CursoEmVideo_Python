'''
crie um programa onde o usuario digita uma expressao qualuqer que use parenteses
seu aplicativo devera analisar se a expressao passada esta com os parenteses abertos e fechados na ordem correta
'''
p_aberto = 0
p_fechado = 0
expressao = str(input('Digite uma expressao matematica: '))

for p in expressao:
    if p == '(':
        p_aberto += 1
    elif p == ')':
        p_fechado += 1
if p_fechado == p_aberto:
    print('sua expressão é válida!')
else:
    print('sua expressao NAO é valida!')