'''
escreva um programa que leia um numero interio qualquer e peça para o usuario escolher qual sera a base de conversao:

-1 para binario
-2 para octal
-3 para hexadecimal

'''
n     = int(input('digite um numero inteiro: '))
opção = int(input('''
escolha para qual base quer converter:
[1] converter para binario
[2] converter para octal
[3] converter para hexadecimal
sua opção: 
'''))

if opção == 1:
    print(f'{n} convertido para binario é igual a {bin(n)[2:]}')
elif opção == 2:
    print(f'{n} convertido para octal é igual a {oct(n)[2:]}')
elif opção == 3:
    print(f'{n} convertido para hexadecimal é igual a {hex(n)[2:]}')
else:
    print('opção invalida, tente novamente')