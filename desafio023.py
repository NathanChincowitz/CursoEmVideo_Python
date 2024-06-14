'''
faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
ex:
digite um numero: 1834
unidade:4
dezema:3
centena:8
milhar:1
'''

n = int(input('digite um numero de 0 a 9999: '))
'''
print(f"""
unidade:{n[3]}
dezena:{n[2]}
centena:{n[1]}
milhar:{n[0]}
""")
'''

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f"""
unidade: {u}
dezena: {d}
centena: {c}
milhar: {m}
""")