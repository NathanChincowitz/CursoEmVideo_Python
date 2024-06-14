'''
crie um porograma que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços
'''
f = str(input('digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
inv = ''

# inv = j[::-1]   exemplo do profesor para resolver sem utilizar laço for

for i in range(len(j)-1, -1, -1):
    inv += j[i]

print('a frase', inv)
if inv == j:
    print('é palindromo')
else:
    print('não é um palindromo')