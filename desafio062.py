'''
melhore o desafio 061 perguntando para o usuario se ele quer mostrar mais alguns termos. o programa encerra quando ele disser que quer mostrar mais 0 termos
'''

termos = 0
c = 0
n = int(input('digite o primeiro valor: '))
r = int(input('digite a razao: '))
mais = 10
while mais != 0:
    termos = termos + mais
    while c < termos:
        n += r
        c += 1
        print(n,end=' ' )
        if c == termos:
            resposta = input('deseja aficionar mais termos?[S/N]: ')
            if resposta in 'Ss':
                termos = termos + int(input('digite quantos termos deseja adicionar: '))
            else: mais = 0
print(f'foram mostradas {c} termos')