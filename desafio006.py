'''crie um algoritmo que leia o número e mostre o seu dobro, triplo e raiz quadrada'''
n = int(input('insira um valor: '))

dobro = 2 * n
triplo = 3 * n
raiz = n**(1/2)

color = {'verde':'\033[4;32m',
         'azul':'\033[4;36m',
         'vermelho':'\033[4;31m',
         'close':'\033[m'
         }

print(f'seu dobro é {color["verde"]}{dobro}{color["close"]}, seu triplo é {color["azul"]}{triplo}{color["close"]} e sua raiz quadrada é {color["vermelho"]}{raiz:.2f}{color["close"]}')
