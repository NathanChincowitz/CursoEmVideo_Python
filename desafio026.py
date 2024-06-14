'''
um programa que leia uma frase pelo teclado e mostre
quantas vezes aparee  a letra "a"
em que posição ela aparece a primeira vez
em que posição ela aparece a ultima vez
'''

nome = input('digite uma frase qualquer: ').upper().strip()

print(f"""
quantidade de 'A': {nome.count('A')}
aparece primeiro em: {nome.find('A')+1}
e por ultimo em: {nome.rfind('A')+1}
""")